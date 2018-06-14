#!/usr/bin/python

class hist:
    def __init__(self):
        self.hist = {}
        self.list_of_values = {}

    def fill(self, key, incr = 1):
        if not key in self.hist:
            self.hist[key] = 0
            self.list_of_values[key] = []
        self.hist[key] += incr
        self.list_of_values[key].append(incr)

    def xrange(self, sort='value'):
        if sort!='value':
            return [x for x in sorted(self.hist, reverse=True)]
        else:
            return [x for x in sorted(self.hist, key=lambda k:
                                      self.hist[k], reverse=True)]

    def yrange(self, sort='value'):
        if sort!='value':
            return [self.hist[x] for x in sorted(self.hist,
                                                 reverse=True)]
        else:
            return [self.hist[x] for x in sorted(self.hist, key=lambda
                                                 k: self.hist[k],
                                                 reverse=True)]
