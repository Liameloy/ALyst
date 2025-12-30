from src.statistics import Statistics
from src.dataclass import Dataclass

empty_set = []
integer_set = [1,2,2,3,3,4,5,5,5,6,7,7]
floating_set = [1.1, 2.01, 2.01, 3.5, 3.5, 4.1, 5,5,5, 6.1,6.2, 7.001, 7.001]
big_set = [26, 15, 62, 40, 66, 67, 2, 54, 23, 87, 64, 33, 42, 39, 56, 68, 76, 5, 61, 69, 48, 51, 93, 46, 57,
           34, 83, 96, 19, 94, 49, 60, 53, 25, 30, 90, 99, 32, 13, 44, 38, 24, 20, 35, 75, 89, 27, 50, 63, 21]

empty_stat = Statistics(empty_set)
integer_stat = Statistics(integer_set)
floating_stat = Statistics(floating_set)
big_stat = Statistics(big_set)

def test_calculate_absolute_frequencies():
    assert integer_stat.calculate_absolute_frequencies() == [1, 2, 2, 2, 2, 1, 3, 3, 3, 1, 2, 2]
    assert empty_stat.calculate_absolute_frequencies() == []
    assert floating_stat.calculate_absolute_frequencies() == [1, 2, 2, 2, 2, 1, 3, 3, 3, 1, 1, 2, 2]
    assert big_stat.calculate_absolute_frequencies() == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def test_calculate_relative_frequencies():
    assert empty_stat.calculate_relative_frequencies() == []
    assert integer_stat.calculate_relative_frequencies() == [0.08333333333333333,
                                                             0.16666666666666666,
                                                             0.16666666666666666,
                                                             0.16666666666666666,
                                                             0.16666666666666666,
                                                             0.08333333333333333,
                                                             0.25,
                                                             0.25,
                                                             0.25,
                                                             0.08333333333333333,
                                                             0.16666666666666666,
                                                             0.16666666666666666]
    assert floating_stat.calculate_relative_frequencies() == [0.07692307692307693,
                                                              0.15384615384615385,
                                                              0.15384615384615385,
                                                              0.15384615384615385,
                                                              0.15384615384615385,
                                                              0.07692307692307693,
                                                              0.23076923076923078,
                                                              0.23076923076923078,
                                                              0.23076923076923078,
                                                              0.07692307692307693,
                                                              0.07692307692307693,
                                                              0.15384615384615385,
                                                              0.15384615384615385]
    assert big_stat.calculate_relative_frequencies() == [0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                                                         0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                                                         0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                                                         0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                                                         0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02]

def test_calculate_and_bundle_absolute_frequencies():
    assert empty_stat.calculate_and_bundle_absolute_frequencies() == {}
    assert integer_stat.calculate_and_bundle_absolute_frequencies() == {1: 1, 2: 2, 3: 2, 4: 1, 5: 3, 6: 1, 7: 2}
    assert floating_stat.calculate_and_bundle_absolute_frequencies() == {1.1: 1, 2.01: 2, 3.5: 2, 4.1: 1, 5: 3, 6.1: 1, 6.2: 1, 7.001: 2}
    assert big_stat.calculate_and_bundle_absolute_frequencies() == {26: 1, 15: 1, 62: 1, 40: 1, 66: 1, 67: 1, 2: 1, 54: 1, 23: 1, 87: 1,
                                                                    64: 1, 33: 1, 42: 1, 39: 1, 56: 1, 68: 1, 76: 1, 5: 1, 61: 1, 69: 1,
                                                                    48: 1, 51: 1, 93: 1, 46: 1, 57: 1, 34: 1, 83: 1, 96: 1, 19: 1, 94: 1,
                                                                    49: 1, 60: 1, 53: 1, 25: 1, 30: 1, 90: 1, 99: 1, 32: 1, 13: 1, 44: 1,
                                                                    38: 1, 24: 1, 20: 1, 35: 1, 75: 1, 89: 1, 27: 1, 50: 1, 63: 1, 21: 1}

def test_calculate_and_bundle_relative_frequencies():
    assert empty_stat.calculate_and_bundle_relative_frequencies() == {}
    assert integer_stat.calculate_and_bundle_relative_frequencies() == {1: 0.08333333333333333,
                                                                        2: 0.16666666666666666,
                                                                        3: 0.16666666666666666,
                                                                        4: 0.08333333333333333,
                                                                        5: 0.25,
                                                                        6: 0.08333333333333333,
                                                                        7: 0.16666666666666666}
    assert floating_stat.calculate_and_bundle_relative_frequencies() == {1.1: 0.07692307692307693,
                                                                         2.01: 0.15384615384615385,
                                                                         3.5: 0.15384615384615385,
                                                                         4.1: 0.07692307692307693,
                                                                         5: 0.23076923076923078,
                                                                         6.1: 0.07692307692307693,
                                                                         6.2: 0.07692307692307693,
                                                                         7.001: 0.15384615384615385}
    assert big_stat.calculate_and_bundle_relative_frequencies() == {26: 0.02, 15: 0.02, 62: 0.02, 40: 0.02, 66: 0.02,
                                                                    67: 0.02, 2: 0.02, 54: 0.02, 23: 0.02, 87: 0.02,
                                                                    64: 0.02, 33: 0.02, 42: 0.02, 39: 0.02, 56: 0.02,
                                                                    68: 0.02, 76: 0.02, 5: 0.02, 61: 0.02, 69: 0.02,
                                                                    48: 0.02, 51: 0.02, 93: 0.02, 46: 0.02, 57: 0.02,
                                                                    34: 0.02, 83: 0.02, 96: 0.02, 19: 0.02, 94: 0.02,
                                                                    49: 0.02, 60: 0.02, 53: 0.02, 25: 0.02, 30: 0.02,
                                                                    90: 0.02, 99: 0.02, 32: 0.02, 13: 0.02, 44: 0.02,
                                                                    38: 0.02, 24: 0.02, 20: 0.02, 35: 0.02, 75: 0.02,
                                                                    89: 0.02, 27: 0.02, 50: 0.02, 63: 0.02, 21: 0.02}

def test_calculate_absolute_sum_frequency():
    assert empty_stat.calculate_absolute_sum_frequency(0) == 0
    assert empty_stat.calculate_absolute_sum_frequency(len(empty_stat.dataset)-1) == 0
    assert integer_stat.calculate_absolute_sum_frequency(0) == next(iter(integer_stat.calculate_and_bundle_absolute_frequencies().values()))
    assert integer_stat.calculate_absolute_sum_frequency(len(integer_stat.dataset)-1) == sum(integer_stat.calculate_and_bundle_absolute_frequencies().values())
    assert floating_stat.calculate_absolute_sum_frequency(0) == next(iter(floating_stat.calculate_and_bundle_absolute_frequencies().values()))
    assert floating_stat.calculate_absolute_sum_frequency(len(floating_stat.dataset)-1) == sum(floating_stat.calculate_and_bundle_absolute_frequencies().values())
    assert big_stat.calculate_absolute_sum_frequency(0) == next(iter(big_stat.calculate_and_bundle_absolute_frequencies().values()))
    assert big_stat.calculate_absolute_sum_frequency(len(big_stat.dataset)-1) == sum(big_stat.calculate_and_bundle_absolute_frequencies().values())

def test_calculate_relative_sum_frequency():
    assert empty_stat.calculate_relative_sum_frequency(0) == 0
    assert empty_stat.calculate_relative_sum_frequency(len(empty_stat.dataset) - 1) == 0
    assert integer_stat.calculate_relative_sum_frequency(0) == next(
        iter(integer_stat.calculate_and_bundle_relative_frequencies().values()))
    assert integer_stat.calculate_relative_sum_frequency(len(integer_stat.dataset) - 1) == sum(
        integer_stat.calculate_and_bundle_relative_frequencies().values())
    assert floating_stat.calculate_relative_sum_frequency(0) == next(
        iter(floating_stat.calculate_and_bundle_relative_frequencies().values()))
    assert floating_stat.calculate_relative_sum_frequency(len(floating_stat.dataset) - 1) == sum(
        floating_stat.calculate_and_bundle_relative_frequencies().values())
    assert big_stat.calculate_relative_sum_frequency(0) == next(
        iter(big_stat.calculate_and_bundle_relative_frequencies().values()))
    assert big_stat.calculate_relative_sum_frequency(len(big_stat.dataset) - 1) == sum(
        big_stat.calculate_and_bundle_relative_frequencies().values())

def test_calculate_amount_classes():
    assert empty_stat.calculate_amount_classes() == 0
    assert integer_stat.calculate_amount_classes() == 4
    assert floating_stat.calculate_amount_classes() == 4
    assert big_stat.calculate_amount_classes() == 7

def test_calculate_span_width():
    assert empty_stat.calculate_span_width() == 0
    assert integer_stat.calculate_span_width() == 6
    assert floating_stat.calculate_span_width() == 5.901
    assert big_stat.calculate_span_width() == 97

def test_calculate_class_width():
    assert empty_stat.calculate_class_width() == 0
    assert integer_stat.calculate_class_width() == 2
    assert floating_stat.calculate_class_width() == 2
    assert big_stat.calculate_class_width() == 20

def test_create_data_classes():
    assert empty_stat.create_data_classes() == []
    assert (integer_stat.create_data_classes() ==
            [Dataclass(class_index = 1, class_lower_bound=1, class_upper_bound=3, class_width=2),
            Dataclass(class_index = 2, class_lower_bound=3, class_upper_bound=5, class_width=2),
            Dataclass(class_index = 3, class_lower_bound=5, class_upper_bound=7, class_width=2)])
    assert (floating_stat.create_data_classes() ==
            [Dataclass(class_index = 1, class_lower_bound=1.1, class_upper_bound=3.1, class_width=2),
            Dataclass(class_index = 2, class_lower_bound=3.1, class_upper_bound=5.1, class_width=2),
            Dataclass(class_index = 3, class_lower_bound=5.1, class_upper_bound=7.1, class_width=2)])
    assert (big_stat.create_data_classes() ==
            [Dataclass(class_index = 1, class_lower_bound=2, class_upper_bound=22, class_width=20),
            Dataclass(class_index = 2, class_lower_bound=22, class_upper_bound=42, class_width=20),
            Dataclass(class_index = 3, class_lower_bound=42, class_upper_bound=62, class_width=20),
            Dataclass(class_index = 4, class_lower_bound=62, class_upper_bound=82, class_width=20),
            Dataclass(class_index = 5, class_lower_bound=82, class_upper_bound=102, class_width=20)]
)

#def test_classify_dataset_data_to_classes():

#def test_classify_dataset_classes_to_data():