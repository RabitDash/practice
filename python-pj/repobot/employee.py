#!/usr/bin/env python
# encoding: utf-8

import datetime
class EmployCommit:

    def __init__(self, name, commits_tot = 0, commits = []):
        self.name = name
        self.commits_tot = commits_tot
        self.commits = commits

    def add_commits_tot(self):
        self.commits_tot += 1

    def add_commit(self, commit):
        self.commits.append(commit)

    def show_commit_tot(self):
        print("\t", self.name)

        for commit in self.commits:
            print()
            print(repr(commit['sha']).ljust(20), repr(commit['time']).ljust(30))
            print(repr(commit['url']).ljust(20))
            print()

    def write_2_md(self):
        date = str(datetime.datetime.now())[0:10:1]
        file_name = self.name + '-commit-list@' + date + '.md'
        f = open('../../weekly_report/' + file_name,'w')
        print("# ", self.name,"\'s commit weekly report\n", file = f)
        print("## ", self.name,"There are", self.commits_tot," commits in last week \n", file = f)
        index = 1
        for commit in self.commits:
            print("%d. [%s](%s) - %s \n" % (index,commit['message'], commit['url'], commit['time']), file = f)
            index += 1
        print("---", file = f)