# array demiyoruz = list

users = []
print(type(users)) # list

kullanicilar = list()
print(type(kullanicilar)) # list

sayilar = [1, 2, 3]
print(sayilar)


# list birden type
urun = 'laptop'

degiskenler = [
    1,
    2,
    True,
    False,
    'gökhan',
    10.11,
    'string',
    urun
]
print(degiskenler)

# a = 1
# b = 2
# c = 3

a,b,c = 1,2,3
print(a,b,c)

ilk, ikinci, ucuncu = 'first', 'second', 'third'

numbers = [
    ilk,
    ikinci,
    ucuncu
]
print(numbers)
print(numbers[0])

# list içine degisken ekleme
dorduncu = 'fourth'
numbers.append(dorduncu)
print(numbers)

numbers.append(5)
print(numbers)

# bilgi degistirme
# print(numbers[0])
numbers[0] = 'degistin'
print(numbers)

# length -> len
print(numbers[len(numbers) - 1])
numbers[len(numbers) -1] = 'sonuncu degerim degisti'
print(numbers)

# istediğim yere ekleme -> insert
numbers.insert(2, 'yeni bir oge')
numbers.insert(0, 'ilk eleman')
numbers.insert(len(numbers), 'en son deger')
print(numbers)

# istediğim yerden listele
print(numbers[2:5])
print(numbers[4:])

# ilk 3 degisken
print(numbers[:3])

# son 3 degisken
print(numbers[len(numbers) -2:])

# terse çevirme
print(numbers[::-1])

# en son deger
print(numbers[-1])

# 2şer ya da 3er
print('*' * 30)
print(numbers)
print(numbers[::2])