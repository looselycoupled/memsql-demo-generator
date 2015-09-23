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

import math
import random

##########################################################################
## Classes
##########################################################################

class Generator(object):

    def __init__(self, size):
        self.values = random.sample(range(0,360), size)

    def incr(self):
        for index, value in enumerate(self.values):
            value += 1
            if value == 361:
                value = 0
            self.values[index] = value

    def transform(self, data):
        result = []
        for el in self.values:
            result.append(math.sin(math.radians(el)))
        return result

    def __iter__(self):
        try:
            while True:
                yield self.transform(self.values)
                self.incr()

        except Exception as e:
            raise


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    g = Generator(3)
    for values in g:
        print values
