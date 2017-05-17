#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import linecache
from mastodon import Mastodon

#toot準備
mastodon = Mastodon(
        client_id="cred.txt", 
        access_token="auth.txt",
        api_base_url = "https://friends.nico") #インスタンス

#1~2309の乱数生成
rand = random.randint(1,2309)

#変数に道具or性器を代入
target_line = linecache.getline('tool_list.txt', rand)

#キャッシュをクリア
linecache.clearcache() 

#toot
mastodon.toot(target_line)
