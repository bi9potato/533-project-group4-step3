import unittest

import sys
sys.path.insert(0, sys.path[0][:-5])

from RecruitmentSystem.sub_system.menu import menu
from unittest.mock import patch


class TestMenu(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
        
    def setUp(self):
        self.m=menu()
        
    def tearDown(self):
        pass
    
    @patch("builtins.input")
    def test_signup(self, mock_input):
        
        mock_input.sied_effect = []
        self.assertEqual(self.m.signup(), None)
        
        mock_input.sied_effect = ['a1', False]
        self.assertEqual(self.m.signup(), None)
        
        mock_input.sied_effect = ['a1', '1', '1', False]
        self.assertEqual(self.m.signup(), None)
        
        mock_input.sied_effect = ['a1', '1', '1', '1', False]
        self.assertEqual(self.m.signup(), None)
        
        mock_input.sied_effect = ['a1', '1', '1', '1', '1']
        self.assertEqual(self.m.signup(), None)
        
        mock_input.sied_effect = ['a11', '1', '2', '1', '1']
        self.assertEqual(self.m.signup(), None)
        
        mock_input.sied_effect = ['a11', '1', '1', '1', '1']
        self.assertEqual(self.m.signup(), None)
        
        
    
    @patch("builtins.input")
    def test_login(self,mock_input):
        
        j1 = self.m.jobseekers[0]
        mock_input.side_effect=['5', '1','j1','1']
        self.assertEqual(self.m.login(), (True, 1, j1))
        
        mock_input.side_effect=['1','j1','2']
        self.assertEqual(self.m.login(),(False, 1, None))
        
        Admin = self.m.admins[0]
        mock_input.side_effect=['2','Admin1','1']
        self.assertEqual(self.m.login(),(True, 2, Admin))
        
        mock_input.side_effect = ['3']
        self.assertEqual(self.m.login(), (False, None, None))
        
        mock_input.side_effect = ['2', 'a12', '12']
        self.assertEqual(self.m.login(), (False, 2, None))

        
    @patch("builtins.input")    
    def test_search_company(self,mock_input):
        
        mock_input.return_value='Amazon'
        self.assertEqual(self.m.search_company(),self.m.companys[1])
        
        mock_input.return_value='Google'
        self.assertEqual(self.m.search_company(),self.m.companys[0])
        
        mock_input.return_value='Facebook'
        self.assertFalse(self.m.search_company(), False)
        
        mock_input.return_value='Microsoft'
        self.assertFalse(self.m.search_company(), False)
    

    @patch("builtins.input")
    @patch("RecruitmentSystem.sub_system.menu.menu.login")
    @patch("RecruitmentSystem.sub_system.menu.menu.search_company")
    def test_start(self, mock_company, mock_login, mock_input): # order！！！！！！！！
        
        # jobseeker
        mock_input.side_effect = ["1", '1', '1', 'gjob1', '4', '4', '3']
        mock_login.side_effect = [(True, 1, self.m.jobseekers[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '1', '2', 'type 1', '4', '4', '3']
        mock_login.side_effect = [(True, 1, self.m.jobseekers[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '1', '5', '3', '2022-10-10', '2022-10-10', '4', '4', '3']
        mock_login.side_effect = [(True, 1, self.m.jobseekers[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '2', 'Google', 'gjob1', '4', '3']
        mock_login.side_effect = [(True, 1, self.m.jobseekers[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '2', 'Goo',  '4', '4', '3']
        mock_login.side_effect = [(True, 1, self.m.jobseekers[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '3',  '4', '3']
        mock_login.side_effect = [(True, 1, self.m.jobseekers[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        # admin
        mock_input.side_effect = ["1", '1', '11', '3']
        mock_login.side_effect = [(True, 2, self.m.admins[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '2', 'gjob11', '1', '1', '2022-1-1', '11', '3']
        mock_login.side_effect = [(True, 2, self.m.admins[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '3', 
                                  '1', 'gjob1', 'gjob111', 
                                  '2', 'gjob1', 12,
                                  '3', 'gjob1', 'type 2',
                                  '4', 'gjob1', '2022-10-12',
                                  '10', '11', '3']
        mock_login.side_effect = [(True, 2, self.m.admins[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '4', 'gjob1', '11', '3']
        mock_login.side_effect = [(True, 2, self.m.admins[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '5', '11', '3']
        mock_login.side_effect = [(True, 2, self.m.admins[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        mock_input.side_effect = ["1", '7', '9', '10', '11', '3']
        mock_login.side_effect = [(True, 2, self.m.admins[0])]
        mock_company.side_effect = [self.m.Google]
        self.assertFalse(self.m.start(), None)
        
        
        
        
        
        
unittest.main(argv=[''], verbosity=2, exit=False)
        
        
        
    