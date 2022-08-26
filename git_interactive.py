"""
A script to facilitate version control usage with google colab (or any platform) using git personal tokens
"""

from encodings.utf_8 import decode
import os
from subprocess import PIPE, run

def yes_no(prompt):
    while(1):
        inp = input(f"{prompt} (y/n)\n")
        if inp == 'y':
            return True
        elif inp == 'n' :
            return False

def convert():
    if 'convert.txt' in os.listdir('.'):
        with open('convert.txt','r') as f:
            for filename in f.readlines():
                filename = filename[:-1]
                outfile = f'{filename.split(".")[0]}.py'
                print(run([
                    'colab-convert',
                    filename,
                    outfile,
                    "-l=en"
                ]))

# first store the repo owner and repo name
if 'info.txt' not in os.listdir('.'):
    repo_owner = input("Enter the repo owner username:\n")
    repo_name = input("Enter the repo name:\n")
    with open("info.txt",'w') as f:
        f.write(repo_owner)
        f.write('\n')
        f.write(repo_name)

else:
    with open("info.txt",'r') as f:
        repo_owner = f.readline()[:-1]
        print(f'repo owner: {repo_owner}')
        repo_name = f.readline()[:-1]
        print(f'repo name: {repo_name}')


username = input("Enter your username:\n")
mail = input("Enter your email:\n")

# user

print(run([
    'bash',
    'config_user.sh',
    username,
    mail,
]))

# new repo
if '.git' not in os.listdir('.'):
    print(run([
        'bash',
        'new_repo.sh',
        username,
        mail
    ]))

# remotes
out = run([
    'git',
    'remote',
    '-v'
],stdout=PIPE)

remote_name = f'{username}-origin'

if remote_name not in decode(out.stdout)[0]:

    token = input("Enter your personal access token:\n")
    remote = f'https://{token}@github.com/{repo_owner}/{repo_name}.git'

    print(run([
        'git',
        'remote',
        'add',
        remote_name,
        remote
    ]))

# convert
if yes_no("Convert notebooks in convert.txt?"):
    convert()
    
# sync

if yes_no("Do you want me to sync changes?"):


    msg = input("Commit message:\n")
    branch = input("Branch name:\n")

    print(run([
        'bash',
        'sync.sh',
        msg,
        branch,
        remote_name
    ]))
