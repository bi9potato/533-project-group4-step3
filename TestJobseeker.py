import unittest

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
                     jobs = {'gjob1': [3, 'type 1', '2022-10-10'],
                             'gjob2': [2, 'type 2', '2022-10-11'],
                             'gjob3': [1, 'type 3', '2022-10-12'],
                             'gjob4': [5, 'type 1', '2022-10-12']})
        self.c2 = company(cname='Amazon',
                     jobs={'ajob1': [3, 'type 1', '2022-10-10'],
                           'ajob2': [2, 'type 2', '2022-10-11'],
                           'ajob3': [1, 'type 3', '2022-10-12'],
                           'ajob4': [5, 'type 1', '2022-10-12']})
        
        # init JobSeeker
        self.j1 = JobSeeker('j1', 1, 1, 'sing')
        self.j2 = JobSeeker('j2', 2, 0, 'dance')
        self.j3 = JobSeeker('j3', 3, 3, 'rap')
        self.j4 = JobSeeker('j4', 4, 4, 'basketball')
    
    def tearDown(self):
        pass
    
    def test_apply(self):
        
        self.j1.apply(self.c1, 'gjob1')
        self.j2.apply(self.c1, 'gjob3')
        self.j3.apply(self.c1, 'gjob3')
        self.j2.apply(self.c2, 'gjob1')
        
        self.assertEqual(self.j1 in self.c1.application_list, True)
        self.assertEqual(self.j2 in self.c1.application_list, True)
        self.assertEqual(self.j3 in self.c1.application_list, False)
        self.assertEqual(self.j4 in self.c2.application_list, False)
    
    def test_search_job_by_name(self):
        
        self.assertEqual(self.j1.search_job_by_name(self.c1, 'gjob1'), True)
        self.assertEqual(self.j2.search_job_by_name(self.c1, 'gjob2'), True)
        self.assertEqual(self.j3.search_job_by_name(self.c1, 'gjob8'), False)
        self.assertEqual(self.j4.search_job_by_name(self.c2, 'gjob1'), False)

    
# unittest.main(argv=[''], verbosity=2, exit=False)