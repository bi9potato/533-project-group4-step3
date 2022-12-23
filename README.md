# 533-project-group4

[![Build Status](https://app.travis-ci.com/bi9potato/533-project-group4-step3.svg?branch=main)](https://app.travis-ci.com/bi9potato/533-project-group4-step3)

The package link: https://pypi.org/project/RecruitmentSystem/
This package is a **recruitment system** where allows admins from companies to manage jobs and candidates and job-seekers to search and apply jobs.
## sub-package1 : system
### module1 : menu
* init : 2 companies, 2 admins and 5 jobseekers has been bulit in for testing
* signup : users input accountnumber and password to creat a account as long as other details like year of experience and specialty
* login : users input accountnumber and password which have to be matched with each other
* search_company : check the inputing company exists or not
* **start** : go to signup or login first, then for admins or jobseekers, we can here invoke all functions in their own modules
### module2 : company
* get_candidate_details : show all details of the applicants
* get_len_ap : show the total number of applicants
* sort_by_mark : Sort all candidates who were scored yet were not hired or rejected
## sub-package2 : character
### module1 : user
* init : Users'account and password (**Heritance** : The class user would be the parent class of the class admin and the class jobseeker.)
### module2 : admin
* scan_job : admins can check the list of jobs with all details such as name, remaining positions, type and releasing date
* job_exist ：check the input job name exists or not
* add_job : if the job doesn't exist, add the job name adn all details to the list
* modify_job_name : if the job exist, change the job name
* modify_remaining : if the job exist, change the remaining number
* modify_type : if the job exist, change the job type
* modify_date : if the job exist, change the date
* del_job : if the job exist, delete the name
* scan_application_list : admins can check the list of applicants(show their accounts)
* choose_candidate : show all details of applicants such as experience of year and specialty and choose to add those applicants to accept_list or wait_list or delete from applicant_list and change their status
* scan_accept_list : show all details of applicants that have been accepted
* process_waitlist : show all details of applicants that are in waitlist and choose to add those applicants to accept_list or delete them and change their status
* marking : show all details of applicants and mark them
### module3: jobseeker
* apply : jobseeker can input company and jobname to look for exising job and then add themselves to applicant_list
* check_notice : jobseeker can check their status which are set by admins
* scan_jobs : show all details of existing job in inputing company
* search_job_by_name : show all details of existing job in inputing company and jobname
* search_job_by_type : show all details of existing job in inputing company and type
* search_job_by_date : show all details of existing job in inputing company and date


