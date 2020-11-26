from indeed import indeed_job_extract
from stackoverflow import stackoverflow_job_extract
from save import save_to_file

indeed_jobs = indeed_job_extract()
stackoverflow_jobs = stackoverflow_job_extract()

total_jobs = indeed_jobs + stackoverflow_jobs

save_to_file(total_jobs)
