""" Implementation of CustomList """


class CustomList(list):
    """
    Child class for list.
    implemented arithmetic operations:
    +, -, ==, !=, >, >=, <, <=
    """

    def __init__(self, data=None):
        super().__init__()
        self.list = data or []

    def __add__(self, other):
        if len(self) == len(other):
            result = [x + y for x, y in zip(self, other)]
        elif len(self) < len(other):
            result = [x + y for x, y in zip(self, other[: len(self)])]
            for i in range(len(self), len(other)):
                result.append(other[i])
        return CustomList(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if len(self) == len(other):
            result = [x - y for x, y in zip(self, other)]
        else:
            result = [x - y for x, y in zip(self, other[: len(self)])]
            result.extend([-i for i in other[len(self):]])
        return CustomList(result)

    def __rsub__(self, other):
        return CustomList([-i for i in self.__sub__(other)])

    def __str__(self):
        summa = sum(i for i in self.list if isinstance(i, int))
        return f"{self.list}, sum={summa}"

    def __eq__(self, other):
        return sum(self.list) == sum(other.list)

    def __ne__(self, other):
        return sum(self.list) != sum(other.list)

    def __gt__(self, other):
        return sum(self.list) > sum(other.list)

    def __ge__(self, other):
        return sum(self.list) >= sum(other.list)

    def __lt__(self, other):
        return sum(self.list) < sum(other.list)

    def __le__(self, other):
        return sum(self.list) <= sum(other.list)
