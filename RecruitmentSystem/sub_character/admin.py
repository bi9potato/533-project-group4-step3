
from .user import user

# module
class Admin(user):

    def __init__(self, account, password,
                 privilege):
        super().__init__(account, password)
        self.__privilege = privilege  # company object. This administrator manages the corresponding company.

    # Attribute
    # privilege
    @property
    def privilege(self):
        return self.__privilege

    @privilege.setter
    def privilege(self, value):
        self.__privilege = value

    # Function
    # View all jobs.  Parameters: Company
    def scan_job(self):
        if self.privilege.jobs.items():
            print('\njob name\tremaining\t type\t\t date')
            for jname, context in self.privilege.jobs.items():
                print(jname, '\t\t', context[0], '\t\t', context[1], '\t', context[2])
            print()

    # Does the job name exist?  Parameters: Company, job name
    def job_exist(self, job_name):
        return True if job_name in self.privilege.jobs.keys() else False

    # Add job.  Parameters: Company, new job name, new job balance
    def add_job(self, new_job_name, new_remaining, new_type, new_date):
        if self.job_exist(new_job_name):
            print(f'job {new_job_name} already exists, insertion is prohibited.')
        elif new_remaining < 0:
            print('job ramining cannot < 0.')
        else:
            self.privilege.jobs[new_job_name] = [new_remaining, new_type, new_date]
            print(f'add job {new_job_name} success.')

    # Modify the job name.  Parameters: Company, old job name, new job name
    def modify_job_name(self, old_job_name, new_job_name):
        if self.job_exist(old_job_name):
            if self.job_exist(new_job_name):
                print(f'job {new_job_name} already exists, modification is prohibited.')
            else:
                self.privilege.jobs[new_job_name] = self.privilege.jobs.pop(old_job_name)
                print('Modified successfully!')
        else:
            print(f"job {old_job_name} doesn't exist, modification is prohibited.")

    # Modify the remaining amount of the job.  Parameters: Company, old job name, new job balance
    def modify_remaining(self, old_job_name, new_remaining):
        if self.job_exist(old_job_name):
            if new_remaining < 0:
                print('job ramining cannot < 0, modification is prohibited.')
            else:
                context = self.privilege.jobs[old_job_name]
                self.privilege.jobs[old_job_name] = [new_remaining, context[1], context[2]]
                print('Modified successfully!')
        else:
            print(f"job {old_job_name} doesn't exists, modification is prohibited.")

    # Modify the job type.
    def modify_type(self, old_job_name, new_type):
        if self.job_exist(old_job_name):
            context = self.privilege.jobs[old_job_name]
            self.privilege.jobs[old_job_name] = [context[0], new_type, context[2]]
            print('Modified successfully!')
        else:
            print(f"job {old_job_name} doesn't exists, modification is prohibited.")

    # Modify the job time.
    def modify_date(self, old_job_name, new_date):
        if self.job_exist(old_job_name):
            context = self.privilege.jobs[old_job_name]
            self.privilege.jobs[old_job_name] = [context[0], context[1], new_date]
            print('Modified successfully!')
        else:
            print(f"job {old_job_name} doesn't exists, modification is prohibited.")

    # Delete the job.  Parameters: Company, old job title
    def del_job(self, old_job_name):
        if self.job_exist(old_job_name):
            del self.privilege.jobs[old_job_name]
            print('Deleted successfully!')
        else:
            print(f"job {old_job_name} doesn't exists, deletion is prohibited.")

    # --------------------------------------------------------------------------------------------
    # Scan the account of candidates who applied.
    def scan_application_list(self):
        if len(self.privilege.application_list) != 0:  # If there are candidates then
            print("No.\taccount")
            for i in range(len(self.privilege.application_list)):
                print(i + 1, '\t', self.privilege.application_list[i].account)
        else:
            print('No applicants!')

    # Accept, reject, put job seekers in waitlist
    def choose_candidate(self):
        self.scan_application_list()

        if len(self.privilege.application_list) != 0:  # If there are candidates then
            while 1:
                index = int(input('Select the candidate serial number to view details: '))
                if index > self.privilege.get_len_ap() or index < 0:
                    print('No such serial number, please re-enter.')
                else:
                    the_candicate = self.privilege.get_candidate_details(index - 1)
                    break

            print('account\tWorking years\tspeciality\tjob applied for\tScore')
            print(the_candicate.account, '\t', the_candicate.job_experience, '\t', the_candicate.speciality, '\t',
                  the_candicate.applied_job, '\t\t', the_candicate.mark)

            while 1:
                index2 = input(
                    'Enter number 1 to reject him, number 2 to hire him, and number 3 to place him on the waitlist, number 4 to exit： ')
                if index2 == '1':
                    del self.privilege.application_list[index - 1]
                    the_candicate.status = 1
                    the_candicate.applied_job = None
                    print(f'reject candidate {the_candicate.account} ')
                    break
                elif index2 == '2':
                    self.privilege.accept_list.append(the_candicate)
                    del self.privilege.application_list[index - 1]
                    the_candicate.status = 2
                    the_candicate.applied_job = 'hired'
                    print(f'hire candidate {the_candicate.account} ')
                    break
                elif index2 == '3':
                    self.privilege.wait_list.append(the_candicate)
                    del self.privilege.application_list[index - 1]
                    the_candicate.status = 3
                    print(f'put candidate {the_candicate.account} into waitlist')
                    break
                elif index2 == '4':
                    print(f'Exit actions for candidate {the_candicate.account}')
                    break
                else:
                    print('No such serial number, please re-enter.')

    # scan accept list
    def scan_accept_list(self):

        if self.privilege.accept_list:
            print('account\tWorking years\tspeciality\tjob applied for\tScore')
            for i in self.privilege.accept_list:
                print(i.account, '\t', i.job_experience, '\t', i.speciality, '\t', i.applied_job, '\t\t', i.mark)
        else:
            print('Accept list is empty.')

    # process waitlist
    def process_waitlist(self):

        if not self.privilege.wait_list:
            print('No one in the waitlist')
            return

        print("No.\taccount")
        for i in range(len(self.privilege.wait_list)):
            print(i + 1, '\t', self.privilege.wait_list[i].account)

        while 1:
            index = int(input('Select the candidate serial number to view details: '))
            if index > len(self.privilege.wait_list) or index < 0:
                print('No such serial number, please re-enter.')
            else:
                the_candicate = self.privilege.wait_list[index - 1]
                break

        print('account\tWorking years\tspeciality\tjob applied for\tScore')
        print(the_candicate.account, '\t', the_candicate.job_experience, '\t', the_candicate.speciality, '\t',
              the_candicate.applied_job, '\t\t', the_candicate.mark)

        while 1:
            index2 = input('Enter number 1 to reject him, or number 2 to hire him, or number 3 exit')
            if index2 == '1':
                del self.privilege.wait_list[index - 1]
                the_candicate.status = 1
                the_candicate.applied_job = None
                print(f'reject candidate {the_candicate.account} ')
                break
            elif index2 == '2':
                self.privilege.accept_list.append(the_candicate)
                del self.privilege.wait_list[index - 1]
                the_candicate.status = 2
                the_candicate.applied_job = 'hired'
                print(f'hire candidate{the_candicate.account} ')
                break
            elif index2 == '3':
                print(f'Exit actions for candidate {the_candicate.account}')
                break
            else:
                print('No such serial number, please re-enter.')

    def marking(self):

        if not self.privilege.application_list:
            print('No one in the application list')
            return

        self.scan_application_list()
        while 1:
            index = int(input('Select the candidate serial number to view details: '))
            if index > self.privilege.get_len_ap() or index < 0:
                print('No such serial number, please re-enter.')
            else:
                the_candicate = self.privilege.get_candidate_details(index - 1)
                break

        print('account\tWorking years\tspeciality\tjob applied for\tScore')
        print(the_candicate.account, '\t', the_candicate.job_experience, '\t', the_candicate.speciality, '\t',
              the_candicate.applied_job, '\t\t', the_candicate.mark)

        while 1:
            index2 = input(f'Enter number 1 to rate {the_candicate.account}, 2 to exit: ')

            if index2 == '1':
                mark = int(input('Enter the mark: '))
                the_candicate.mark = mark
                print('Scoring success.')
                break
            elif index2 == '2':
                print('exit rating!')
                break
            else:
                print('No such serial number, please re-enter.')

