#!/usr/bin/env python
#Copyright (c) 2014 James Beedy

import os
from Pubnub import Pubnub


class Streamteam(object):

    def __init__(self, args):
        self.channel = args.channel
        self.pubnub = Pubnub(
            args.publish,
            args.subscribe,
            None,
            False
        )

    def publish(self, m):
        def callback(message):
            return message

        self.pubnub.publish(
            self.channel,
            m,
            callback=callback,
            error=callback
        )

    def subscribe(self):

        def callback(message, channel):
                print(message)

        def error(message):
            print("ERROR : " + str(message))

        def connect(message):
            print("CONNECTED")

        def reconnect(message):
            print("RECONNECTED")

        def disconnect(message):
            print("DISCONNECTED")

        self.pubnub.subscribe(
            self.channel,
            callback=callback,
            error=callback,
            connect=connect,
            reconnect=reconnect,
            disconnect=disconnect
        )