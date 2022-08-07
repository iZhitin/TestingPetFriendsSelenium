import math
a = 11
b = 10

c = a/2
d = a//2

print(math.ceil(c), d)

names = ['ds', 'sd', 'ds', 'ds', 'ds', 21]

# len(list(set(names))) == len(names)
print(len(list(set(names))))
print(len(names))

lll = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# print('Проверочка')
# print(set(l))
# print(len(l))

l = {'name': 'имя','type': 'тип','age': 'возраст'}
d = {'name1': 'имя','type1': 'тип','age1': 'возраст'}
dd = {'name1': 'имя','type1': 'тип','age1': 'возраст'}
ddd = {'name2': 'имя','type2': 'тип','age2': 'возраст'}
dddd = {'name2': 'имя','type2': 'тип','age2': 'возраст'}
ddddd = {'name3': 'имя','type3': 'тип','age3': 'возраст'}
ll = []
ll.append(l)
ll.append(d)
ll.append(dd)
ll.append(ddd)
ll.append(dddd)

print(ll)
a = True
lll = [[1, 2, 3], [1, 2, 4], [1, 2, 5]]
for i in range(len(lll)):
    for j in range(len(lll)):
        if i != j:
            if lll[i] == lll[j]:
                a = False
                # print('Есть одинаковые словари')


# print(len(lll))
print(a)