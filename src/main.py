import itertools
import functools
from lru_cache import LRUCache
from types import MethodType
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


"""dic = {}
t1 = ("sergey", "mineyev")
print (t1)
dic[t1] = "programmer"

t2 = ("vikram", "sekhon")
dic[t2] = "fedex contractor"

print (dic)

print ("imperative: ")
for firstname, lastname in dic:
  print (firstname + ": " + dic[firstname, lastname])

print ("new1: ")
f = lambda firstname, lastname: print (firstname + ": " + dic[firstname, lastname])
[f(firstname, lastname) for firstname, lastname in dic]

print ("new2")
[print (firstname + ": " + dic[firstname, lastname]) for firstname, lastname in dic]

lis = [ 1, 3, 4, 10, 4 ] 
print (list(itertools.accumulate(lis,lambda x,y : x+y)))

print (functools.reduce(lambda x,y:x+y,lis)) """

cache = LRUCache(3)
print (cache)

cache.put(1, "v1")
print (cache)

cache.put(2, "v2")
print (cache)

cache.put(3, "v3")
print (cache)

cache.get(1)

cache.put(4, "v4")
print (cache)
