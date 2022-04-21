import pyperclip # module to copy and paste

#isX method
# == isalpha(),isalnum(),isdecimal(),isspace(),istitle()
print('Hello'.isalnum())
print('Hello123'.isalnum())

#startswith and endswith
print('Hello World'.startswith('Hello'))

name = 'Ferdinand Cruz'
print('\n',name.startswith('Cruz'))

#join and split
print(' '.join(['My','name is','Ferdinand','Cruz']))
#print('My daugther is'.join(['Sophie','Cruz']))

#rjust, ljust, center
print('Hello'.rjust(10))
print('Hello'.ljust(5))

print('MAIN'.rjust(40,'*'))
print('MAIN'.ljust(40,'='))


#example tabular printing
def printPicnic (itemsDict, leftwidth, rightwidth) -> None:
    print('PICNIC ITEMS'.center(leftwidth + rightwidth, '-'))

    for k, v in itemsDict.items():
        print(k.ljust(leftwidth,".") + str(v).rjust(rightwidth))

picnicItems = {'Sandwiches':4,'apples':12,'cups':4,'cookies':1800}
printPicnic(picnicItems, 12,5)
printPicnic(picnicItems, 20,6)

#removing whitespace
message = "             Hello         "
print(message.strip())

#removing chars
mymess = "Ferdinand.Cruz@infor.com"
print(mymess.strip("@infor.com\n"))

pyperclip