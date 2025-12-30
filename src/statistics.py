import math

from src.dataclass import Dataclass


class Statistics:

    def __init__(self, dataset):
        self.dataset = dataset


    def calculate_absolute_frequencies(self):
        dataset_element_absolute_frequencies = []
        frequency_dict = {}

        for element in self.dataset:
            key = tuple(element) if isinstance(element, list) else element
            frequency_dict[key] = frequency_dict.get(key, 0) + 1

        for element in self.dataset:
            key = tuple(element) if isinstance(element, list) else element
            dataset_element_absolute_frequencies.append(frequency_dict[key])

        return dataset_element_absolute_frequencies

    def calculate_relative_frequencies(self):
        dataset_element_absolute_frequencies = self.calculate_absolute_frequencies()
        dataset_element_relative_frequencies = [dataset_element / len(self.dataset) for dataset_element in
                                                dataset_element_absolute_frequencies]
        return dataset_element_relative_frequencies


    def calculate_and_bundle_absolute_frequencies(self):
        absolute_frequency_dict = {}
        for element in self.dataset:
            if element in absolute_frequency_dict:
                absolute_frequency_dict[element] += 1
            else:
                absolute_frequency_dict[element] = 1
        return absolute_frequency_dict

    def calculate_and_bundle_relative_frequencies(self):
        absolute_frequency_dict = self.calculate_and_bundle_absolute_frequencies()
        dataset_length = len(self.dataset)
        relative_frequency_dict = {}
        for element, absolute_frequency in absolute_frequency_dict.items():
            relative_frequency_dict[element] = absolute_frequency / dataset_length
        return relative_frequency_dict

    def calculate_absolute_sum_frequency(self, category_index):
        dataset_and_absolute_frequency_items = list(self.calculate_and_bundle_absolute_frequencies().items())
        return sum(absolute_frequency for element, absolute_frequency in dataset_and_absolute_frequency_items[:category_index+1])

    def calculate_relative_sum_frequency(self, category_index):
        dataset_and_relative_frequency_items = list(self.calculate_and_bundle_relative_frequencies().items())
        return sum(relative_frequency for element, relative_frequency in dataset_and_relative_frequency_items[:category_index+1])

    def calculate_amount_classes(self):
        if len(self.dataset) > 25:
            amount_classes = 1 + 3.3 * math.log10(len(self.dataset))    #sturges-rule
        else:
            amount_classes = math.sqrt(len(self.dataset))
        return math.ceil(amount_classes)

    def calculate_span_width(self):
        if self.dataset == []:
            return 0
        sorted_dataset = sorted(self.dataset)
        span_width = sorted_dataset[len(sorted_dataset)-1]-sorted_dataset[0]
        return span_width

    def calculate_class_width(self):
        amount_classes = self.calculate_amount_classes()
        if amount_classes == 0:
            return 0
        span_width = self.calculate_span_width()
        class_width = span_width/amount_classes
        # nice rounding algorithm
        extracted_scale = 10 ** math.floor(math.log10(class_width))
        scaled_width = class_width / extracted_scale
        if scaled_width <= 1:
            round_res = 1
        elif scaled_width <= 2:
            round_res = 2
        elif scaled_width <= 5:
            round_res = 5
        else:
            round_res = 10
        return round_res * extracted_scale

    def create_data_classes(self):
        class_width = self.calculate_class_width()
        data_class_index = 1
        data_classes = []
        start = min(self.dataset) if self.dataset != [] else 0
        max_elem = max(self.dataset) if self.dataset != [] else len(self.dataset)
        while start < max_elem:
            end = start + class_width
            data_classes.append(Dataclass(data_class_index, start, end, class_width))
            start = end
            data_class_index += 1
        return data_classes

    #returns dictionary with data elements as keys and class as values
    def classify_dataset_data_to_classes(self):
        classified_dataset = {}
        data_classes = self.create_data_classes()
        for element in self.dataset:
            if element not in classified_dataset:
                for data_class in data_classes:
                    if data_class.check_if_elem_in_dataclass(element):
                        classified_dataset[element] = data_class
        return classified_dataset

    #returns dictionary with classes as elements and element-lists as values
    def classify_dataset_classes_to_data(self):
        data_classes = self.create_data_classes()
        classified_dataset = {dataclass.class_index: [] for dataclass in data_classes}
        for i, data_class in enumerate(data_classes):
            is_last = i == len(data_classes)-1
            for element in self.dataset:
                if data_class.check_if_elem_in_dataclass(element, is_last):
                    classified_dataset[data_class.class_index].append(element)
        return classified_dataset

    def full_run(self):
        print("Full run")
        return  "\n".join(map(str, ((self.calculate_absolute_frequencies(), self.calculate_relative_frequencies(),
                self.calculate_and_bundle_absolute_frequencies(), self.calculate_and_bundle_relative_frequencies(),
                self.calculate_absolute_sum_frequency(0), self.calculate_relative_sum_frequency(0),
                self.calculate_absolute_sum_frequency(len(self.dataset)-1), self.calculate_relative_sum_frequency(len(self.dataset)-1),
                self.calculate_amount_classes(), self.calculate_span_width(), self.calculate_class_width()))))


