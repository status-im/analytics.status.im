#!/usr/bin/env python

# > python -i ./retention.py ~/git/status-react/ 2017-01-01 2018-01-01
#
# > ./retention.py ~/git/status-react/ 2017-01-01 2018-01-01
# Retention statistics for /Users/oskarth/git/status-react/
# From 2017-01-01 to 2018-01-01
# [19, 5, 6, 6, 4, 3, 4, 4, 3, 3, 3, 3]
# ['100%', '26%', '31%', '31%', '21%', '15%', '21%', '21%', '15%', '15%', '15%', '15%']
#
# First number is number of contributors in first month (i.e. january 2017, july 2017 or september 2017), then number of contributors active in month N from cohort "active in month 1". Second line is same but expressed as %

# First commit
# > (cd ~/git/node && git log -1 --format=%ci $(git rev-list --max-parents=0 HEAD))
# Year 1 activity not bad idea
# After being around for 1y how do, 2y?


# Roughly second year retention rate statistics
#
# Retention statistics for /Users/oskarth/git/status-react/
# From 2017-01-01 to 2018-01-01
# [19, 5, 6, 6, 4, 3, 4, 4, 3, 3, 3, 3]
# ['100%', '26%', '31%', '31%', '21%', '15%', '21%', '21%', '15%', '15%', '15%', '15%']
#
# Retention statistics for /Users/oskarth/git/node/
# From 2010-01-01 to 2011-01-01
# [18, 8, 7, 9, 8, 4, 3, 8, 5, 6, 3, 4]
# ['100%', '44%', '38%', '50%', '44%', '22%', '16%', '44%', '27%', '33%', '16%', '22%']
#
# > ./retention.py ~/git/tensorflow/ 2017-01-01 2018-01-01
# Retention statistics for /Users/oskarth/git/tensorflow/
# From 2017-01-01 to 2018-01-01
# [128, 70, 63, 53, 57, 55, 47, 48, 51, 49, 44, 50]
# ['100%', '54%', '49%', '41%', '44%', '42%', '36%', '37%', '39%', '38%', '34%', '39%']
#
# > ./retention.py ~/git/kubernetes/ 2015-01-01 2016-01-01
# Retention statistics for /Users/oskarth/git/kubernetes/
# From 2015-01-01 to 2016-01-01
# [80, 51, 42, 42, 40, 41, 38, 34, 36, 29, 31, 29]
# ['100%', '63%', '52%', '52%', '50%', '51%', '47%', '42%', '45%', '36%', '38%', '36%']

from dateutil import rrule
import datetime
import os
import sets
import subprocess
import sys

# TODO: Clean up arg parsing / setup
# TODO: Clean up last script funky bits

git_repo = sys.argv[1]
start = sys.argv[2]
until = sys.argv[3]
print "Retention statistics for", git_repo
print "From", start, "to", until
os.chdir(git_repo)

def periods(start, until):
    months, res = [], []
    dt_start = datetime.datetime.strptime(start, '%Y-%m-%d')
    dt_until = datetime.datetime.strptime(until, '%Y-%m-%d')

    for dt in rrule.rrule(rrule.MONTHLY, dtstart=dt_start, until=dt_until):
        months.append(dt.strftime('%Y-%m-%d'))

    for i in range(len(months)-1):
        res.append([months[i], months[i+1]])

    return res

def contributors(since, until):
    git_str = "git log --format='%aN' --since='" + since + "' --until '" + until + "'"
    p1 = subprocess.Popen(git_str.split(), stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["sort", "-u"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close() # Allow p1 to receive a SIGPIPE if p2 exits.
    output,err = p2.communicate()
    return filter(None, output.replace('\'', '').split('\n'))

contributor_month = []
for p in periods(start, until):
    contributor_month.append(sets.Set(contributors(p[0], p[1])))

active_month = []
for m in contributor_month:
    active_month.append(len(contributor_month[0] & m))

active_month_retention = []
for am in active_month:
    active_month_retention.append(str(100 * am / active_month[0]) + "%")

print active_month
print active_month_retention
