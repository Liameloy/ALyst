
class Dataclass:
    def __init__(self, class_index, class_lower_bound, class_upper_bound, class_width):
        if class_lower_bound >= class_upper_bound:
            print("lower bound is greater or equal to upper bound, this should be switched or reviewed")
        self.class_index = class_index
        self.class_lower_bound = class_lower_bound
        self.class_upper_bound = class_upper_bound
        self.class_width = class_width

    def __repr__(self):
        return (f"MyClass(class_index = {self.class_index}, class_lower_bound={self.class_lower_bound}, "
                f"class_upper_bound={self.class_upper_bound}, class_width={self.class_width})")

    def __eq__(self, other):
        return (isinstance(other, Dataclass) and self.class_index == other.class_index and
                self.class_lower_bound == other.class_lower_bound and self.class_upper_bound == other.class_upper_bound)

    def print_class_information(self):
        print(self)

    def check_if_elem_in_dataclass(self, element, is_last=False):
        if element is None:
            return False
        if is_last:
            if self.class_lower_bound <= element <= self.class_upper_bound:
                return True
            else:
                return False
        else:
            if self.class_lower_bound <= element < self.class_upper_bound:
                return True
            else:
                return False

