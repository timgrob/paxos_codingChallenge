from functools import reduce


class PairFinder(object):

    def __init__(self, items):
        if len(items) < 2:
            raise ValueError('Not enough items in list')
        else:
            self.items = items

    def _sum(self, pair):
        return reduce(lambda a, b: a.price + b.price, pair)

    def find_in_O_n(self, max_price):
        cursor_left = 0
        cursor_right = len(self.items) - 1
        item_pair = [self.items[cursor_left], self.items[cursor_right]]
        item_pair_prev = [None, None]

        if self._sum([self.items[0], self.items[2]]) > max_price:
            return item_pair_prev

        while cursor_left < cursor_right:

            if self._sum(item_pair) <= max_price:
                cursor_left += 1
            else:
                cursor_right -= 1

            item_pair_prev = item_pair.copy()
            item_pair[0] = self.items[cursor_left]
            item_pair[1] = self.items[cursor_right]

            if (self._sum(item_pair) > max_price) and (self._sum(item_pair_prev) <= max_price):
                break

        return item_pair_prev

    def find_in_O_n2(self, max_price):
        items_copy = self.items.copy()
        item_pair = [None, None]
        item_sum = 0
        for i in self.items:
            items_copy.remove(i)
            for j in items_copy:
                price_of_pair = i.price + j.price

                if price_of_pair > max_price:
                    break

                if price_of_pair > item_sum:
                    item_pair[0] = i
                    item_pair[1] = j

                item_sum = self._sum(item_pair)

        return item_pair
