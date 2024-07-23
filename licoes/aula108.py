# Count é um iterador sem fim

from itertools import count
#          count começa no oito, pula de oito em oito (count é infinito)
c1 = count(8, 8)
#          range começa no oito termina em 100, pula de 8 em 8 (range você pode definir quando parar)
r1 = range(8,100,8)

print('count')
for i in c1:
    print(i)
    if i >= 100:
        break

print('range')

for i in r1:
    print(i)

