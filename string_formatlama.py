first_name = 'gÖkHan'
last_name = 'BiYiK'

# str'nin içinde karakter bulma
print(first_name[2]) # k
print(last_name[-1]) # K

# belli bir yerden basla belli bir yere kadar göster
print(first_name[0:3]) # gÖk
print(last_name[:3]) # BiY
print(first_name[-3:]) # Han
print(first_name[3:]) # Han

# str'yi terse çevirme
print(first_name[::-1]) # naHkÖg
print(first_name[::-2]) # nHÖ

#  Tumu buyuk harf olsun -> upper
print(first_name.upper()) # GÖKHAN

# tumu kucuk harf olsun -> lower
print(first_name.lower()) # gökhan

# capitalize = ilk harfi büyük yapar
full_name = first_name + ' ' + last_name
print(full_name.capitalize()) # Gökhan biyik

# title = bütün ilk harfleri büyük yapar
print(full_name.title()) # Gökhan Biyik

# swapcase = büyük varsa küçültür küçük varsa büyültür
print(full_name.swapcase()) # GöKhAN bIyIk

# say = count
print(full_name.count('n')) # 1

# split = str'mi list yapar (array yapar)
print(full_name.split(' ')) # ['gÖkHan', 'BiYiK']
print(full_name.split(', ')) # ['gÖkHan BiYiK']

# join = listelerimi str yapar
names = ['Gökhan', 'Ahmet', 'Ali', 'Emre']
print(names)
print(''.join(names)) # GökhanAhmetAliEmre
print(' '.join(names)) # Gökhan Ahmet Ali Emre
print(', '.join(names)) # Gökhan, Ahmet, Ali, Emre

# soru soruyor

# istitle -> bu bi baslik seklinde mi
print('Python'.istitle()) # istitle
print('python'.istitle()) # istitle

# islower -> küçük mü ?
print('gökhan'.islower()) # true
print('Gökhan'.islower()) # false

# startswith ve endswith
print(first_name.startswith('g'))
print(first_name.endswith('n'))

# find = aradığım bilgi var mı
print(first_name.find('g'))

# replace
print(full_name.lower().replace('gökhan', 'ahmet'))