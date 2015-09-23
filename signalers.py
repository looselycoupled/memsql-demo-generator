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

    def __init__(self, topic, producer, generator, hertz):

        self.topic      = topic
        self.producer   = producer
        self.generator  = generator

        self.hertz      = float(hertz)
        self.rate       = 1.0 / self.hertz

        self.beginning  = None
        self.counter    = None


    def transform(self, payload):
        return ','.join(map(str,payload))


    def wait(self):
        """
        returns the amount of time (as float) that we should wait before
        the next iteration
        """
        # how much time have we used and is remaining
        elapsed = time.time() - self.beginning
        time_remaining = 1.0 - elapsed

        # Find time remaining if we're done.  Otherwise return
        # the time remaining divided but 1 + the number of loops remaining
        if self.counter == 0:
            # wait the balance of the time remaining
            period = max(time_remaining, 0)
        else:
            period = max(time_remaining / float(self.counter + 1), 0)

        # go to sleep for an appropriate amount of time
        time.sleep(period)

        # reset clock if nescessary
        if self.counter == 0:
            self.reset_clock()


    def reset_clock(self):
        self.beginning = time.time()
        self.counter = int(self.hertz)


    def signal(self, message):
        self.producer.send(self.topic, self.transform(message))
        self.counter -= 1


    def start(self):
        self.reset_clock()
        for payload in self.generator:
            self.signal(payload)
            self.wait()





##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    s = Signaler()
