import unittest

import sys
sys.path.insert(0, sys.path[0][:-4])


from RecruitmentSystem.sub_character.admin import Admin
from RecruitmentSystem.sub_system.company import company
from RecruitmentSystem.sub_character.jobseeker import JobSeeker



from unittest.mock import patch


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
                     jobs={'fjob1': [5, 'type 1', '2022-10-10'],
                           'fjob2': [5, 'type 2', '2022-10-11'],
                           'fjob3': [5, 'type 3', '2022-10-12'],
                           'fjob4': [5, 'type 1', '2022-10-12']})
        
        # init Admin
        self.a1 = Admin('a1', 1, self.c1)
        self.a2 = Admin('a2', 2, self.c2)
        self.a3 = Admin('a3', 3, self.c3)
        
        # init jobseekers
        self.j11 = JobSeeker('j11', 1, 1, 'python')
        self.j22 = JobSeeker('j22', 2, 0, 'R')
        self.j33 = JobSeeker('j33', 3, 3, 'SQL')
        self.j44 = JobSeeker('j44', 4, 4, 'stats')
        
        self.j11.apply(self.c1, 'gjob1')
        self.j22.apply(self.c1, 'gjob2')
        self.j33.apply(self.c1, 'gjob3')
        self.j44.apply(self.c2, 'ajob1')
    
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
        
        self.a2.modify_job_name('ajob20', 'ajob3')
    
    def test_scan_job(self):
        self.assertEqual(self.a1.scan_job(), None)
    
    def test_add_job(self):
        
        self.a1.add_job('gjob11', 10, 'type 1', '2022-12-10')
        self.a1.add_job('gjob1', 10, 'type 1', '2022-12-10')
        self.a1.add_job('gjob12', -1, 'type 1', '2022-12-10')
        self.assertIn('gjob11', self.c1.jobs)

    def test_modify_remaining(self):
        
        self.a1.modify_remaining('gjob1', -1)
        self.a1.modify_remaining('gjob101', 1)
        self.a1.modify_remaining('gjob1', 100)
        self.assertEqual(100, self.c1.jobs['gjob1'][0])
    
    def test_modify_type(self):
        
        self.a1.modify_type('gjob101', 'type 22')
        self.a1.modify_type('gjob1', 'type 11')
        self.assertEqual('type 11', self.c1.jobs['gjob1'][1])
        
    def test_modify_date(self):
        
        self.a1.modify_date('gjob101', '2010-10-10')
        self.a1.modify_date('gjob1', '2010-10-10')
        self.assertEqual('2010-10-10', self.c1.jobs['gjob1'][2])
    
    def test_del_job(self): 
        
        self.a1.del_job('gjob101')
        self.a1.del_job('gjob1')
        self.assertNotIn('gjob1', self.c1.jobs)
    
    def test_scan_application_list(self):
        
        self.assertEqual(self.a1.scan_application_list(), None)
    
    
    @patch("builtins.input")
    def test_choose_candidate(self, mock_input):
        
        # mock_input.side_effect=[1, 1] 
        self.assertEqual(self.a3.choose_candidate(), None) # no candidates
        
        mock_input.side_effect=[10, '1', '1'] 
        self.assertEqual(self.a1.choose_candidate(), None) # wrong number1 then rj
        
        # mock_input.side_effect=[1, '1']  # reject
        # self.assertEqual(self.a1.choose_candidate() , None)
        
        mock_input.side_effect=[1, '2']  # ac
        self.assertEqual(self.a1.choose_candidate() , None)
        
        mock_input.side_effect=[1, '3']  # wl
        self.assertEqual(self.a1.choose_candidate() , None)
        
        mock_input.side_effect=[1, '4']  # exit
        self.assertEqual(self.a1.choose_candidate() , None)
        
        mock_input.side_effect=[1, '5', '1']  # wrong number2 then reject
        self.assertEqual(self.a2.choose_candidate() , None)
    
    @patch("builtins.input")
    def test_scan_accept_list(self, mock_input):
        mock_input.side_effect=[1, '2']  # ac
        self.a1.choose_candidate()
        self.assertEqual(self.a1.scan_accept_list() , None)
        
        self.assertEqual(self.a3.scan_accept_list() , None)
    
    @patch("builtins.input")
    def test_process_waitlist(self, mock_input):
        pass
    
    @patch("builtins.input")
    def test_marking(self , mock_input): 
        
        self.a3.marking() # no candidates
        
        mock_input.side_effect=[-1, 1, '1', 90]  # wrong number1
        self.assertEqual(self.a1.marking() , None)
        
        mock_input.side_effect=[1, '2']  # exit
        self.assertEqual(self.a1.marking(), None)
    
    
        
         
    
        
unittest.main(argv=[''], verbosity=2, exit=False)