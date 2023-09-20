from inspect import currentframe
import json
from bs4 import BeautifulSoup 
import datetime

def find_latest_date(dates: list[datetime.date], target: datetime.date) -> int:
    l, r = 0, len(dates) - 1

    if target <= dates[0]:
        return 0

    elif target > dates[-1]:
        return -1

    while l <= r:
        m = (l + r) // 2

        if dates[m-1] <= target <= dates[m]:
            return m

        elif target > dates[m]:
            l = m + 1

        elif target < dates[m-1]:
            r = m - 1

with open('./course-data.js') as f:
    # assignments = json.load(f)['assignments']
    assignments = json.load(f)
    test = json.dumps(assignments, indent=4)
    print(test)
    assignments = [ass for ass in assignments if ass['title'].startswith('Homework')]
    assignments = sorted(assignments, key=lambda x: x['dueAt'])

    due_dates = [(lambda x: datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S%z').date())(x) for x in [ass['dueAt'] for ass in assignments]]
    cur_date = datetime.datetime.today().date()

    latest_assignment = assignments[find_latest_date(due_dates, cur_date)]
    soup = BeautifulSoup(latest_assignment['content'], features='html.parser')
    p = soup.find('p').text
    p = p[3:-4]
    print(f'{latest_assignment["title"]}')
    print(p)
