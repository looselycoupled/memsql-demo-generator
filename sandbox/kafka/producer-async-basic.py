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

def get_client():
    host = 'ec2-52-27-114-107.us-west-2.compute.amazonaws.com'
    port = '9092'
    connection = '{}:{}'.format(host, port)

    # To send messages synchronously
    kafka = KafkaClient(connection)

    return kafka

def main():
    kafka = get_client()
    producer = SimpleProducer(kafka)

    # To send messages asynchronously
    producer = SimpleProducer(kafka, async=True)
    producer.send_messages('farmhouse', '"Meerkat",1,"M"')

    # To wait for acknowledgements
    # ACK_AFTER_LOCAL_WRITE : server will wait till the data is written to
    #                         a local log before sending response
    # ACK_AFTER_CLUSTER_COMMIT : server will block until the message is committed
    #                            by all in sync replicas before sending a response
    # producer = SimpleProducer(kafka, async=False,
    #                           req_acks=SimpleProducer.ACK_AFTER_LOCAL_WRITE,
    #                           ack_timeout=2000,
    #                           sync_fail_on_error=False)

    # responses = producer.send_messages(b'my-topic', b'another message')
    # for r in responses:
    #     logging.info(r.offset)

    # To send messages in batch. You can use any of the available
    # producers for doing this. The following producer will collect
    # messages in batch and send them to Kafka after 20 messages are
    # collected or every 60 seconds
    # Notes:
    # * If the producer dies before the messages are sent, there will be losses
    # * Call producer.stop() to send the messages and cleanup
    # producer = SimpleProducer(kafka, async=True,
    #                           batch_send_every_n=20,
    #                           batch_send_every_t=60)


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    setup_logging()
    main()








