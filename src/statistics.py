import math

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
        return amount_classes

    def calculate_span_width(self):
        sorted_dataset = sorted(self.dataset)
        span_width = sorted_dataset[len(sorted_dataset)-1]-sorted_dataset[0]
        return span_width

    def calculate_class_width(self):
        amount_classes = self.calculate_amount_classes()
        span_width = self.calculate_span_width()
        class_width = span_width/amount_classes
        return class_width

    def classify_dataset(self):
        classified_dataset = {}





