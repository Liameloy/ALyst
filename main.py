

from src import Statistics

test_set = [1, 2, 4, 2, 5]

stat = Statistics(test_set)

print(stat.calculate_absolute_frequencies())

print(stat.calculate_relative_frequencies())

print(stat.calculate_and_bundle_absolute_frequencies())

print(stat.calculate_and_bundle_relative_frequencies())

print(stat.calculate_absolute_sum_frequency(2))

print(stat.calculate_relative_sum_frequency(2))

print(stat.calculate_span_width())