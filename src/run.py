# coding: utf-8

from slackbot.bot import Bot
import os
import sys

'''
プロセスをデーモン化します。
'''
def daemonize():
    def fork():
        if os.fork():
          sys.exit()

    fork()
    os.setsid()
    fork()


def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    #daemonize()
    main()