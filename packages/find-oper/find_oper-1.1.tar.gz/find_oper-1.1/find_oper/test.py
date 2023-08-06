"""testing module for greedy_alg()"""


from find_operators import find


class TestClass:
    def test_one(self):
        assert find({'O!': {4, 5, 7, 9},
                       'Мегаком': {1, 2, 3, 4, 5, 6},
                       'Билайн': {1, 4, 5, 10, 11}},
                      {1, 2, 3, 4, 5, 7, 11}) == ['Мегаком', 'O!', 'Билайн']

    def test_two(self):
        assert find({'O!': {4, 5, 7, 9},
                       'Мегаком': {1, 2, 3, 4, 5, 6},
                       'Билайн': {1, 4, 5, 10, 11}},
                      {1, 2, 3, 4, 5, 7, 77}) == None

    def test_three(self):
        assert find({'Билайн': {1, 5, 19, 77, 1001},
                       'O!': {2, 3, 4, 5, 6, 7},
                       'Мегаком': {1, 3, 5, 177}},
                      {2, 5, 6, 7, 77, 177, 1001}) == ['O!', 'Билайн', 'Мегаком']
