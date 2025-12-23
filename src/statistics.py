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


