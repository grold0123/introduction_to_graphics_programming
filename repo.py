import subprocess

git_add = ['git','add',r'C:\projects\introduction_to_graphics_programming']
git_commit = ['git','commit','-m','update']
git_push = ['git','push']

for arg in [git_add,git_commit,git_push]:
    print('\n\n')
    subprocess.run(arg)
    print('\n\n\t\t**Process complete**\n\n')

print('REPOSITORY UPDATED\n\n')