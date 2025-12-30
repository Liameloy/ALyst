from src.dataclass import Dataclass

none_elem = None
integer_elem = 1
float_elem = 0.0001
outside_elem = -1

test_index = 1

test_lower_bound = 0
test_upper_bound = 1

test_class_width = test_upper_bound - test_lower_bound

test_data_class = Dataclass(test_index, test_lower_bound, test_upper_bound, test_class_width)

def test_check_if_elem_in_dataclass():
    assert test_data_class.check_if_elem_in_dataclass(none_elem) == False
    assert test_data_class.check_if_elem_in_dataclass(integer_elem) == True
    assert test_data_class.check_if_elem_in_dataclass(float_elem) == True
    assert test_data_class.check_if_elem_in_dataclass(outside_elem) == False

