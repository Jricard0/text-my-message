import argparse
from classes.google_chat import GoogleChat
from classes.slack import Slack
from termcolor import colored
from classes.version import APP_NAME
from classes.configuration import Configuration


def create_arguments():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-s', '--service')
    arg_parser.add_argument('-r', '--room')
    arg_parser.add_argument('-t', '--text')
    arg_parser.add_argument('-dm', '--direct-message')
    arg_parser.add_argument('-c', '--configure')
    arg_parser.add_argument('-b', '--bot-name')
    arg_parser.add_argument('-i', '--icon')
    # use '+' for 1 or more args (instead of 0 or more)
    arg_parser.add_argument('arg', nargs='*')
    parsed_args = arg_parser.parse_args()

    return vars(parsed_args)


def __validate_arguments__(args):
    if args['service'] and args['text'] and args['room']:
        return True


def main():

    arguments = create_arguments()

    if arguments['configure'] != None:
        Configuration.create_configurations()
        print(colored("Success:", color='green'),
              "Configuration template was created")
        exit(0)

    if __validate_arguments__(arguments):
        if arguments['service'] == 'google':
            print("google")
            google_chat = GoogleChat(
                room=str(arguments['room']),
                text=str(arguments['text'])
            )

            google_chat.perform()

        elif arguments['service'] == 'slack':

            slack_service = None

            if arguments['icon'] != None:
                slack_service = Slack(room=arguments['room'], text=arguments['text'], icon=str(arguments['icon']))
            else:
                slack_service = Slack(room=arguments['room'], text=arguments['text'], icon='ghost')

            slack_service.perform()

        elif arguments['service'] == 'rocket':
            print("rocket")

        elif arguments['service'] == 'twitter':
            if 'direct_message' in arguments and arguments['direct_message']:
                print(f"Send on dm: {arguments['direct_message']}")
            print("twitter")

        elif arguments['service'] == 'telegram':
            print("telegram")

        else:
            print(colored(f"Error:", color='red'),
                  f"Invalid value '{arguments['service']}' for parameter SERVICE")
            print(colored(f"Warning:", color='yellow'),
                  "Possible values are => google, slack, telegram and twitter")
    else:
        print(colored(f"Error:", color='red'), f"Arguments are not valid")
        print(colored(f"Usage:", color='yellow'), f"{APP_NAME} -h")


if __name__ == "__main__":
    main()
