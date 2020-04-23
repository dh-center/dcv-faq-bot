# Data, Culture & Visualization telegram bot

Telegram bot for DCV Master program FAQ.

## Getting Started

If you copy the project and running on your local machine for development and testing 
purposes you should:
1. Install requirements
2. Set environment variables: `MODE`, `TOKEN`
3. Start `bot.py` script

See deployment for notes on how to deploy the project on a live system.

### Installing
Clone this repo:
```shell script
git clone https://github.com/amamonova/dcv_bot
```
Change working directory to repo folder. 
Inside your environment:
```
pip install requirements.txt
set TOKEN 'telegram_API_token'
set MODE 'dev'
```

Note, permissible values for `MODE` are [`dev`, `prod`, `prod_heroku`]. 

For `prod_heroku` set env variable `HEROKU_APP_NAME`.

## Deployment
Clone this repo:
```shell script
git clone https://github.com/amamonova/dcv_bot
```

Add TOKEN in Dockerfile.

Let's use docker container:
```shell script
docker build -t dcv_bot:v1 .
docker run dcv_bot:v1
```

That's pretty much it. 