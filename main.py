import os
import sys
from random import randint


git_url = 'https://github.com/your_github_username/github-hack.git' if not sys.argv[1] else sys.argv[1]    #your GitHub repository URL
num_year = 3  #number of year to go back

print('Hacking:', git_url)

for days in range(1, num_year*365 + 1):     #go back in time (days)
    for times in range(1, randint(2,10)):   #number of contrib per day
        if randint(1,2) == 1:               #skip some days
            continue
        d = str(days) + ' day ago'
        with open('bot.txt', 'w') as file:
            file.write(str(d) + ' - ' + str(times) + ' times')
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "' + str(days) + ' commit"')

os.system('git push '+git_url+' main')
