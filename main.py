# -*- coding:utf-8 -*-
import datetime
import json

from mirai import Image, Voice
from mirai import Mirai, WebSocketAdapter, GroupMessage
from mirai.models import BotInvitedJoinGroupRequestEvent,NewFriendRequestEvent

from plugins import wReply

if __name__ == '__main__':
    with open('config.json','r',encoding='utf-8') as fp:
        data=fp.read()
    config=json.loads(data)
    qq=int(config.get('botQQ'))
    key=config.get("vertify_key")
    port= int(config.get("port"))
    bot = Mirai(qq, adapter=WebSocketAdapter(
        verify_key=key, host='localhost', port=port
    ))


    botName = config.get('botName')
    master=int(config.get('master'))

    def loadUser():

        botName = config.get('botName')
        master = config.get('master')
        time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(time1 + '| botName:'+botName+'     |     master:'+master)
        time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(time1 + '| 功能已加载完毕，正在连接mirai-api-http(如出现WARNING可忽略)')




    wReply.main(bot,config)# 自定义回复
    loadUser()
    bot.run()