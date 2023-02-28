class SortingFunction:

    def sort_ascending(self, data):
        """
        It sorts the data in ascending order based on the first element of each tuple

        :param data: the list of tuples to be sorted
        """
        data.sort(key=lambda x: x[0], reverse=False)

    def sort_descending(self, data):
        """
        Sort the data in descending order by the first element of each tuple

        :param data: the list of tuples to be sorted
        """
        data.sort(key=lambda x: x[0], reverse=True)
