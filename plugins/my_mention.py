# coding: utf-8

import random
import wikipedia

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

@respond_to('たすけて')
def mention_func(message):
    message.reply('もう大丈夫じゃ。この神通力を飲みなされ')

@listen_to('神通力')
def listen_func(message):
    number = random.random() * 100
    if (number >= 80):
        message.reply('よい神通力じゃ')
    elif (number>=50):
        message.reply('神通力はいらんかね〜')
    else:
        message.reply('呼んだかの？')


@listen_to(r'^\$wiki .+$')
def wiki_func(message):
    str = message.body['text'] #メッセージ取り出し
    keyword = str.split(' ')

    wikipedia.set_lang('jp')
    try:
        rslt = wikipedia.summary(keyword[1])
    except(wikipedia.exceptions.HTTPTimeoutError, wikipedia.exceptions.DisambiguationError,
            wikipedia.exceptions.PageError, wikipedia.exceptions.RedirectError):
        message.send('そんなことより霞(かすみ)を吸いに行かんか')
    else:
        message.send('「' + keyword[1] + '」について教えてやるかの\n>>>' + rslt)
