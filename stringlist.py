import copy
import collections

class StringList(object):
    """
    It looks like a string, acts like a string, but if you call append on it, 
    it magically transforms into a list.
    
    Supports some useful API constructs, like += addition.
    """
    
    # the internal value, will be a string or a list (but always iterable) 
    # depending on the circumstances
    _val = None
    
    def __init__(self, *args):
        """
        Constructor can take any number of arguments, some logic happens to
        decide if there is a single string or many individual
        objects.
        """
        if len(args) == 1:
            if not isinstance(args[0], str):
                self._val = list(args[0])
            else:
                self._val = args[0]
        elif len(args) == 0:
            self._val = ""
        else:
            self._val = list(args)
          
    def append(self, value):
        """
        Append is not a string method. The use of this method indicates that
        you really wanted a list, not a string, so the internal value is 
        converted.
        """
        if isinstance(self._val, str):
            if not self._val == '':
                self._val = [self._val,]
            else:
                self._val = []
        
        self._val.append(value)
            
    def __len__(self):
        """
        Handle len()
        """
        return len(self._val)
        
    def __getitem__(self, key):
        """
        Item retreval (e.g. self[1])
        """
        return self._val.__getitem__(key)
        
    def __setitem__(self, key, value):
        """
        Item assignment (e.g. self[1] = 'four')
        """
        self._val[key] = value
        
    def __delitem__(self, key):
        """
        Item removal (e.g. del self[1])
        """
        del self._val[key]
       
    def __iter__(self):
        """
        Iterator for [x for x in self] and similar looping
        """
        return iter(self._val)
        
    def __contains__(self, item):
        """
        Handle "if 'string' in self"
        """
        return item in self._val
        
    def _add(self, seed, other):
        """
        Centralize the addition logic into a single method.
        
        Will concatenate other to seed if seed is a string.
        
        If seed is not a string, assume it's a list.
        
        If seed is a list, and other is some kind of iterable, 
        extend seed with other.
        
        If seed is a list, and other is a string, append other to seed.
        
        If other is a StringList, recurse on the internal value of other
        """
        if isinstance(other, StringList):
            other = copy.copy(other._val)
        
        if isinstance(seed, list):
            if isinstance(other, collections.Iterable) and not isinstance(other, str):
                seed.extend(other)
            else:
                seed.append(other)
        else:
            seed += other
            
        return seed
        
    def __add__(self, other):
        """
        Addition - return a new StringOrList object
        """
        # make a copy of the internal structure so we don't alter it
        seed = self._add(copy.copy(self._val), other)
        
        return StringList(seed)
        
    def __iadd__(self, other):
        """
        Assignment and addition
        """
        self._val = self._add(self._val, other)
            
        return self
        
    def __repr__(self):
        """
        Proxy the representation/cast to string
        """
        return self._val.__repr__()
        
    def __eq__(self, other):
        """
        Proxy equality
        """
        return self._val.__eq__(other) 
        
    def __getattr__(self, name):
        """
        All other undefined non-magic methods get proxied to the internal
        object.
        """
        return getattr(self._val, name)
        
    def __set__(self, instance, value):
        """
        Allow descriptor use.
        """
        self.__init__(value)
