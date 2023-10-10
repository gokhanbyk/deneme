urunler = ['kablo', 'klavye', 'laptop']
print(urunler)

yeni_urunler = urunler.copy()
yeni_urunler[0] = 'mouse'
print(urunler)
print(yeni_urunler)

dijital_urunler = ['bilgisayar', 'telefon']

# urunler.append(dijital_urunler)
# print(urunler[3][1])

# extend
urunler.extend(dijital_urunler)
print(urunler) # ['kablo', 'klavye', 'laptop', 'bilgisayar', 'telefon']

# len
print(len(urunler)) # 5

# listenin içinde bu var mı -> in
print('bilgisayar' in urunler) # true
print('kulaklık' in urunler) # false

""" item = input('Elinizde ne var? ')
if item in urunler:
    print(f'{item} ürün bulunmakta')
else:
    print('ürün bulunmamakta') """

urunler.append('telefon')
print(urunler)
print('kaç adet: ', urunler.count('bilgisayar'))

# index bulma -> index
print('laptobumun indexi: ', urunler.index('laptop'))
print(urunler[2])

# silme -> remove
urunler.remove('telefon')
print(urunler)
urunler.append('bilgisayar')
print(urunler)
urunler.remove('bilgisayar')
print(urunler)

# degisken listeden cıkarma -> pop()
en_sonuncu_degisken = urunler.pop()
print(en_sonuncu_degisken)
print(urunler)

# tertemiz olsun -> clear()
urunler.clear()
print(urunler)

# matematiksel gömülü metotlar 
sayilar = [1, 2, 3, 4, 5, 6, 7]

# sum
print(sum(sayilar))
# min
print(min(sayilar))
# max
print(max(sayilar))

# sıralam -> sort
numbers = [2,5,8,12,1]
numbers.sort()
print(numbers)

# büyükten küçük
numbers.sort(reverse=True)
print(numbers)

# string sıralama -> sort

meyveler = ['muz', 'elma', 'üzüm']
print(meyveler)

meyveler.sort()
print(meyveler) # ['elma', 'muz', 'üzüm']

# tersten sıralama
meyveler.sort(reverse=True)
print(meyveler) # ['üzüm', 'muz', 'elma']

# silme -> pop() / del
# print(meyveler.pop())


del meyveler[1]
print(meyveler)