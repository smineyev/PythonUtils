import time
from types import MethodType

def timing_decorator(func):
    def inner(*args, **kwargs):
        print ("Entered: "+func.__name__)
        startTime = time.time()
        res = func(*args, **kwargs)
        d = (time.time() - startTime)*1000
        print ("Finished %s in %f ms"%(func.__name__, d))
        return res
  
    return inner

def class_timing_decorator(original_class):

    orig_init = original_class.__init__
    # Make copy of original __init__, so we can call it without recursion
    
#     def new_method_maker(p_orig_method):
#         def new_method(new_self, *new_args, **new_kwargs):
#             res = timing_decorator(p_orig_method)(new_self, *new_args, **new_kwargs)
#             return res;
#         return new_method

    def __init__(orig_self, *args, **kws):
        methods = [func for func in dir(original_class) if callable(getattr(original_class, func)) and  not func.startswith("__")]
     
        for method_name in methods:
            orig_method = original_class.__dict__[method_name]
            orig_self.__dict__[method_name] =  MethodType(timing_decorator(orig_method), orig_self)
#             print ("mapped old method %s to new method %s"%(orig_self.__dict__[method], orig_method.__name__))
     
        orig_init(orig_self, *args, **kws) # Call the original __init__
        
    original_class.__init__ = __init__ # Set the class' __init__ to the new one
    return original_class



  
