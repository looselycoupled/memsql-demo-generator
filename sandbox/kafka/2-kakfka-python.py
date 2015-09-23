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

import sys
from kafka import KafkaConsumer
import logging



##########################################################################
## Code
##########################################################################

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.DEBUG
    )


def main():
    logger = logging.getLogger()

    host = 'ec2-52-27-114-107.us-west-2.compute.amazonaws.com'
    ip_address = '52.27.114.107'
    ip_address = '127.0.0.1'
    port = '9092'
    connection = '{}:{}'.format(host, port)

    # To consume messages
    print connection
    consumer = KafkaConsumer('farmhouse', bootstrap_servers=[connection])

    for message in consumer:
        import pdb; pdb.set_trace()
        print 'HELLO'
        logger.info('HELLO THERE')
        logger.info(message)
        # message value is raw byte string -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        # print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
        #                                      message.offset, message.key,
        #                                      message.value))


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    setup_logging()

    main()
