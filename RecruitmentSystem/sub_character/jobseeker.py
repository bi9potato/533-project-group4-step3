

from .user import user

# module
class JobSeeker(user):

    def __init__(self, account, password,
                 job_experience,
                 speciality,
                 ):
        super().__init__(account, password)
        self.__job_experience = job_experience
        self.__speciality = speciality
        self.__status = None
        self.__mark = None
        self.__applied_job = None

        # attribute

    # job_experience
    @property
    def job_experience(self):
        return self.__job_experience

    @job_experience.setter
    def job_experience(self, value):
        self.__job_experience = value

    # speciality
    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, value):
        self.__speciality = value

    # status
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    # mark
    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, value):
        self.__mark = value

    # applied_job
    @property
    def applied_job(self):
        return self.__applied_job

    @applied_job.setter
    def applied_job(self, value):
        self.__applied_job = value

    # Function
    def apply(self, company, job_name):
        if job_name not in company.jobs.keys():
            print(f"there doesn't exist job {job_name}")
            return False
        elif company.jobs[job_name][0] <= 0:
            print(f"no enough job {job_name}")
            return False
        elif self.applied_job != None:
            print(f'you have applied job {self.applied_job}, cannot apply more job')
            return False
        else:
            company.application_list.append(self)
            company.jobs[job_name][0] = company.jobs[job_name][0] - 1
            self.applied_job = job_name
            return True

    def check_notice(self):
        if self.status == None:
            print('Unprocessed')
        elif self.status == 1:
            print('Rejected')
        elif self.status == 2:
            print('Hired')
        elif self.status == 3:
            print('Placed in the waitlist')
        else:
            pass

    # Output all jobs of a company
    def scan_jobs(self, company):
        print('\njob name\tremaining\t type\t\t date')
        for jname, context in company.jobs.items():
            print(jname, '\t\t', context[0], '\t\t', context[1], '\t', context[2])
        print()

    # Find Jobs
    # by name
    def search_job_by_name(self, company, job_name):
        if job_name in company.jobs:
            print('\njob name\tremaining\t type\t\t date')
            print(job_name, '\t\t', company.jobs[job_name][0], '\t\t', company.jobs[job_name][1], '\t',
                  company.jobs[job_name][2])
            return True
        else:
            print('The job was not found')
            return False

    # by type
    def search_job_by_type(self, company, job_type):

        i = False
        for job_name, context in company.jobs.items():
            if job_type == context[1]:
                i = True
        if i == True:
            print('\njob name\tremaining\t type\t\t date')

        i = False
        for jname, context in company.jobs.items():
            if job_type == context[1]:
                i = True
                print(jname, '\t\t', context[0], '\t\t', context[1], '\t', context[2])

        if i:
            return
        else:
            print('The job was not found')

    # by date. find jobs whose date beetween [start_job_date, end_job_date]
    def search_job_by_date(self, company, start_job_date, end_job_date):

        i_syear = start_job_date[:4]
        i_smonth = start_job_date[5:7]
        i_sday = start_job_date[-2:]

        i_eyear = end_job_date[:4]
        i_emonth = end_job_date[5:7]
        i_eday = end_job_date[-2:]

        i = False
        for jname, context in company.jobs.items():

            year = context[2][:4]
            month = context[2][5:7]
            day = context[2][-2:]

            if (year > i_syear and year < i_eyear):
                i = True
            elif year == i_syear:
                if (month > i_smonth):
                    i = True
                elif month == i_smonth:
                    if (day >= i_sday):
                        i = True
                    else:
                        pass
                else:
                    pass
            elif year == i_eyear:
                if (month < i_emonth):
                    i = True
                elif month == i_emonth:
                    if (day <= i_sday):
                        i = True
                    else:
                        pass
                else:
                    pass
            else:
                pass

        if i:
            print('\njob name\tremaining\t type\t\t date')

        i = False
        for jname, context in company.jobs.items():

            year = context[2][:4]
            month = context[2][5:7]
            day = context[2][-2:]

            if (year > i_syear and year < i_eyear):
                print(jname, '\t\t', context[0], '\t\t', context[1], '\t', context[2])
                i = True
            elif year == i_syear:
                if (month > i_smonth):
                    print(jname, '\t\t', context[0], '\t\t', context[1], '\t', context[2])
                    i = True
                elif month == i_smonth:
                    if (day >= i_sday):
                        print(jname, '\t\t', context[0], '\t\t', context[1], '\t', context[2])
                        i = True
                    else:
                        pass
                else:
                    pass
            elif year == i_eyear:
                if (month < i_emonth):
                    print(jname, '\t\t', context[0], '\t\t', context[1], '\t', context[2])
                    i = True
                elif month == i_emonth:
                    if (day <= i_sday):
                        print(jname, '\t\t', context[0], '\t\t', context[1], '\t', context[2])
                        i = True
                    else:
                        pass
                else:
                    pass
            else:
                pass

        if i:
            return
        else:
            print('The job was not found')




