#!/usr/bin/env python3

from tqdm import tqdm
from time import sleep
import argparse
import os

CATALOG = {
    "neovim": "sudo apt install -y neovim",
    "figlet": "sudo apt install -y figlet",
    "fzf": "sudo apt install -y fzf",
    "nyancat": "sudo apt install -y nyancat",
    "cmatrix": "sudo apt install -y cmatrix",
    "cbonsai": "sudo apt install -y cbonsai",
    "sl": "sudo apt install -y sl",
    "neofetch": "sudo apt install -y neofetch",
    "lolcat": "sudo gem install lolcat",
    "fortune": "sudo apt install -y fortune",
    "cowsay": "sudo apt install -y cowsay",
    "ranger": "sudo apt install -y ranger",
    "ani-cli": "git clone https://github.com/pystardust/ani-cli.git && cd ani-cli && sudo install ani-cli /usr/local/bin",
    "pokemon-colorscripts": "git clone https://gitlab.com/phoneybadger/pokemon-colorscripts.git && cd pokemon-colorscripts && sudo ./install.sh",
}

FUN = {
    "fortune | cowsay | lolcat",
    "pokemon",
    "camtrix"
}

parser = argparse.ArgumentParser(description='A random command')

parser.add_argument('-i', '--install', help='Install a command', type=str)
parser.add_argument('-f', '--fun', help='List of funny command', action='store_true')
parser.add_argument('-l', '--list', help='List of command', action='store_true')
parser.add_argument('-p', '--print', help='Print the content of a file', type=str)

args = parser.parse_args()

if args.install:
    if(args.install in CATALOG):
        os.system(CATALOG[args.install])
        sleep(1)
        os.system("clear")
        print("Program installed")
        # print(CATALOG[args.install])
    else:
        print("Command not found")

if args.fun:
    print("LIST OF FUNNY COMMAND\n")
    for i in FUN:
        print(i)

if args.list:
    print("LIST OF THE COMMANDS\n")
    for command in CATALOG:
        print(command)

if args.print:
    if os.path.isfile(args.print):
        print(f"Content of {args.print}:\n")
        with open(args.print, 'r') as file:
            print(file.read())
    else:
        print(f"File {args.print} not found.")
