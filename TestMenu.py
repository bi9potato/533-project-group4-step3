import unittest
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
    
    
    # @patch("RecruitmentSystem.sub_system.menu.menu.login")
    @patch("builtins.input")
    def test_login(self,mock_input):
        
        j1 = self.m.jobseekers[0]
        mock_input.side_effect=['1','j1','1']
        self.assertEqual(self.m.login(), (True, 1, j1))
        
        mock_input.side_effect=['1','j1','2']
        self.assertEqual(self.m.login(),(False, 1, None))
        
        Admin = self.m.admins[0]
        mock_input.side_effect=['2','Admin1','1']
        self.assertEqual(self.m.login(),(True, 2, Admin))
        
        mock_input.side_effect = ['3']
        self.assertEqual(self.m.login(), (False, None, None))
        
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
        
unittest.main(argv=[''], verbosity=2, exit=False)
        
        
        
    