nose-ittr
=========
nose expansion for supporting parametrized testing.
---------------------------------------------------
allow developer to run the same test over and over again using different values

Main Features:
- Very easy to integrate with existing tests.
- Saves a lot of boilerplate code, and code replication.
- Work with all nose plugins (including multiprocessing).


basic usage:
------------
        
.. code-block:: python

    from nose.tools import ok_
    from nose_ittr import IttrMultiplayer, ittr    
    
    class TestFoo(object):
        
        __metaclass__ = IttrMultiplayer
        
        def setup(self):
            pass
        
        def teardown(self):
            pass
            
        @ittr(number=[1, 2, 3, 4])
        def test_even(self):
            ok_(self.number % )
            
        
        @ittr(param_one=['case_one', 'case_two'], param_two=['case_three', 'case_four'])
        def test_bar(self):
            # do test
            print self.param_one, self.param_two
            

:Authors:
    Sergey Ragatsky 
    
:Contributors: 

    Tal Ben Basat
  
    Nicole Franco  

    Roy Klinger 
 
    Maroun Maroun  
    
:Version: 1.0 of 25/11/2014 
