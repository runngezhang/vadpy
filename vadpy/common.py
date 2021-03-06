import os 
import re
import functools

class Object(object):
    pass

def listdir(path, *exprs):
   """Return a list of files from a directory filtered by regular expression

   path  - directory path
   exprs - a string or a list of strings with regular expression(s) (None for listdir behaviour)
   """
   files = sorted(os.listdir(path))
   if not any(exprs):
       return files

   reos = [re.compile(rexp) for rexp in exprs  
           if rexp]
   files = [f for f in files 
            if any((reo.match(f) for reo in reos))]

   return files


def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        pass

def calloverridden(f):
    @functools.wraps(f)
    def wrapper(self, *args, **kw):
        if getattr(self, f.__name__).im_func != wrapper:
            return f(self, *args, **kw)
    return wrapper
