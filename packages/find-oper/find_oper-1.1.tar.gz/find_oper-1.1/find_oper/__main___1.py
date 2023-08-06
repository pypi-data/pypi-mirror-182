"""simple interface for demonstration
"1 2 3 4 5 7 11"
"""

import argparse
from find_operators import find
try:
    import pytest
except ImportError:
    pytest = None


def main():
    """CLI arguments, possible options for finding set of operators"""
    parser = argparse.ArgumentParser()
    parser.add_argument('regions', type=str, nargs='?', help='The set of all regions that need to be covered', default="2 5 6 7 77 177 1001")
    parser.add_argument('-t', '--test', action='store_true', help='test mode')
    args = parser.parse_args()
    reg = args.regions
    test = args.test
    if test:
        print('TEST')
        if pytest:
            pytest.main(['-q', 'find_oper/test.py'])
        else:
            print('No pytest found, only doctest will run')
    else:
        dict_of_operators = {'Билайн': {1, 5, 19, 77, 1001},
                       'O!': {2, 3, 4, 5, 6, 7},
                       'Мегаком': {1, 3, 5, 177}}
        regions = set(map(int, reg.split()))
        print(find(dict_of_operators, regions))


if __name__ == '__main__':
    main()
