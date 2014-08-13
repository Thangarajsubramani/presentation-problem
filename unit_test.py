import unittest
import present_schedule
from collections import OrderedDict, namedtuple
class TestPresentation(unittest.TestCase):
    
    def setUp(self):
        self.file = "input.csv"
        self.tschedule=3
    def test_main(self):      
        self.assertTrue(present_schedule.main_setup(self.tschedule,self.file))
        self.mydict=present_schedule.main_setup(self.tschedule,self.file)       
    
    def test_maxpresent_mincost(self):
        
        self.mydict=present_schedule.main_setup(self.tschedule,self.file)
        del self.mydict['presenter']
        del self.mydict['mincost_pres']
        tup = namedtuple('tup', ['Name','Hours','cost'])
        self.assertTrue(present_schedule.maxpresent_mincost(self.mydict,tup,self.tschedule))
    def test_mincost_present(self):
        self.mydict=present_schedule.main_setup(self.tschedule,self.file)
        del self.mydict['presenter']
        tup = namedtuple('tup', ['Name','Hours','cost'])
        self.assertTrue(present_schedule.mincost_present(self.mydict,tup,self.tschedule))
        #self.assertTrue(present_schedule.mincost_present(self.mydict,tup,self.tschedule))
        
        
if __name__ == '__main__':
    unittest.main()
