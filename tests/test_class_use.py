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
