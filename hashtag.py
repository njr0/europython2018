import unittest


class BadInputError(Exception):
    pass


def split_hashtag(hashtag):
    """
    Split a hashtag into a string of space-separated words
    if the hashtag uses camelCase.

    e.g. '#thisKindOfHashTag' --> 'this Kind Of Hash Tag'
    """
    if not type(hashtag) == str or not hashtag.startswith('#'):
        raise BadInputError('split_hashtag needs a string starting "#"')

    out = []
    for c in hashtag[1:]:
        if c.isupper() and out != []:
            out.append(' ')
        out.append(c)
    return ''.join(out)


class TestHashTagSplitter(unittest.TestCase):
    def test_simple_camelCase_hashtag(self):
        self.assertEqual(split_hashtag('#thisKindOfHashTag'),
                                       'this Kind Of Hash Tag')

    def test_simple_CamelCase_hashtag(self):
        self.assertEqual(split_hashtag('#ThisKindOfHashTag'),
                                       'This Kind Of Hash Tag')

    def testEmptyInputs(self):
        self.assertEqual(split_hashtag('#'), '')

    def testBadInputs(self):
        self.assertRaises(BadInputError, split_hashtag, '')
        self.assertRaises(BadInputError, split_hashtag, 'no hash')
        self.assertRaises(BadInputError, split_hashtag, 1)
        self.assertRaises(BadInputError, split_hashtag, None)


if __name__ == '__main__':
    unittest.main()
