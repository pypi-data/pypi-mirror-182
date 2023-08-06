"""The module "find_operators"
a) select the operator covering the largest number
of regions and not yet included in the coverage. If the operator will cover
some regions already included in the coverage, this is normal;
b) repeat until uncovered elements of the set remain"""


def find(dict_of_operators, set_of_regions):
    """
        module example:
        >>> find({'Билайн': {4, 5, 7, 9}, 'Мегаком': {1, 2, 3, 4, 5, 6}}, {1, 2, 3, 4, 5, 7})
        ['Мегаком', 'Билайн']

        :param regions: set of regions
        :return: list with answer
    """
    result = []
    while set_of_regions:
        list_of_tuples = []
        for index, item in dict_of_operators.items():
            list_of_tuples.append((index, item & set_of_regions))
        if all(time_try[1] == set() for time_try in list_of_tuples):
            return
        list_of_tuples.sort(key=lambda x: len(x[1]), reverse=True)
        set_of_regions -= list_of_tuples[0][1]
        result.append(list_of_tuples[0][0])
        del dict_of_operators[list_of_tuples[0][0]]
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
