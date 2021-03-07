import job_scraper
from job_scraper import find_jobs_from

desired_characs = ['titles', 'companies', 'links', 'date_listed', 'salary']

find_jobs_from('Indeed', 'java', 'london', desired_characs)