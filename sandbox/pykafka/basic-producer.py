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
import pykafka

from pykafka.client import KafkaClient

##########################################################################
## Code
##########################################################################

def main(topic_name):

    host = 'ec2-52-27-114-107.us-west-2.compute.amazonaws.com'
    port = '9092'
    connection = '{}:{}'.format(host, port)

    client = KafkaClient(hosts=connection)

    if topic_name not in client.topics:
        raise KeyError('Topic "{}" Not Found'.format(topic_name))

    topic = client.topics[topic_name]

    import pdb; pdb.set_trace()

    with topic.get_producer() as p:
        p.produce('"vole",1,"M"')






##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    # topic_name = sys.argv[1]
    topic_name = 'farmhouse'
    main(topic_name)


