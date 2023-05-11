# Перед использованием установите библиотеку BioPython
from Bio.Seq import Seq

seq = Seq(input('Введите последовтельность для qPCR (ВАЖНО - одной строкой!):').replace('\n', '').upper())

a1 = Seq(input('Введите Forward Primer component:'))
a2 = Seq(input('Введите Reverse Primer component:')).reverse_complement()
n = int(input("Введите длину нуклеотидов наращиваемой последовательности, которую вы хотите включить в праймер:"))
F = a1 + seq[:n]
R = (seq[-n::] + a2).reverse_complement()
result = Seq(a1 + seq + a2)
print("Получившиеся праймеры F и R:", F, R, '\n', f'Получившаяся последовательность: {result}')
