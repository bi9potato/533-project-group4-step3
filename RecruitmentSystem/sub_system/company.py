class company():

    def __init__(self, cname, jobs) -> None:
        self.__cname = cname
        self.__jobs = jobs
        self.__application_list = []
        self.__accept_list = []
        self.__wait_list = []

        # Attribute

    # cname
    @property
    def cname(self):
        return self.__cname

    @cname.setter
    def cname(self, value):
        self.__cname = value

    # jobs
    @property
    def jobs(self):
        return self.__jobs

    @jobs.setter
    def jobs(self, value):
        self.__jobs = value

    # application_list
    @property
    def application_list(self):
        return self.__application_list

    @application_list.setter
    def aplication_list(self, value):
        self.__application_list = value

    # accept_list
    @property
    def accept_list(self):
        return self.__accept_list

    @accept_list.setter
    def aplication_list(self, value):
        self.__accept_list = value

    # wait_list
    @property
    def wait_list(self):
        return self.__wait_list

    @wait_list.setter
    def wait_list(self, value):
        self.__wait_list = value

    # Function
    # Find individual applicants by number (order of application)
    def get_candidate_details(self, index):
        return self.application_list[index]

    # Return application_list length
    def get_len_ap(self):
        return len(self.application_list)

    # Sort all candidates who were scored and were not hired or rejected.
    def sort_by_mark(self):

        marked_candidates = []
        for i in self.application_list:
            if i.mark != None:
                marked_candidates.append(i)

        for i in self.wait_list:
            if i not in marked_candidates and i.mark != None:
                marked_candidates.append(i)

        if not marked_candidates:
            print('No one was rated!')
        else:
            sorted_list = sorted(marked_candidates, key=lambda x: x.mark, reverse=True)

            print('account\tWorking years\tspeciality\tjob applied for\tScore')
            for the_candicate in sorted_list:
                print(the_candicate.account, '\t', the_candicate.job_experience, '\t', the_candicate.speciality, '\t',
                      the_candicate.applied_job, '\t\t', the_candicate.mark)
