from collections.abc import Sequence


class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class IndexableNode(BinaryNode):
    def _search(self, count, index):
        pass

    def __getitem__(self, index):
        found, _ = self._search(0, index)

        if not found:
            raise IndexError('Index out of range')

        return found.value
