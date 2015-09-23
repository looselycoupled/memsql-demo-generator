# pkg.mod
# description
#
# Author:   Allen Leis <allen@windsorview.com>
# Created:  timestamp
#
# Copyright (C) 2015 windsorview.com
# For license information, see LICENSE.txt
#
# ID: producers.py [] allen@windsorview.com $

"""

"""

##########################################################################
## Imports
##########################################################################

from utils.decorators import memoized
import json

from kafka import SimpleProducer, KafkaClient

##########################################################################
## Classes
##########################################################################

class Producer(object):

    def __init__(self, host, port=9092):
        self.host = host
        self.port = port
        self._producer = SimpleProducer(self.client, async=True)


    @memoized
    def client(self):
        connection = '{}:{}'.format(self.host, self.port)
        return KafkaClient(connection)

    def started(self):
        """
        Logging will eventually go here
        """
        pass

    def finished(self):
        """
        Logging will eventually go here
        """

    def _send(self, topic, message):
        return self._producer.send_messages(topic, message)

    def send(self, topic, message):
        try:
            self.started()
            result = self._send(topic, message)
            self.finished()
        except:
            raise
        else:
            return result


##########################################################################
## Execution
##########################################################################


