# import
# import sys
# sys.path.append(r'C:\Users\Renghe\Desktop\Course\block3\533\proj_step1\RecruitmentSystem')
# from sub_system.company import company
# from sub_character.admin import Admin
# from sub_character.jobseeker import JobSeeker

from .company import company
from ..sub_character.admin import Admin
from ..sub_character.jobseeker import JobSeeker

# module
class menu:

    def __init__(self) -> None:

        self.jobseekers = []  # Store the registered joobseeker object

        # companies. 2 comapnies buit-in
        self.Google = company(cname='Google',
                              jobs={'gjob1': [3, 'type 1', '2022-10-10'],
                                    'gjob2': [2, 'type 2', '2022-10-11'],
                                    'gjob3': [1, 'type 3', '2022-10-12'],
                                    'gjob4': [5, 'type 1', '2022-10-12']})
        self.Amazon = company(cname='Amazon',
                              jobs=
                              {'ajob1': [3, 'type 1', '2022-10-10'],
                               'ajob2': [2, 'type 2', '2022-10-11'],
                               'ajob3': [1, 'type 3', '2022-10-12'],
                               'ajob4': [5, 'type 1', '2022-10-12']})
        self.companys = [self.Google, self.Amazon]

        # Admin. 2 Admins buit-in
        self.admin_google = Admin('Admin1', '1', self.Google)
        self.admin_amazon = Admin('Admin2', '2', self.Amazon)
        # list of Admins
        self.admins = [self.admin_google, self.admin_amazon]

        # jobseekers. 5 job-seekers build-in
        j1 = JobSeeker('j1', '1', 1, 1)
        j2 = JobSeeker('j2', '2', 2, 2)
        j3 = JobSeeker('j3', '3', 3, 3)
        j4 = JobSeeker('j4', '4', 4, 4)
        j5 = JobSeeker('j5', '5', 5, 5)
        self.jobseekers = [j1, j2, j3, j4, j5]
        j1.apply(self.Amazon, job_name='ajob1')
        j2.apply(self.Amazon, job_name='ajob2')
        j3.apply(self.Amazon, job_name='ajob3')
        j4.apply(self.Amazon, job_name='ajob4')
        j5.apply(self.Google, job_name='gjob3')


    # Signup. Enter: Account Number (non-empty, no duplicates), Password (non-empty), Confirm Password, Years of Service (non-empty), Specialties (non-empty).
    def signup(self):

        account = input('Enter your Account Number: ')
        if not account:
            print('account cannot be empty, sign up fails')
            return
        password = input('Enter your Password')
        if not password:
            print('password cannot be empty, sign up fails')
            return
        password2 = input('Confirm your Password')
        job_experience = input('Enter your working years')
        if not job_experience:
            print('job_experience cannot be empty, sign up fails')
            return
        speciality = input('Enter your Specialties')
        if not speciality:
            print('specialities cannot be empty, sign up fails')
            return

            # The account already exists and failed to create.
        for i in self.jobseekers:
            if i.account == account:
                print(f'the account {account} has existed, registration fails')
                return

        # The password entered 2 times is not the same, creation failed.
        if password != password2:
            print(f'two pwds do not match, please re-enter pwd, registration fails')
            return

        j = JobSeeker(account, password, job_experience, speciality)
        self.jobseekers.append(j)

        print('Sign up Success!')

    # Login. Success returns True, failure returns False. jobseeker returns 1, admin returns 2.
    def login(self):

        while 1:
            index = input('Enter number 1 for job seeker login, number 2 for admin login, number 3 to exit: ')

            if index == '1':

                account = input('Enter your account: ')
                pwd = input('Enter your password: ')

                for jobseeker in self.jobseekers:
                    if jobseeker.account == account and jobseeker.password == pwd:
                        print('Login success!')
                        return (True, 1, jobseeker)

                print('Wrong account or password!')
                return (False, 1, None)

            elif index == '2':

                account = input('Enter admin account: ')
                pwd = input('Enter admin password: ')

                for admin in self.admins:
                    if admin.account == account and admin.password == pwd:
                        print('Login success!')
                        return (True, 2, admin)

                print('Wrong account or password!')
                return (False, 2, None)

            elif index == '3':
                return (False, None, None)

            else:
                print('No such serial number, plz re-enter.')

    def search_company(self):

        search_company_name = input('Enter the name of the company you want to view: ')
        for i in self.companys:
            if i.cname == search_company_name:
                the_company = i
                return the_company

        return False

    def start(self):

        while 1:
            print('\t\t\t    menu')
            print('\t\t\t 1. login \n \
                   \t 2. signup  \n \
                   \t 3. exit')

            index1 = input('Please enter the serial number: ')
            if index1 == '1':  # login
                index2 = self.login()

                if index2[0]:  # If the login is successful, then
                    index_account = index2[1]  # =1 jobseeker，=2 admin
                    if index_account == 1:  # jobseeker
                        the_jobseeker = index2[2]  # jobseeker obj
                    else:
                        admin = index2[2]  # admin obj

                    # Job Seekers Page
                    if index_account == 1:

                        # menu
                        print('\t\t\t    Welcome job seeker!')
                        print('\t\t\t 1. Search for companies and jobs')
                        print('\t\t\t 2. Apply ')
                        print('\t\t\t 3. Check status (Accepted/ Rejected/ Put into waitlist)')

                        while 1:
                            index1j = input('Enter 1 to search, 2 to apply, 3 to check status, 4 to exit: ')

                            if index1j == '1':
                                print('\nname of company: ')
                                for i in self.companys:
                                    print(i.cname)
                                print()

                                the_company = self.search_company()
                                if the_company == False:
                                    print('No such company.')
                                else:
                                    the_jobseeker.scan_jobs(the_company)

                                    while 1:  # search
                                        index1s = input(
                                            f'Enter 1 to search job in {the_company.cname} by name, 2 by type ,3 by date, 4 to exit: ')

                                        if index1s == '1':  # by name
                                            job_name = input('Enter job name: ')
                                            the_jobseeker.search_job_by_name(the_company, job_name)

                                        elif index1s == '2':  # by type
                                            job_type = input('Enter job type: ')
                                            the_jobseeker.search_job_by_type(the_company, job_type)

                                        elif index1s == '3':  # by date
                                            job_start_date = input('Enter start date: ')
                                            job_end_date = input('Enter end date: ')
                                            the_jobseeker.search_job_by_date(the_company, job_start_date, job_end_date)

                                        elif index1s == '4':  # exit
                                            print('exit search!')
                                            break
                                        
                                        else:
                                            print('no such serial number, plz re-enter!')



                            elif index1j == '2':  # Apply for company and job

                                print('\nname of company')
                                for i in self.companys:
                                    print(i.cname)
                                print()
                                applied_company_name = input(
                                    'Please enter the name of the company you want to apply for: ')

                                i = False
                                for c in self.companys:
                                    if c.cname == applied_company_name:
                                        the_company = c
                                        i = True

                                if not i:
                                    print(f'No such company {applied_company_name}! Application failed!')

                                else:
                                    the_jobseeker.scan_jobs(the_company)

                                    applied_job_name = input('Please enter the name of the job you want to apply for: ')
                                    if the_jobseeker.apply(the_company, applied_job_name):
                                        print('Application successful!')
                                    else:
                                        print('Application failed!')




                            elif index1j == '3':  # 3. check the status (whether accepted/ rejected/ put on waitlist)
                                the_jobseeker.check_notice()

                            elif index1j == '4':
                                print('logout!')
                                break

                            else:
                                print('No such serial number!')


                    elif index_account == 2:  # admin page

                        # meenu
                        print(f'\t\t\t    Welcome admin! You are managing {admin.privilege.cname}!')
                        print('\t\t\t 1. View all jobs')
                        print('\t\t\t 2. Add new job ')
                        print('\t\t\t 3. Modify job')
                        print('\t\t\t 4. delere job')
                        print('\t\t\t 5. View all applicant accounts')
                        print('\t\t\t 6. Process applicants (accept/ reject/ put on waitlist)')
                        print('\t\t\t 7. process waitlist')
                        print('\t\t\t 8. Rate')
                        print('\t\t\t 9. Applicant score ranking (from highest to lowest)')
                        print('\t\t\t 10. View acceptance list')
                        print('\t\t\t 11. exit')

                        while 1:
                            index1a = input('\nEnter operation number: ')

                            if index1a == '1':
                                admin.scan_job()

                            elif index1a == '2':
                                new_job_name = input('New job name: ')
                                new_remaining = int(input(f'input the remaining of job {new_job_name}: '))
                                new_type = input(f'input the type of job {new_job_name}: ')
                                new_date = input(f'input the date of job {new_job_name}: ')
                                admin.add_job(new_job_name, new_remaining, new_type, new_date)

                            elif index1a == '3':

                                while 1:
                                    index1a3 = input(
                                        'Enter 1 to modify job name, 2 to modify remaining, 3 to modify type, 4 to modify date, 5 to exit modify')

                                    if index1a3 == '1':  # modify job name
                                        old_job_name = input('Enter the name of the job you wish to modify: ')
                                        new_job_name = input(f'You want to change the name of job {old_job_name} to: ')
                                        admin.modify_job_name(old_job_name, new_job_name)

                                    elif index1a3 == '2':  # modify job remaining
                                        old_job_name = input('Enter the name of the job you wish to modify: ')
                                        new_remaining = int(input(f'You want to change the remaining of job {old_job_name} to: '))
                                        admin.modify_remaining(old_job_name, new_remaining)

                                    elif index1a3 == '3':  # modify job type
                                        old_job_name = input('Enter the name of the job you wish to modify: ')
                                        new_type = input(f'You want to change the type of job {old_job_name} to: ')
                                        admin.modify_type(old_job_name, new_type)

                                    elif index1a3 == '4':  # modify job date
                                        old_job_name = input('Enter the name of the job you wish to modify: ')
                                        new_date = input(f'You want to change the date of job {old_job_name} to: ')
                                        admin.modify_date(old_job_name, new_date)

                                    elif index1a3 == '10':  # exit modify
                                        print('exit modify!')
                                        break

                                    else:
                                        print('No serial number, please re-enter: ')


                            elif index1a == '4':
                                old_job_name = input('Enter the name of the job you want to delete: ')
                                admin.del_job(old_job_name)

                            # ---------------------------------------------------------------
                            elif index1a == '5':
                                admin.scan_application_list()

                            elif index1a == '6':
                                admin.choose_candidate()

                            elif index1a == '7':
                                admin.process_waitlist()

                            elif index1a == '8':
                                admin.marking()

                            elif index1a == '9':
                                admin.privilege.sort_by_mark()

                            elif index1a == '10':
                                admin.scan_accept_list()

                            elif index1a == '11':
                                print('admin log out')
                                break

                            else:
                                pass





            elif index1 == '2':  # signup
                self.signup()

            elif index1 == '3':
                print('exit system!')
                break

            else:
                print('No such serial number, plz re-enter.')



