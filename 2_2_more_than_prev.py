"""
На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. Напишите программу
подсчета количества чисел, которые больше предшествующего им в этом списке числа.
"""
nums = input().split()
counter = 0

for i in range(len(nums) - 1):
    if int(nums[i + 1]) > int(nums[i]):
        counter += 1

print(counter)
