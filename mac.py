#!/usr/bin/env python

# > python -i ./mac.py ~/git/status-react/ 2017-01-01 2018-01-01

from dateutil import rrule
import datetime
import itertools
import os
import sets
import subprocess
import sys

# TODO: Clean up arg parsing / setup
# TODO: Clean up last script funky bits

# git rev-list --all | tail -n1 | xargs git log --format=%ci | xargs echo | cut -d " " -f 1
def first_commit():
    pipe_cmds = ["git rev-list --all", "tail -n1", "xargs git log --format=%ci", "xargs echo"]
    procs = []
    procs.append(subprocess.Popen(pipe_cmds[0].split(), stdout=subprocess.PIPE))
    procs.append(subprocess.Popen(pipe_cmds[1].split(), stdin=procs[0].stdout, stdout=subprocess.PIPE))
    procs.append(subprocess.Popen(pipe_cmds[2].split(), stdin=procs[1].stdout, stdout=subprocess.PIPE))
    procs.append(subprocess.Popen(pipe_cmds[3].split(), stdin=procs[2].stdout, stdout=subprocess.PIPE))
    output, err = procs[3].communicate()
    return output[:10]

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

repos = sys.argv[1:]

# XXX: Hacky af
index = 0
repo_stats = []
for git_repo in repos:
    repo_stats.append([])
    os.chdir(git_repo)
    git_name = git_repo.split("/")[-2]
    start = first_commit()
    until = "2018-01-01"

    repo_stats[index].append(git_name + " (" + start + " - " + until + ")")

    contributor_month = []
    for p in periods(start, until):
        contributor_month.append(sets.Set(contributors(p[0], p[1])))

    for m in contributor_month:
        repo_stats[index].append(len(m))

    index = index + 1

for row in list(itertools.izip_longest(*repo_stats)):
    csv_row = ""
    for col in row:
        if col == None:
            cell = ""
        else:
            cell = str(col)
        csv_row = csv_row + cell + ","
    print csv_row

# > ./mac.py ~/git/status-react/ ~/git/status-go/ > foo.csv
