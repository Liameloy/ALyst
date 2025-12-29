from src.statistics import Statistics
empty_set = []
test_set = [1,2,2,3,3,4,5,5,5,6,7,7]

test_stat = Statistics(test_set)

def test_calculate_absolute_frequencies():
    assert test_stat.calculate_absolute_frequencies() == [1, 2, 2, 2, 2, 1, 3, 3, 3, 1, 2, 2]
