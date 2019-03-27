"""Telepath

Usage:
  telepath ssh --user=user SERVER ...
  telepath -h | --help
  telepath --version

Options:
  -h --help  Show this screen.
  --version  Version
"""
from docopt import docopt
from prompt_toolkit import prompt
from pssh.clients.native import ParallelSSHClient

def runCommand(command, client):
    print(" Running command %s" %(command))
    output = client.run_command(command)

    for server, serverOutput in output.items():
        for line in serverOutput.stdout:
            print("%s:    %s" % (server, line));

if __name__ == '__main__':
    args = docopt(__doc__, version='1')

    #  print("Got args: ", args)

    client = ParallelSSHClient(args['SERVER'], user=args['--user'])

    runCommand('hostname', client)
    a = prompt('$ ')
    while a != 'exit':
        runCommand(a, client)
        a = prompt('$ ')
