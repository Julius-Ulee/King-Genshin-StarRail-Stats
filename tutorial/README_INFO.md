<p align="center">
  <img src="https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/blob/master/images/banner/%E7%AB%8B%E7%BB%98_%E6%B5%8A%E5%BF%83%E6%96%AF%E5%8D%A1%E8%92%82_skin1.png" width="470" alt="Goddess" />
</p>

# Anime Game Stats

Anime Game Stats is a Python script that retrieves statistics and information from anime games, specifically Genshin Impact and a game called HSR. It utilizes the genshin library to interact with the Hoyolab API and retrieve data such as user stats, achievements, rewards, and character showcases. The retrieved data is then rendered using a Jinja2 template to generate an HTML report.

## Features

- Retrieves Genshin Impact user stats including full stats, Spiral Abyss progress, diary, daily rewards, and character showcases.
- Retrieves HSR (Star Rail) user stats including user stats, character details, diary, forgotten hall challenge, daily rewards, and character showcases (todo).
- Claims daily rewards for both games and redeems codes for extra rewards.
- Generates an HTML report using a Jinja2 template.

## Getting Started

To use Anime Game Stats, you can follow these steps:

### Fork this repository by clicking the "Fork" button on the top right corner of this page. This will create a copy of the repository in your GitHub account.
#### Copy your cookies

Log in at [hoyolab](https://hoyolab.com), open the developer console by pressing F12 on your keyboard and navigate to the console tab. Finally, paste the following in the console to copy your cookies to your clipboard

`copy(document.cookie)`

![image](https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/assets/61336116/2d21f1a1-aa91-44f4-9281-d22e1f38bf04)


After that, make it cookie into json format, for example
```json
{"ltuid": "...", "ltoken": "....", "account_id": "...", "cookie_token": "..."}
```
### Create a repository secret

![image](https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/assets/61336116/8d822eff-6ade-4c45-87b5-4d67204b44de)


### Paste your json format cookie in the repository secret

![image](https://github.com/Julius-Ulee/King-Genshin-StarRail-Stats/assets/61336116/2ba5961b-d446-41a7-aa4b-cf9646852473)


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
