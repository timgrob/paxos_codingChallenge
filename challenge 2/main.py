import sys
import collections
from PairFinder import PairFinder


def read_file(filename):
    txt_file = open(filename, 'r')
    Item = collections.namedtuple('Item', ['name', 'price'])
    items = []

    for line in txt_file:
        line_split = line.split(',')
        items.append(
            Item(name=line_split[0], price=int(line_split[1].rstrip('\n')))
        )

    return items

def print_items_to_console(pair):
    if None in pair:
        print('Not possible')
    else:
        print('{} {}, {} {}'.format(pair[0].name, pair[0].price, pair[1].name, pair[1].price))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Not enough input parameters')
    else:
        gift_items = read_file(sys.argv[1])

        try:
            pf = PairFinder(gift_items)
            pair_n = pf.find_in_O_n(int(sys.argv[2]))
            pair_n2 = pf.find_in_O_n2(int(sys.argv[2]))

            print_items_to_console(pair_n)
            print_items_to_console(pair_n2)
        except ValueError as e:
            print(f'Error: {e}')
        except Exception as ex:
            print(ex)

