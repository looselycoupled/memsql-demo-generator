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

import time

from producers import Producer
from generators import Generator
from signalers import Signaler

##########################################################################
## Classes
##########################################################################

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    host = 'ec2-52-27-114-107.us-west-2.compute.amazonaws.com'
    p = Producer(host)
    g = Generator(5)
    topic = 'pmu-sim-2'
    signaler = Signaler(topic, p, g, 60)

    try:
        signaler.start()
    except KeyboardInterrupt:
        print '\nExiting program...'



