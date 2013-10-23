stringlist
==========

Python class that acts like a string or a list depending on the context.

Its primary goal is to be used as API sugar for a "one or many" property on an object.

The initial use case was for a "role" attribute, which mapped to Chef configuration management attributes. Its common to have one role, or have many. 

I ran into an issue when other people used the API - initially it assumed that the role attribute was always a list, and do some processing when saving. Some less experienced users would assign a bare string to the attribute, and since a string is an iterable, it wouldn't fail; instead the role list would essentially consist of individual characters of the role name.

StringList handles this common case elegantly.

The conversion from string to list happens when the .append() method is called. 

Pull requests, suggestions, edge cases to test, and issues are greatly appreciated.

Developed and tested in Python 2.7.3.

Potential Issues
================
There are a few quirks worth noting in this implementation:

- When doing addition on a StringList that is in 'list mode', the way objects are just appended to the list is not representative of how Python works. Normally if you try to add anything to a list that isn't a list, a TypeError is raised.
- Adding objects to a 'string mode' StringList just fails if they are not strings (raises a TypeError). It may make more sense for the object to be cast to a string and concatenated to draw the implementation in line with how 'list mode' addition works.
- There is no way to go back to a single string value.

Example
=======

::
    
    class Instance(object):
        """
        Arbitrary class representing a single chef node.
        """
        
        role = StringList()
        name = None
        
        def __init__(self, name, role=None):
            self.name = name
            self.role = role
            
            
    # initialized with the string 'master' as the value of inst.role
    inst = Instance('node1', 'master')
    
    # now inst.role is a list, ['master', 'secondary']
    inst.role.append("secondary")
    
    # it's a string again, overriding what was there
    inst.role = "server"
    
    # now it's adding a word to the name - 'server special'
    inst.role += " special'
    
    # converted into a list again - ['server special', 'server basic']
    inst.role.append('server basic')
    
    # addition works here too - ['server special', 'server basic', 'classic']
    inst.role.append('classic')
    
    # typical list operations work too - ['server basic', 'classic']
    del inst.role[0]
    
    
