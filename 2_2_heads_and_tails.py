"""
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла,
а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество
подряд выпавших Решек. Если выпавших Решек нет, то необходимо вывести число 0.
"""
oreshka = input().split('О')

print(len(max(oreshka)))
