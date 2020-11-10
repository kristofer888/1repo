me = input('Among the following fishes: guppy, molly, betta, shark, and whale. pick one and see for the result.')
a = {'guppy':'your great', 'molly':'something good', 'betta':'brave', 'shark':'to destroy', 'whale':'calm'}
if me=='guppy':
    print(a['guppy'])
elif me=='molly':
    print(a['molly'])
elif me=='betta':
    print(a['betta'])
elif me=='shark':
    print(a['shark'])
elif me=='whale':
    print(a['whale'])
else:
    print('not among the following choices')
b = input('what is  your favorite color? ')
c = 'blue','red','black','yellow','green'
if b in c:
    print('great')
if b not in c:
    print('How about second favorite color')
d = int(input('Guess the bills i have in my pokect? '))
e = 100, 200, 300, 400, 500, 1000
if d in e:
    print('good job')
else:
    print('wrong')


