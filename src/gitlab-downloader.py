#!/usr/bin/python3
import os
import sys
import gitlab
import subprocess


def visit(group):
    name = group.name
    real_group = glab.groups.get(group.id)

    os.mkdir(name)
    os.chdir(name) 

    clone(real_group.projects.list(all=True))

    for child in real_group.subgroups.list():
        visit(child)

    os.chdir("../")

def clone(projects):
    for repo in projects:
        command = f'git clone {repo.ssh_url_to_repo}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        process.wait()

if __name__ = '__main__':

    glab = gitlab.Gitlab(f'https://{sys.argv[1]}', f'{sys.argv[3]}')
    groups = glab.groups.list()
    root = sys.argv[2]
    
    for group in groups:
        if group.name == root:
            visit(group)
