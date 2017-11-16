# coding: utf-8

import os

# botアカウントのAPIトークン
API_TOKEN = os.environ['SLACKBOT_TOKEN_SENNIN']

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答
DEFAULT_REPLY = "仙人困っちゃう"

# プラグインリスト
PLUGINS = ['plugins']