FROM python:3.7

RUN mkdir /app
ADD requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app
RUN rm -rf dcv_bot_env
ENV MODE='prod'
ENV TOKEN='your_token_here'

CMD python /app/bot.py