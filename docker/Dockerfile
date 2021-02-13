FROM python:3.7.5-slim
EXPOSE 80
WORKDIR /usr/src/app
RUN python -m pip install -U discord.py python-dotenv
COPY bot.py .
CMD ["python", "bot.py"]
