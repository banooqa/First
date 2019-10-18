# Write a program to prompt the user for hours and rate per hour to compute gross pay

hours = input('Enter Hours:')
rate = input('Enter Rate:')
ihours = float(hours)
irate = float(rate)

#another way of doing this is grosspay = float(hours) * float(rate)

grosspay = ihours * irate
print('Pay:', grosspay)