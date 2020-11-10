from indeed import indeed_job_extract

indeed_jobs = indeed_job_extract()
for num in range(len(indeed_jobs)):
    print(indeed_jobs[num])