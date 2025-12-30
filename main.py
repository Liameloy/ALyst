import math

from src import Statistics

empty_set = []
integer_set = [1,2,2,3,3,4,5,5,5,6,7,7]
floating_set = [1.1, 2.01, 2.01, 3.5, 3.5, 4.1, 5,5,5, 6.1,6.2, 7.001, 7.001]
big_set = [26, 15, 62, 40, 66, 67, 2, 54, 23, 87, 64, 33, 42, 39, 56, 68, 76, 5, 61, 69, 48, 51, 93, 46, 57,
           34, 83, 96, 19, 94, 49, 60, 53, 25, 30, 90, 99, 32, 13, 44, 38, 24, 20, 35, 75, 89, 27, 50, 63, 21]

empty_stat = Statistics(empty_set)
integer_stat = Statistics(integer_set)
floating_stat = Statistics(floating_set)
big_stat = Statistics(big_set)

print(empty_stat.full_run())

print(integer_stat.full_run())

print(floating_stat.full_run())

print(big_stat.full_run())


print(math.ceil(3.25))

