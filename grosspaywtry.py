#Rewrite the grosspay prog using try/except

hours = input('Enter Hours:')
rate = input('Enter Rate')
try:
    ihours = float(hours)
    irate = float(rate)
except:
    print('Error, Please Enter a Numeric Input')
    quit()

grosspay = irate * ihours
print('Pay:', grosspay)




