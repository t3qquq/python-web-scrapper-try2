import csv

def save_to_file(jobs):
    file = open('jobs.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'location'])
    
    for num in range(len(jobs)):
        writer.writerow([jobs[num]['title'], jobs[num]['company'], jobs[num]['location']])