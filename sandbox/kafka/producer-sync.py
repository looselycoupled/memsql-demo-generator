# pkg.mod
# description
#
# Author:   Allen Leis <allen@windsorview.com>
# Created:  timestamp
#
# Copyright (C) 2015 windsorview.com
# For license information, see LICENSE.txt
#
# ID: 1-pykafka.py [] allen@windsorview.com $

"""

"""

##########################################################################
## Imports
##########################################################################

from kafka import SimpleProducer, KafkaClient
import logging

##########################################################################
## Code
##########################################################################

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )


def main():
    logger = logging.getLogger()

    host = 'ec2-52-27-114-107.us-west-2.compute.amazonaws.com'
    port = '9092'
    connection = '{}:{}'.format(host, port)

    # To send messages synchronously
    kafka = KafkaClient(connection)
    producer = SimpleProducer(kafka)

    # Note that the application is responsible for encoding messages to type bytes
    producer.send_messages('farmhouse', '"Tiger",5,"M"')




##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    setup_logging()
    main()

