""" # Tas, kagit, makas

import random

bot = random.choice(('tas', 'kagit', 'makas'))
print(bot)

kullanici = input('Taş, kağit ya da makas ?')

if kullanici == 'makas' and bot == 'makas':
    print('berabere')
elif kullanici == 'kagit' and bot == 'kagit':
    print('berabere')
elif kullanici == 'tas' and bot == 'tas':
    print('berabere')
elif kullanici == 'makas' and bot == 'kagit':
    print('kullanici kazandi')
elif kullanici == 'kagit' and bot == 'tas':
    print('kullanici kazandi')
elif kullanici == 'tas' and bot == 'makas':
    print('kullanicim kazandi')
elif bot == 'tas' and kullanici == 'makas':
    print('bot kazandi')
elif bot == 'makas' and kullanici == 'kagit':
    print('botum kazandi')
elif bot == 'kagit' and kullanici == 'tas':
    print('bot kazandi dedim')
else:
    print('yanliş değer girdiniz')
     """


# beden kitle endeksi
# bke = kilo / (boy * boy)

kilo = int(input('Kilonuz: '))
boy = int(input('Boyunuz (cm): ')) 

endeks = kilo / (boy * boy) * 10_000
print(endeks)


if endeks < 18.5:
    print(f'{endeks}: ideal kilo')
elif endeks > 18 and endeks < 28:
    print('{}: normal bir kilo'.format(endeks))
elif endeks > 28 and endeks < 35:
    print(f'{endeks}: biraz kilolusun')
else:
    print('obezsin')