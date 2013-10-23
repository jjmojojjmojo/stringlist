"""
Test basic functionality
"""

import unittest

class TestStringList_StartWithString(unittest.TestCase):
    """
    Test basic functionality of a StringList when the initial value is a 
    string.
    """

    def setUp(self):
        from stringlist import StringList
        self.sl = StringList('hello world')
        self.sl2 = StringList()
        
    def test_empty_stringlist(self):
        """
        What happens when a StringList is initialized with no parameters?
        """
        self.assertEquals(self.sl2, "")
        self.sl2 += 'foo'
        self.assertEquals(self.sl2, "foo")
    
    def test_empty_stringlist_convert(self):
        """
        What happens when a StringList is initialized with no parameters and append() is called?
        """
        self.sl2.append('foo')
        self.assertEquals(self.sl2, ['foo'])
    

    def test_string_split(self):
        """
        Does split() work as expected?
        """
        self.assertEquals(self.sl.split(' '), ['hello', 'world'])
        
    def test_string_array(self):
        """
        Do the string index/slice methods work?
        """
        self.assertEquals(self.sl[1:3], 'el')
        self.assertEquals(self.sl[0], 'h')
        
    def test_string_addition(self):
        """
        Can we add two stringlist objects together, if they are strings?
        """
        new_sl = self.sl + " wow!"
        
        self.assertEquals(new_sl, "hello world wow!")
        
        # make sure the original property isn't altered.
        self.assertEquals(self.sl, "hello world")
        
    def test_string_iaddition(self):
        """
        Can we do an inline addition of another string?
        """
        self.sl += " zoinks!"
        
        self.assertEquals(self.sl, "hello world zoinks!")
        
    def test_string_conversion(self):
        """
        Convert from a string to an array
        """
        self.sl.append('foo bar')
        
        self.assertEquals(self.sl, ['hello world', 'foo bar'])
        
    def test_iteration(self):
        """
        Use the StringList in a loop
        """
        output = []
        
        for x in self.sl:
            output.append(x)
        
        self.assertEquals(output, ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'])
        
        self.assertEquals([x for x in self.sl], ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'])
        
    def test_contains(self):
        """
        Does x in StringList work?
        """
        self.assertTrue('e' in self.sl)
        self.assertFalse('x' in self.sl)
        
    def test_delete(self):
        """
        Test del StringList[x] - should raise an exception
        """
        with self.assertRaises(TypeError):
            del self.sl[1]
            
    def test_index_assignment(self):
        """
        Test StringList[x] = 'c' - should raise an exception
        """
        with self.assertRaises(TypeError):
            self.sl[1] = 'd'
       
    def test_length(self):
        """
        len(StringList)
        """
        self.assertEquals(len(self.sl), 11)
        
    def test_inline_addition_integer(self):
        """
        StringList += 100
        """
        with self.assertRaises(TypeError):
            self.sl += 100
        
    def test_addition_object(self):
        """
        StringList + 100
        """
        with self.assertRaises(TypeError):
            new_sl = self.sl + 100
            
    def test_cast_to_string(self):
        """
        str(StringList)
        """
        self.assertEquals(str(self.sl), "'hello world'")
        
class TestStringList_StartWithList(unittest.TestCase):
    """
    Test basic functionality of a StringList when the initial value is a series
    of strings.
    """

    def setUp(self):
        from stringlist import StringList
        self.sl = StringList('hello', 'world')
        
    def test_getitem_slice(self):
        """
        Does index and slice access work?
        """
        self.assertEquals(self.sl[0], 'hello')
        self.assertEquals(self.sl[:-1], ['hello'])
        
    def test_pop(self):
        """
        Does a common function proxy properly?
        """
        self.sl.pop()
        
        self.assertEquals(self.sl, ['hello'])
        
    def test_addition_string(self):
        """
        Does StringList + a string work?
        """
        new_sl = self.sl + 'foo'
        
        self.assertEquals(new_sl, ['hello', 'world', 'foo'])
        
        # make sure the original property isn't altered.
        self.assertEquals(self.sl, ['hello', 'world'])
        
    def test_addition_list(self):
        """
        Does StringList += a list work?
        """
        new_sl = self.sl + ['foo', 'bar']
        
        self.assertEquals(new_sl, ['hello', 'world', 'foo', 'bar'])
        
        # make sure the original property isn't altered.
        self.assertEquals(self.sl, ['hello', 'world'])
        
    def test_inline_addition_string(self):
        """
        Does StringList += a string work?
        """
        self.sl += 'foo'
        
        self.assertEquals(self.sl, ['hello', 'world', 'foo'])
        
    def test_inline_addition_list(self):
        """
        Does StringList += a list work?
        """
        self.sl += ['foo', 'bar']
        
        self.assertEquals(self.sl, ['hello', 'world', 'foo', 'bar'])
        
    def test_iteration(self):
        """
        Can you loop over a StringList?
        """
        output = []
        
        for x in self.sl:
            output.append(x)
            
        self.assertEquals(output, ['hello', 'world'])
            
        self.assertEquals([x for x in self.sl], ['hello', 'world'])
        
    def test_contains(self):
        """
        Does x in StringList work?
        """
        self.assertTrue('hello' in self.sl)
        self.assertFalse('foo' in self.sl)
        
    def test_delete(self):
        """
        Test del StringList[x]
        """
        del self.sl[0]
        
        self.assertEquals(self.sl, ['world'])
        
    def test_index_assignment(self):
        """
        Test StringList[x] = 'string'
        """
        self.sl[1] = 'foo'
        
        self.assertEquals(self.sl, ['hello', 'foo'])
        
    def test_length(self):
        """
        len(StringList)
        """
        self.assertEquals(len(self.sl), 2)
        
        
    def test_inline_addition_integer(self):
        """
        StringList += 100
        """
        self.sl += 100
            
        self.assertEquals(self.sl, ['hello', 'world', 100])
        
    def test_addition_object(self):
        """
        StringList + 100
        """
        new_sl = self.sl + 100
        
        self.assertEquals(new_sl, ['hello', 'world', 100])
        
        self.assertEquals(self.sl, ['hello', 'world'])
            
    def test_cast_to_string(self):
        """
        str(StringList)
        """
        self.assertEquals(str(self.sl), "['hello', 'world']")
        
        
class TestSLAddition(unittest.TestCase):
    """
    Test various edge cases of adding two StringLists together
    """
    
    def setUp(self):
        from stringlist import StringList
        self.sl1 = StringList('hello', 'world')
        self.sl2 = StringList('hello world')
        self.sl3 = StringList('foo', 'bar', 'baz')
        self.sl4 = StringList('foo bar baz')
    
    def test_add_two_string_stringlists(self):
        """
        Add two string-based StringLists together
        """
        new_sl = self.sl2 + self.sl4
        
        self.assertEquals(new_sl, 'hello worldfoo bar baz')
        
        # make sure they didn't change
        self.assertEquals(self.sl2, 'hello world')
        self.assertEquals(self.sl4, 'foo bar baz')
        
    def test_add_two_list_stringlists(self):
        """
        Add two list-based StringLists together
        """
        new_sl = self.sl1 + self.sl3
        
        self.assertEquals(new_sl, ['hello', 'world', 'foo', 'bar', 'baz'])
        
        # make sure they didn't change
        self.assertEquals(self.sl1, ['hello', 'world'])
        self.assertEquals(self.sl3, ['foo', 'bar', 'baz'])
        
