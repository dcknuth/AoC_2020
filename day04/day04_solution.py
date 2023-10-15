'''AOC Day04 Part 1: Count the number of valid passports
In your batch file, how many passports are valid?'''
import time

#filename = "test04.txt"
filename = "input04.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

def checkValid(p):
    # required fields
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = True
    for field in req:
        if field not in p:
            valid = False
            break
    return(valid)


T0 = time.time()
# need to process each passport and will store them by pid (if valid)
#  for later, if needed. Will only store valid ones so we can use len()
#  to get the final total
# Careful: turns out that the pid field can be repeated, so I just kept
#  a count of them and used that as the dict key instead
passports = dict()
ln = 0
pnum = 0
while ln < len(ls):
    pid = ""
    cur_passport = dict()
    while ln < len(ls) and ls[ln] != '':
        fields = ls[ln].split()
        for field in fields:
            pkey, pval = field.split(':')
            cur_passport[pkey] = pval
        ln += 1
    if checkValid(cur_passport):
        passports[pnum] = cur_passport
        pnum += 1
    ln += 1

T1 = time.time()
print("Total number of valid passports is", len(passports))
print("Time taken was", T1-T0, "seconds")

'''Part 2: Count the number of valid passports - those that have all
required fields and valid values.
In your batch file, how many passports are valid?'''
# maybe we just make a new check function and run the passports
#  through that
def checkValid2(p):
    # check birth year
    try:
        y = int(p['byr'])
    except:
        return(False)
    if y < 1920 or y > 2002:
        return(False)
    # check issue year
    try:
        y = int(p['iyr'])
    except:
        return(False)
    if y < 2010 or y > 2020:
        return(False)
    # check expiration year
    try:
        y = int(p['eyr'])
    except:
        return(False)
    if y < 2020 or y > 2030:
        return(False)
    # check height
    if p['hgt'][-2:] != 'cm' and p['hgt'][-2:] != 'in':
        return(False)
    try:
        h = int(p['hgt'][:-2])
    except:
        return(False)
    if p['hgt'][-2:] == 'cm' and (h < 150 or h > 193):
        return(False)
    if p['hgt'][-2:] == 'in' and (h < 59 or h > 76):
        return(False)
    # check hair color
    if p['hcl'][0] != '#':
        return(False)
    try:
        c = int(p['hcl'][1:7])
    except:
        return(False)
    if c < 0 or c > 999999:
        return(False)
    # check eye color
    eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if p['ecl'] not in eye_color:
        return(False)
    # check passport id
    try:
        id = int(p['pid'][0:9])
    except:
        return(False)
    return(True)

valid_passports = dict()
for key in passports.keys():
    if checkValid2(passports[key]):
        valid_passports[key] = passports[key]
print("New number of valid passports is", len(valid_passports))
