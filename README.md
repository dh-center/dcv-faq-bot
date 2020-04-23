# Data, Culture & Visualization telegram bot

Telegram bot for DCV Master program FAQ.

## Getting Started

If you copy the project and running on your local machine for development and testing 
purposes you should:
1. Install requirements
2. Set environment variables: `MODE`, `TOKEN` in .env file (use `.env.sample` as an example)
3. Start `bot.py` script

See deployment for notes on how to deploy the project on a live system.

### Installing
Clone this repo:
```shell script
git clone https://github.com/dh-center/dcv-faq-bot.git
```
Change working directory to repo folder. 
Inside your environment:
```
pip install requirements.txt
cp .env.sample .env
```

Note, permissible values for `MODE` are [`dev`, `prod`, `prod_heroku`]. 

For `prod_heroku` set env variable `HEROKU_APP_NAME`.

## Deployment to prod
1. Copy `docker-compose.prod.yml`
2. Create `.env` file and fill necessary variables (see `.env.sample`)
3. Run `docker-compose -f docker-compose.prod.yml up`