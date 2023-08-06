"""
snaketest.

A small package to help test and prototype snakemake rules
"""

__version__ = "0.1.0"
__author__ = 'Albert'
__credits__ = 'Me'

from itertools import product
class snaketest(object):
    def __init__(self,**xargs):
        self.items = xargs
    def __getattribute__(self,attr):
        if attr=="items":
            return object.__getattribute__(self, "items")
        attr =  object.__getattribute__(self, "items")[attr]
        if type(attr)==str:
            if ('{' in attr ) and ("wildcards" in globals()):
                attr = attr.format(**wildcards.items)
        if type(attr)==list:
            new = []
            for i in attr:
                if type(i)==str:
                    if ('{' in i ) and ("wildcards" in globals()):
                        new.append(i.format(**wildcards.items))
                    else:
                        new.append(i)
                else:
                    new.append(i)
            attr = new
        return attr

def expand(s,**xargs):
    out = []
    for a in (product(*[[(a,c) for c in b] for a,b in xargs.items()])):
        out.append(s.format(**dict(a)))
    return out

temporary = lambda x:x
protected = lambda x:x
directory = lambda x:x
ancient   = lambda x:x
