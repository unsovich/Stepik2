"""
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым, а остальные
сдвигаются на одну позицию вперед, в сторону увеличения индексов.
"""
nums = input().split()

nums.insert(0, nums[len(nums) - 1])
del nums[len(nums) - 1]

print(*nums)
