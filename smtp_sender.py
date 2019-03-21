#!/usr/bin/python
"""smtp_sender.py

Simple mail service.


Usage:

    python smtp_sender.py -server=<server> -port=<port> -from=<mailfrom> -to=<mailto> -msg=<msg>

"""
from SMTPClient import *

import argparse
import sys


def createParser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
            '-s',
            '--server',
            help='Server Address',
            required=True)
    parser.add_argument(
            '-p',
            '--port',
            help='Port Number',
            required=True)
    parser.add_argument(
            '-f',
            '--from',
            help='Sender address',
            required=True)
    parser.add_argument(
            '-t',
            '--to',
            help='Recipient address',
            required=True)
    parser.add_argument(
            '-m',
            '--msg',
            help='',
            required=True)
    return parser

def sendMsg(args):
    smtpClient = Client(
            serverAddr=args['server'],
            serverPort=int(args['port']))
    smtpClient.setFromTo(args['from'], args['to'])
    smtpClient.setMsg(args['msg'])
    smtpClient.takeDown()

def main():
    parser = createParser()
    args = vars(parser.parse_args())
    send_msg(args)
    exit(0)

main()
