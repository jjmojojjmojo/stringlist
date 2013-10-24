"""
Test use of StringList as an attribute in a class
"""

import unittest

class TestDescripterClassUse(unittest.TestCase):
    
    def setUp(self):
        from stringlist import StringList
        
        class Setup(object):
            roles = StringList() 
    
        self._class = Setup
        
    def test_set_roles(self):
        obj = self._class()
        
        obj.roles = 'lead'
        
        self.assertEquals(obj.roles, 'lead')
        
        obj.roles = ['great', 'scott']
        
        self.assertEquals(obj.roles, ['great', 'scott'])
        
        obj.roles += 'hola'
        
        self.assertEquals(obj.roles, ['great', 'scott', 'hola'])
        
    def test_set_many_roles(self):
        obj = self._class()
        
        obj.roles = 'first', 'second'
        
        self.assertEquals(obj.roles, ['first', 'second'])
        
    def test_initialize_many_roles(self):
        """
        Can we initialize the StringList in a class with multiple values?
        """
        from stringlist import StringList
        
        class SpecialThing(object):
            roles = StringList()
            
            def __init__(self, roles):
                self.roles = roles
        
        obj = SpecialThing(['one', 'two'])
        
        self.assertEquals(obj.roles, ['one', 'two'])
