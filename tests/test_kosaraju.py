import unittest

from kosaraju import get_components

GRAPH = [
        (0, 2),
        (0, 3),
        (2, 3),
        (0, 4),
        (1, 5),
        (4, 3),
        (3, 1),
        (1, 2),
        (4, 0),
]


class KosarajuTests(unittest.TestCase):

    def test_get_components(self):
        components = get_components(GRAPH)
        self.assertEqual(components, [[0, 4], [1, 2, 3], [5]])
