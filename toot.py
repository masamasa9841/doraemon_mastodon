#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mastodon import Mastodon
 
mastodon = Mastodon(
        client_id="cred.txt", 
        access_token="auth.txt",
        api_base_url = "https://friends.nico") #インスタンス
mastodon.toot("Hello world") #ここを変える
