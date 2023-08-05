import click
from app import aitest_application


@click.group()
def main():
    """  The  aitest  Command  Line  Interface is a unified tool to manage your aitest
         services.

        To see help text, you can run:

        aitest --help\n
        aitest <command> --help\n
        aitest <command> <subcommand> --help\n

    """

#adding subcommands 
main.add_command(aitest_application.configure)
main.add_command(aitest_application.run)
main.add_command(aitest_application.status)
