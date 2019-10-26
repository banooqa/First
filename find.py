# Author: Banukah Banday
# This program asks for a file and looks for line containing a string and computes the mean of the values following
# that string

inp = input('Enter The File Name:')
try:
    fhand = open(inp)
except:
    print('File Not Found')
    quit()
sum = 0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence'):
        idx = line.find(':')
        x = float(line[idx + 1:])
        sum += x
        count += 1

# handing string not found case:
if count == 0:
    print('No Value Found')
    quit()

print('Mean =', sum/count)
