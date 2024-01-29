<p align="center">
  <img src="https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/blob/master/images/banner/%E7%AB%8B%E7%BB%98_%E6%B5%8A%E5%BF%83%E6%96%AF%E5%8D%A1%E8%92%82_skin1.png" width="470" alt="Goddess" />
</p>

# King's Anime Game Stats

Anime Game Stats is a Python script that retrieves statistics and information from anime games, specifically Genshin Impact and a game called HSR. It utilizes the genshin library to interact with the Hoyolab API and retrieve data such as user stats, achievements, rewards, and character showcases. The retrieved data is then rendered using a Jinja2 template to generate an HTML report.

## Features

- Retrieves Genshin Impact user stats including full stats, Spiral Abyss progress, diary, daily rewards, and character showcases.
- Retrieves HSR (Star Rail) user stats including user stats, character details, diary, forgotten hall challenge, daily rewards, and character showcases (todo).
- Claims daily rewards for both games and redeems codes for extra rewards.
- Generates an HTML report using a Jinja2 template.

## Getting Started

To use Anime Game Stats, you can follow these steps:

### Fork this repository by clicking the "Fork" button on the top right corner of this page. This will create a copy of the repository in your GitHub account.

#### Getting your HoYoLAB cookies

- Go to [HoYoLAB](https://www.hoyolab.com/) (https://www.hoyolab.com/) and log in.
- Go to your profile page.
- Open the developer tools (F12 or Ctrl+Shift+I).
- Go to the "Network" tab.
- Click on the "Preserve Log" / "Persist Logs" button.
- Refresh the page.
- Click on the getGameRecordCard request where the method is "GET" (it should be named "getGameRecordCard" with your HoYoLab UID).
- Go to the "Cookies" tab.
- Copy the "ltuid_v2" cookie value.
- Copy the "ltoken_v2" cookie value.
- Copy the "cookie_token_v2" cookie value.
- Copy the "account_id_v2" cookie value.
- Copy the "ltmid_v2" cookie value.

  ![image](https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/assets/61336116/b3e812c0-1146-46eb-9827-a1208deec72d)

After that, make it cookie into json format, for example
```json
{"ltuid_v2": "...", "ltoken_v2": "...", "cookie_token_v2": "...", "account_id_v2": "...", "ltmid_v2": "..."}
```
### Create a repository secret

![image](https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/assets/61336116/8d822eff-6ade-4c45-87b5-4d67204b44de)

### Paste your json format cookie in the repository secret

![image](https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/assets/61336116/bcf140c6-3e25-4a8d-9d33-04f2a8d90193)

For now the cookie is just supported for genshin and hsr at the same account.

### Give Action Write Permissoion

![image](https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/assets/61336116/615152d3-e548-41a2-9724-74ef4d1a320d)

![image](https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/assets/61336116/2fb0f499-839c-4c7f-a660-76d4053bc786)

### Run the action manually

![image](https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/assets/61336116/accaefd3-3e67-4ee7-a409-1a5d442cb9db)

And you're set! From now on the repo will claim any new codes and redeem the daily check-in rewards at Hoyolab for you every 6 hours!

## Costumization
You can customize the `src/template.html` file to modify the appearance and layout of the generated HTML report.

## Acknowledgments
- [genshin](https://github.com/thesadru/genshin.py) library by thesadru for Genshin Impact, HSR and Honkai Impact 3rd API integration.

## Credits
This repository is the clone of [genshin-stats](https://github.com/thesadru/genshin-stats)
