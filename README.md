# Finance telegram-bot

![Status](https://github.com/ikrutik/finance_bot/workflows/Build,%20Test%20and%20Deploy/badge.svg?branch=master)

Interface for working with [finance speadsheet](https://journal.tinkoff.ru/spreadsheet/) via telegram_bot.

Features:

* Get your balance for today.
* Get your purchases for today.
* Add a purchase to the spreadsheet.

## Run

Makefile
```sh
make install_and_run
```

Python run as pooling app
```sh
pipenv run python src/rest/applications/aiogram/application.py
```

Python run as webhook
```sh
pipenv run python src/rest/applications/aiogram/application.py --mode=webhook
```

## Technologies

0. Python 3.8
1. asyncIO
2. aiogram
3. gspread_asyncio
4. Clean Architecture

![](https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

## Basic Usage

0. Edit your `settings.py` file or `local_settings.py`
1. [Obtain OAuth2 credentials from Google Developers Console](http://gspread.readthedocs.org/en/latest/oauth2.html) - `GOOGLE_CREDENTIALS`
2. Get [Google API](https://console.developers.google.com/) credentials -  `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`
3. Copy [spreadsheet](https://docs.google.com/spreadsheets/d/1C_CyWpjUeZGXSHvQgF-YKcxtZvkywsscnJq51stiWEA/copy) to your google drive and set URL -  `SHEET_URL`
5. Create your telegram bot via [@Bot_father](https://core.telegram.org/bots) and set token and user_id -  `TELEGRAM_BOT_TOKEN`, `TELEGRAM_USER_ID`
6. [Optional] Set webhook host -  `WEBHOOK_HOST`
7. Profit 🎐
