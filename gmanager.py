import subprocess
from os import chdir, listdir, path, scandir, walk
import sys
from pathlib import Path


home_w = str(Path.home())
home_script = path.dirname(path.dirname(path.abspath(__file__)))

class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

config = '.config'
powershell = path.join(home_script, config, 'powershell')
# print(home_script)

# powershell = path.join(home_w, 'documents', 'windowspowershell')
user_code = 'Code/User'
user = path.join(home_script, config, user_code)
# user = path.join(home_w, 'AppData/Roaming', user_code)
custom = path.join(home_script, '.oh-my-zsh', 'custom')

excludedirs = ['.oh-my-zsh', 'git']

git_special_dirs = [powershell,custom]
# git_special_dirs = []
    
    
def main():

    br = ''
    msg = 'commit from gitmanagerpy'
    # msg = 'python data cleaning !!NEW!!'
    # commit(msg=msg, br=br)
    sev_repos()


def sev_repos():

    git_special_dirs.extend(git_first_level())

    for dir_ in git_special_dirs:

        # pass
        print(color.BOLD,dir_,color.END)
        chdir(dir_)
        run('pull')
        # run('status')
        # run ('remote','-v')
        # commit()
    print(color.BOLD,'End',color.END)


def walklevel():
    num_sep = home_script.count(path.sep)
    for root, dirs, files in walk(home_script):
        yield root, dirs, files
        dirs.sort()
        num_sep_this = root.count(path.sep)
        if num_sep + 1 <= num_sep_this:
            del dirs[:]


def git_first_level():
    slist = []

    for root, dirs, files in walklevel():

        if '.git' in dirs:
            if not(any(excl in root for excl in excludedirs)):
                # print(color.BOLD+root+color.END)
                slist.append(root)
    return slist


def run(*args):
    return subprocess.check_call(['git'] + list(args))
    # return subprocess.Popen(['git'] + list(args))


def commit(br=None, msg=None):

    commit_message = msg
    branch = br
    if br == '':
        branch = 'master'
    if msg == None:
        commit_message = 'commit from gitmanager.py'

    print(commit_message)

    run('add', '.')
    run('commit', '-am', commit_message)
    run('push')


def branch(br):

    run('checkout', '-b', br)


if __name__ == '__main__':
    main()