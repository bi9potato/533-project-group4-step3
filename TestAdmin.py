import unittest

from RecruitmentSystem.sub_character.admin import Admin
from RecruitmentSystem.sub_system.company import company

class TestAdmin(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
        
    def setUp(self):
        
        # init company
        self.c1 = company(cname = 'Google',
                     jobs = {'gjob1': [3, 'type 1', '2022-10-10'],
                             'gjob2': [2, 'type 2', '2022-10-11'],
                             'gjob3': [1, 'type 3', '2022-10-12'],
                             'gjob4': [5, 'type 1', '2022-10-12']})
        self.c2 = company(cname='Amazon',
                     jobs={'ajob1': [3, 'type 1', '2022-10-10'],
                           'ajob2': [2, 'type 2', '2022-10-11'],
                           'ajob3': [1, 'type 3', '2022-10-12'],
                           'ajob4': [5, 'type 1', '2022-10-12']})
        
        # init Admin
        self.a1 = Admin('a1', 1, self.c1)
        self.a2 = Admin('a2', 2, self.c2)
    
    def tearDown(self):
        pass
        
    def test_job_exist(self):
        
        self.assertEqual(self.a1.job_exist('gjob1'), True)
        self.assertEqual(self.a1.job_exist('g'), False)
        self.assertEqual(self.a2.job_exist('ajob2'), True)
        self.assertEqual(self.a2.job_exist('ajob8'), False)
    
    
    def test_modify_job_name(self):
        
        self.a1.modify_job_name('gjob1', 'gjob11')
        self.assertEqual(self.a1.job_exist('gjob11'), True)
        self.assertEqual(self.a1.job_exist('gjob1'), False)
        
        self.a2.modify_job_name('ajob2', 'ajob3')
        self.assertEqual(self.a2.job_exist('ajob2'), True)
        self.assertEqual(self.a2.job_exist('ajob3'), True)
    
    
        
unittest.main(argv=[''], verbosity=2, exit=False)