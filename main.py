from indeed import get_jobs as get_indeed_jobs
from stack import get_jobs as get_stack_jobs
from save import save_file

indeed_jobs = get_indeed_jobs()
stack_jobs = get_stack_jobs()

jobs = stack_jobs + indeed_jobs

save_file(jobs)

#print(indeed_jobs)
#print(stack_jobs)



