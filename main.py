from indeed import indeed_job_extract
from stackoverflow import stackoverflow_job_extract

indeed_jobs = indeed_job_extract()
stackoverflow_jobs = stackoverflow_job_extract()

total_jobs = indeed_jobs + stackoverflow_jobs

for num in range(len(total_jobs)):
    print(total_jobs[num])