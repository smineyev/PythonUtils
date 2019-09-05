import time
from types import MethodType

def timing_decorator(func):
  def inner(*args, **kwargs):
    print ("Entered: "+func.__name__)
    startTime = time.time()
    res = func(*args, **kwargs)
    d = (time.time() - startTime)*1000
    print ("\'%s\' call took %f ms"%(func.__name__,d))
    print ("Finished: "+func.__name__)
    return res
  
  return inner

def class_timing_decorator(original_class):

  orig_init = original_class.__init__
  # Make copy of original __init__, so we can call it without recursion

  def __init__(orig_self, *args, **kws):
    methods = [func for func in dir(original_class) if callable(getattr(original_class, func)) and  not func.startswith("__")]

    for method in methods:
      print (original_class.__dict__[method])
      orig_method = original_class.__dict__[method]

      def new_method(new_self, *new_args, **new_kwargs):
        print ("new_method ""%s"" with args %sm %s, %s: "%(orig_method.__name__, str(new_self), str(new_args), str(new_kwargs)))
        return orig_method(new_self, *new_args, **new_kwargs)

      orig_self.__dict__[method] =  MethodType(new_method, orig_self)

    print (orig_self.__dict__)

    orig_init(orig_self, *args, **kws) # Call the original __init__
    print ("init with args: %s %s, %s"%(str(orig_self), str(args), str(kws)))

  original_class.__init__ = __init__ # Set the class' __init__ to the new one
  return original_class



  
