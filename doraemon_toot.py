#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import linecache
from mastodon import Mastodon

mastodon = Mastodon(
        client_id="cred.txt", 
        access_token="auth.txt",
        api_base_url = "https://friends.nico") #インスタンス
rand = random.randint(1,1945)
target_line = linecache.getline('tool_list.txt', rand)
linecache.clearcache() 
mastodon.toot(target_line) #ここを変える

