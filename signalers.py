# pkg.mod
# description
#
# Author:   Allen Leis <allen@windsorview.com>
# Created:  timestamp
#
# Copyright (C) 2015 windsorview.com
# For license information, see LICENSE.txt
#
# ID: signaler.py [] allen@windsorview.com $

"""

"""

##########################################################################
## Imports
##########################################################################

import time

##########################################################################
## Classes
##########################################################################


class Signaler(object):

    def __init__(self, producer, generator, hertz):

        self.hertz      = float(hertz)
        self.rate       = 1.0 / self.hertz
        self.producer   = producer
        self.generator  = generator

    def start(self):
        counter = 0
        for payload in self.generator:
            # yield payload
            payload = '{}     {}'.format(time.time(), payload)
            self.producer.send('farmhouse', payload)
            time.sleep(self.rate)

##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    s = Signaler()
