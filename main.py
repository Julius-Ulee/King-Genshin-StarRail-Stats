import argparse
import asyncio
import logging
import os
import io
import pathlib
import json
import pytz
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime

import genshin
import jinja2

logger = logging.getLogger()
load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--template", default="src/template.html", type=pathlib.Path)
parser.add_argument("-o", "--output", default="output/stats.html", type=pathlib.Path)
parser.add_argument("-c", "--cookies", default=None)
parser.add_argument("-l", "--lang", "--language", choices=genshin.LANGS, default="en-us")


def format_date(date: "datetime"):
    tz = pytz.timezone("Asia/Jakarta")
    now = date.now(tz=tz)
    fmt = f"{now.strftime('%b')} \
            {now.strftime('%d')}, \
            {now.strftime('%Y')} \
            {now.strftime('%H:%M %z')}"
    return fmt


async def main():
    args = parser.parse_args()
    debug = args.verbose

    # type: <class 'str'>
    _c = os.getenv("COOKIES")
    # must loads to dict
    cookies = json.loads(_c)

    client = genshin.Client(cookies, debug=debug, game=genshin.Game.GENSHIN)

    user = await client.get_full_genshin_user(0, lang=args.lang)
    abyss = user.abyss.current if user.abyss.current.floors else user.abyss.previous
    diary = await client.get_diary()

    # claim daily reward genshin
    try:
        await client.claim_daily_reward(lang=args.lang, reward=False)
    except genshin.AlreadyClaimed:
        pass
    finally:
        reward = await client.claimed_rewards(lang=args.lang).next()
        reward_info = await client.get_reward_info()

    # claim daily reward honkai star rail
    try:
        await client.claim_daily_reward(lang=args.lang, reward=False, game=genshin.types.Game.STARRAIL)
    except genshin.AlreadyClaimed:
        pass
    finally:
        sr_reward = await client.claimed_rewards(lang=args.lang, game=genshin.types.Game.STARRAIL).next()
        sr_reward_info = await client.get_reward_info(game=genshin.types.Game.STARRAIL)

    template: jinja2.Template = jinja2.Template(args.template.read_text())
    rendered = template.render(
        user=user,
        lang=args.lang,
        abyss=abyss,
        reward=reward,
        sr_reward=sr_reward,
        diary=diary,
        reward_info=reward_info,
        sr_reward_info=sr_reward_info,
        updated_at=format_date(reward.time),
        _int=int
    )
    args.output.write_text(rendered)

    #Get New Code
    res = requests.get("https://www.pockettactics.com/genshin-impact/codes")
    soup = BeautifulSoup(res.text, 'html.parser')

    active_codes = [code.text.strip() for code in soup.find("div", {"class":"entry-content"}).find("ul", recursive=False).findAll("strong")]

    codes_file = pathlib.Path(__file__).parent.resolve() / "codes.txt"
    used_codes = codes_file.open().read().split("\n")
    new_codes = list(filter(lambda x: x not in used_codes and x != "", active_codes))
    
    # Redeem New Code
    failed_codes = []
    for code in new_codes[:-1]:
        try:
            await client.redeem_code(code)
        except Exception as e:
            failed_codes.append(code)
        time.sleep(5.2)
    if len(new_codes) != 0:
        try:
            await client.redeem_code(new_codes[-1])
        except Exception as e:
            failed_codes.append(new_codes[-1])

    redeemed_codes = list(filter(lambda x: x not in failed_codes, new_codes))
    if len(redeemed_codes) != 0:
        print("Redeemed " + str(len(redeemed_codes)) + " new codes: " + ", ".join(redeemed_codes))
    else:
        print("No new codes found")

    # Add new codes to used codes
    used_codes.extend(new_codes)
    io.open(codes_file, "w", newline="\n").write("\n".join(used_codes))

if __name__ == "__main__":
    asyncio.run(main())
