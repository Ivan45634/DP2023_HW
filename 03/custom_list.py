""" Implementation of CustomList """


class CustomList(list):
    """
    Child class for list.
    implemented arithmetic operations:
    +, -, ==, !=, >, >=, <, <=
    """

    def __init__(self, lst):
        super().__init__(lst)

    def __add__(self, other):
        if len(self) == len(other):
            result = [x + y for x, y in zip(self, other)]
        elif len(self) < len(other):
            result = [x + y for x, y in zip(self, other[: len(self)])]
            for i in range(len(self), len(other)):
                result.append(other[i])
        else:
            result = other + self
        return CustomList(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if len(self) == len(other):
            result = [x - y for x, y in zip(self, other)]
        elif len(self) > len(other):
            result = [x - y for x, y in zip(self, other)]
            result.extend(self[len(other):])
        else:
            result = [x - y for x, y in zip(self, other[: len(self)])]
            result.extend([-i for i in other[len(self):]])
        return CustomList(result)

    def __rsub__(self, other):
        return [-i for i in self.__sub__(other)]

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)
