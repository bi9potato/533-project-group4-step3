import unittest

import sys
sys.path.insert(0, sys.path[0][:-5])

from RecruitmentSystem.sub_character.jobseeker import JobSeeker
from RecruitmentSystem.sub_system.company import company

class TestJobseeker(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        
        # init company
        self.c1 = company(cname = 'Google',
                     jobs = {'gjob1': [30, 'type 1', '2022-10-10'],
                             'gjob2': [20, 'type 2', '2022-10-11'],
                             'gjob3': [10, 'type 3', '2022-10-12'],
                             'gjob4': [50, 'type 1', '2022-10-12']})
        
        self.c2 = company(cname='Amazon',
                     jobs={'ajob1': [30, 'type 1', '2022-10-10'],
                           'ajob2': [20, 'type 2', '2022-10-11'],
                           'ajob3': [10, 'type 3', '2022-10-12'],
                           'ajob4': [50, 'type 1', '2022-10-12']})
        
        self.c3 = company(cname='Facebook',
                     jobs={'fjob1': [0, 'type 1', '2022-10-10'],
                           'fjob2': [5, 'type 2', '2022-10-11'],
                           'fjob3': [5, 'type 3', '2022-10-12'],
                           'fjob4': [0, 'type 1', '2022-10-12']})
        
        # init JobSeeker
        self.j1 = JobSeeker('j1', 1, 1, 'sing')
        self.j2 = JobSeeker('j2', 2, 0, 'dance')
        self.j3 = JobSeeker('j3', 3, 3, 'rap')
        self.j4 = JobSeeker('j4', 4, 4, 'basketball')
        self.j5 = JobSeeker('j5', 5, 5, 'badminton')
    
    def tearDown(self):
        pass
    
    def test_apply(self):
        
        self.j1.apply(self.c1, 'gjob1')
        self.j2.apply(self.c1, 'gjob3')
        self.j3.apply(self.c1, 'gjob3')
        self.j3.apply(self.c1, 'gjob3') # repeat
        self.j2.apply(self.c2, 'gjob1')
        self.j5.apply(self.c3, 'fjob1')
        
        self.assertEqual(self.j1 in self.c1.application_list, True)
        self.assertEqual(self.j2 in self.c1.application_list, True)
        self.assertEqual(self.j3 in self.c1.application_list, True)
        self.assertEqual(self.j4 in self.c2.application_list, False)
        self.assertEqual(self.j5 in self.c3.application_list, False)
    
    def test_check_notice(self): 
        self.j1.status = None
        self.j1.check_notice()
        self.assertEqual( self.j1.status, None)
        
        self.j1.status = 1
        self.j1.check_notice()
        self.assertEqual( self.j1.status, 1)
        
        self.j1.status = 2
        self.j1.check_notice()
        self.assertEqual( self.j1.status, 2)
        
        self.j1.status = 3
        self.j1.check_notice()
        self.assertEqual( self.j1.status, 3)
        
        self.j1.status = 4
        self.j1.check_notice()
        self.assertNotEqual( self.j1.status, 3)
    
    def test_scan_jobs(self):
        
        self.assertEqual(self.j1.scan_jobs(self.c1), None)
    
    def test_search_job_by_name(self):
        
        self.assertEqual(self.j1.search_job_by_name(self.c1, 'gjob1'), True)
        self.assertEqual(self.j2.search_job_by_name(self.c1, 'gjob2'), True)
        self.assertEqual(self.j3.search_job_by_name(self.c1, 'gjob8'), False)
        self.assertEqual(self.j4.search_job_by_name(self.c2, 'gjob1'), False)
    
    def test_search_job_by_type(self):
        self.assertEqual(self.j1.search_job_by_type(self.c1, 'type 1'), None)
        self.assertEqual(self.j1.search_job_by_type(self.c1, 'type 11'), None)
    
    def test_search_job_by_date(self):
        self.assertEqual(self.j1.search_job_by_date(self.c1, '2022-10-9', '2022-10-12'), None)
        self.assertEqual(self.j1.search_job_by_date(self.c1, '2021-10-9', '2021-10-12'), None)
    
    def test_init(self):
        self.assertIsInstance(JobSeeker('j10', 1, 1, 'lol'), JobSeeker)

    
unittest.main(argv=[''], verbosity=2, exit=False)