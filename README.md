# Text my message
Send messages for most famous chat services:

- Google Hangouts Chat
- Slack
- Rocket Chat (not implement yet)
- Telegram (not implement yet)
- Twitter tweets and direct message (not implement yet)


# Installing

This project **only** supports installation cloning the repository.

```
user@machine$ git clone https://github.com/tm-2/text-my-message.git

user@machine$ cd text-my-message && bash install.sh

user@machine$ source ~/.bashrc
```

# Getting started

## Create a configuration template
All the app use a configuration file called `webhooks.json`. This file contains you bots/webhooks url, name, message service

Configuration file location is: `your-home-directory/.textmymessage/config/webhooks.json`

To generate a template file execute the command below:

```
user@machine$ text-my-message -c true
```

## Starting to send messages

### Google Hangouts Chat
- Follow the [official google docs](https://developers.google.com/hangouts/chat/quickstart/incoming-bot-python) to create a bot webhook

- execute from command line terminal the command: `text-my-message -s google -r "ROOM_NAME" -t "TEXT TO SEND"`

- See your room

### Slack
- Follow the [official docs](https://api.slack.com/incoming-webhooks)
- execute from command line terminal the command: `text-my-message -s slack -r "ROOM_NAME" -t "TEXT TO SEND"`

### Telegram
Not implement yet

### Rocket Chat
Not implement yet

### Twitter
Not implement yet