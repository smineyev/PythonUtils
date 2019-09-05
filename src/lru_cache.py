from datetime import datetime
from io import StringIO
from utils import timing_decorator
from utils import class_timing_decorator

class CacheItem:
  
  def __init__(self, key, value, timestamp):
    self.key = key
    self.value = value
    self.timestamp = timestamp
    self.nextItem = None
    self.prevItem = None

@class_timing_decorator
class LRUCache:

  def __init__(self, maxSize):
    self.memcache = dict()
    self.maxSize = maxSize
    self.head = None
    self.tail = None

  def __str__(self):
    res = StringIO()
    for key, item in self.memcache.items():
      res.write(str(key) + ":" + str(item.value) + " @ " + str(item.timestamp) + "\n")

    return res.getvalue()

  def __getitem__(self, key):
    return self.get(key)

  @timing_decorator
  def get(self, key):
    item = self.memcache.get(key)
    if item != None:
      self.onNewHead(item);
      return item.value
    else:
      return None

  @timing_decorator
  def put(self, key, value):
    item = CacheItem(key, value, datetime.now())
    self.onNewHead(item)
    self.memcache[key] = item

    if (len(self.memcache) > self.maxSize):
      self.remove(self.tail.key)

  @timing_decorator
  def onNewHead(self, item):
    # remove from chain
    if self.tail == item:
      self.tail = item.prevItem

    self.removeFromChain(item)

    #adjust head and tail
    if self.head != None:
      self.head.prevItem = item
    item.nextItem = self.head
    self.head = item

    if self.tail == None:
      self.tail = item

  @timing_decorator
  def remove(self, key):
    item = self.memcache.get(key)
    if item != None:
      self.memcache.pop(key)
      self.onRemove(item)
      return item.value
    else:
      return None

  @timing_decorator    
  def onRemove(self, item):
    self.removeFromChain(item)

    if item == self.head:
      self.head = item.nextItem

    if item == self.tail:
      self.tail = item.prevItem

  @timing_decorator
  def removeFromChain(self, item):
    if item.prevItem != None:
      item.prevItem.nextItem = item.nextItem
      
    if item.nextItem != None:
      item.nextItem.prevItem = item.prevItem  

