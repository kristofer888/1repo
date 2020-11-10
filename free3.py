name = input('What is your name? ')
print('hi ' + name)
you = int(input('How many candies do you want? '))
a = 1
av = 5
while a<=you:
    if a>av:
        break
    print('candy')
    a+=1

for c in range(1,20):
    if c%3==0 or c%5==0:
        continue
    print(c)

for d in range(1,50):
    if (d%2!=0):
        pass
    else:
        print(d)

q = ['eagle','snake','bird','fish',2,4,56.6,3,4,5,6,7]
for p in q:
    print(p)
print(len(q))
q.append(23)
print(q)
q.extend([56.2,87])
print(q)
q.extend(['you','me'])
print(q)
q.insert(0,'monkey')
print(q)
q.insert(-14,'maya')
print(q)
q.pop(-1)
print(q)
q.remove('eagle')
print(q)
for k in range(1,10+1):
    print(k)
print(q[0:4])
print(q)
print(q[7:10])
