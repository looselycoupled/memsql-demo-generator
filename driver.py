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

import argparse

import time

from producers import Producer
from generators import Generator
from signalers import Signaler


HOST    = 'ec2-52-27-114-107.us-west-2.compute.amazonaws.com'
HERTZ   = 60
GENERATOR_LIST_LENGTH = 5

##########################################################################
## Classes
##########################################################################

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )

def main(args):
    p = Producer(HOST)
    g = Generator(GENERATOR_LIST_LENGTH)
    try:
        signaler = Signaler(args.topic, p, g, HERTZ)
        signaler.start()
    except KeyboardInterrupt:
        print '\nExiting program...'

    return 0


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Data generator for MemSQL/Spark/Kafka architecture")
    parser.add_argument("topic", help="kafka topic")
    parser.add_argument("pmu", help="PMU identifier")
    args = parser.parse_args()

    exit(main(args))


