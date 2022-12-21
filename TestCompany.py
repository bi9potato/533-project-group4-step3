import unittest
from RecruitmentSystem.sub_system.company import company
from RecruitmentSystem.sub_character.jobseeker import JobSeeker

class TestCompany(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self):
        self.j1 = JobSeeker('j1', 1, 1, 'python')
        self.j2 = JobSeeker('j2', 2, 0, 'R')
        self.j3 = JobSeeker('j3', 3, 3, 'SQL')
        self.j4 = JobSeeker('j4', 4, 4, 'stats')
        
        self.c1 = company(cname = 'Google',
                     jobs = {'gjob1': [3, 'type 1', '2022-10-10'],
                             'gjob2': [2, 'type 2', '2022-10-11'],
                             'gjob3': [1, 'type 3', '2022-10-12'],
                             'gjob4': [5, 'type 1', '2022-10-12']})
        
        
        self.j1.apply(self.c1, 'gjob1')
        self.j2.apply(self.c1, 'gjob3')
        self.j3.apply(self.c1, 'gjob2')
        self.j4.apply(self.c1, 'gjob1')
    
       
        
        
        
    def tearDown(self):
        print('Tear Down')
    
    def test_get_candidate_details(self):
        
        
        l = self.c1.application_list
        self.assertEqual((l[0].account, l[0].password, l[0].job_experience, l[0].speciality), ('j1', 1, 1, 'python'))
        self.assertEqual((l[1].account, l[1].password, l[1].job_experience, l[1].speciality), ('j2', 2, 0, 'R'))
        self.assertEqual((l[2].account, l[2].password, l[2].job_experience, l[2].speciality), ('j3', 3, 3, 'SQL'))
        self.assertEqual((l[2].account, l[3].password, l[3].job_experience, l[3].speciality), ('j3', 4, 4, 'stats'))
    
    def test_get_len_ap(self):
        
        self.assertIsInstance(self.c1.get_len_ap(), int)
        self.assertEqual(self.c1.get_len_ap(), 4)
        
        self.c1.application_list.pop(0)
        
        self.assertNotEqual(self.c1.get_len_ap(), 4)
        self.assertEqual(self.c1.get_len_ap(), 3)
        
        
unittest.main(argv=[''], verbosity=2, exit=False)
