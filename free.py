def greet():
    print('Hello')
    print('Good Morning')
greet()

def add_sub(a,b):
    c = a+b
    d = a-b
    return c,d
result1,result2 = add_sub(10,20)    
print(result1,result2)

def person(name,age,birthday):
    print(name)
    print(age)
    print(birthday)
person(age=38,name='kris',birthday='Dec. 23, 1980')    

def animal(name,age=5):
    print(name)
    print(age)
animal('chips',10)
    
def peolpe(name, **data):
    print(name)
    print(data)
peolpe('kris',age=39,add='Phillines',mob=9345567273)

Title = 'My args'
quiz_1 = 'The name of your wife.'
quiz_2 = 'The name of your daughters.'
quiz_3 = 'The name of your dog.'
quiz_4 = 'The name of your fish.'

def quiz(Title,*data):
    print(Title)
    for post in data:
        print(post)
quiz(Title,quiz_1,quiz_2,quiz_3,quiz_4)
