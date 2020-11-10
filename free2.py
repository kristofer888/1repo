name = input('What is your name? ')
print('oh, hi! ' + name)
print('welcome to multiply!')
set1 = int(input('please enter your first number: '))
set2 = int(input('please enter your second number: '))
ans = input('the result was ' + str(set1 * set2) + '. Do you agree? ')
ans1 = int(set1+set2)
if ans=='yes':
    print('right')
else:
    print('wrong')
set3 = int(input('if the 1st given number will add to second given number. What what will be the result? '))
if set3==ans1:
    print('oh great')
else:
    print('are you sure?')
you  = int(input('Rate yourself from 1 to  10. 10 is the highest. What will be? ')) 
a = (8,9,10)
b = (5,6,7)
c = (1,2,3,4)
if you in a:
    print('excellent')
elif you in b:
    print('very good')
elif you in c:
    print('try again')
else:
    print('from 1 to 10  only...try again')
if you!=1000:
    print('oh')

