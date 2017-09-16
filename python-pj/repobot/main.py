#!/usr/bin/env python3
from github import Github
import datetime
from employee import EmployCommit
import sys
# input_username = input("Github username: ")
# input_password = input("password: ")
# 接受命令行参数
input_username = sys.argv[1] 
input_password = sys.argv[2]

github_obj = Github(input_username, input_password)

contributions = {}

repo_name = input("repo: ")

repo_obj = github_obj.get_user().get_repo(repo_name)

print('In', repo_obj.name, ',we need to choose a branch: ')
branch_name = input("branch: ")

commites = repo_obj.get_commits(sha=branch_name,
                                since=datetime.datetime.now() - datetime.timedelta(days=7),
                                until=datetime.datetime.now()
                                )

for commit in commites:
    if commit.author is not None:
        author_name = commit.author.name
        commit_dic = {
            "author": commit.author.name,
            "sha": commit.sha,
            "time": commit.last_modified,
            "url": commit.html_url,
            "message": commit.commit.message,
        }
    else:
        author_name = "None"
        commit_dic = {
            "author": "None",
            "sha": commit.sha,
            "time": commit.last_modified,
            "url": commit.html_url,
            "message": commit.commit.message,
        }
    if author_name in contributions:
        contributions[author_name].add_commits_tot()
        contributions[author_name].add_commit(commit_dic)

    else:
        contributions[author_name] = EmployCommit(name=author_name,
                                                  commits_tot=1,
                                                  commits=[commit_dic])

for key in contributions:
    contributions[key].show_commit_tot()
    contributions[key].write_2_md()

print("\n")
