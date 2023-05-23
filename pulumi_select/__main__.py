import os, sys
import click, click_spinner
import json
import inquirer
import subprocess
import re

def main(args=None):
    click.secho('Pulumi preview in progress ...', fg='green')
    with click_spinner.spinner():
        subprocess.call('pulumi preview -j > /tmp/preview.json',shell=True,executable='/bin/zsh')

    create = []
    update = []
    delete = []
    with open('/tmp/preview.json') as f:
        data = json.load(f)
        for change in data['steps']:
            if change['op'] == 'create':
                create.append('\u001b[32m' + change['urn'] + '\033[0m')
            elif change['op'] == 'update':
                update.append('\u001b[33m' + change['urn'] + '\033[0m')
            elif change['op'] == 'delete':
                delete.append('\u001b[31m' + change['urn'] + '\033[0m')

    choices = create + update + delete
    questions = [
    inquirer.Checkbox('pulumiup',
                        message="What resources do you want to filter on?",
                        choices=choices,
                        ),
    ]

    answers = inquirer.prompt(questions)
    # remove ascii color code from answers
    answers['pulumiup'] = [re.sub(r'\x1b[^m]*m', '', x) for x in answers['pulumiup']]

    pulumi_command = "pulumi up "
    for answer in answers['pulumiup']:
        pulumi_command += "-t "+ answer + " "

    click.secho(pulumi_command, fg='green')

if __name__ == "__main__":
    sys.exit(main())
