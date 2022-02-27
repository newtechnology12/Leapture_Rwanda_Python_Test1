import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from task import read_json_file
except ImportError:
    pass

try:
    from task import get_types
except ImportError:
    pass

try:
    from task import get_types_counts
except ImportError:
    pass

try:
    from task import get_author_count
except ImportError:
    pass


d_1 = {
        "articles": [{
            "slug": "how-to-train-your-mule",
            "title": "How to train your mule",
            "description": "Ever wonder how?",
            "body": "It takes a Jacobian",
            "tagList": ["mules", "training"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 0,
            "author": {
              "username": "jake",
              "bio": "I work at statefarm",
              "following": False
            }
        }, {
            "slug": "and another article",
            "body": "I'm getting bored",
            "tagList": ["bored", "article"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 20,
            "author": {
              "username": "cap",
              "following": True
            }
        }],
        "tweets": [{
            "body": "See my article on training mules.",
            "author": {
              "username": "jake"
            }
        }]
    }

d_2 = {
        "articles": [{
            "slug": "how-to-train-your-mule",
            "title": "How to train your mule",
            "description": "Ever wonder how?",
            "body": "It takes a Jacobian",
            "tagList": ["mules", "training"],
            "createdAt": "2016-02-18T03:22:56.637Z",
            "updatedAt": "2016-02-18T03:48:35.824Z",
            "favoritesCount": 0,
            "author": {
              "username": "jake",
              "bio": "I work at statefarm",
              "following": False
            }
        }],
        "books": [{
            "body": "See my article on training mules.",
            "author": {
              "username": "jake"
            }
        }],
        "papers": []
    }


class TestStudent(unittest.TestCase):
    def test_read_json_file_s_1(self):
        ret_val = read_json_file('data.json')
        assert ret_val == d_1

    def test_read_json_file_s_2(self):
        ret_val = read_json_file('data_2.json')
        assert ret_val == d_2


    def test_get_types_s_1(self):
        ret_val = get_types(d_1)
        for i in ['tweets', 'articles']:
            assert i in ret_val
        assert len(ret_val) == 2

    def test_get_types_s_2(self):
        ret_val = get_types({})
        assert ret_val == []

    def test_get_types_s_3(self):
        ret_val = get_types(d_2)
        for i in ['books', 'articles', 'papers']:
            assert i in ret_val
        assert len(ret_val) == 3

    def test_get_types_counts_s_1(self):
        ret_val = get_types_counts(d_1)
        assert len(ret_val) == 2
        assert ret_val['articles'] == 2
        assert ret_val['tweets'] == 1

    def test_get_types_counts_s_2(self):
        ret_val = get_types_counts(d_2)
        assert len(ret_val) == 3
        assert ret_val['articles'] == 1
        assert ret_val['books'] == 1
        assert ret_val['papers'] == 0

    def test_get_types_counts_s_3(self):
        ret_val = get_types_counts({})
        assert len(ret_val) == 0

    def test_get_author_count_s_1(self):
        ret_val = get_author_count(d_1, 'jake')
        assert ret_val == 2

    def test_get_author_count_s_2(self):
        ret_val = get_author_count(d_1, 'cap')
        assert ret_val == 1

    def test_get_author_count_s_3(self):
        ret_val = get_author_count({}, 'whoever')
        assert ret_val == 0
    
    def test_get_author_count_s_4(self):
        ret_val = get_author_count({}, 'missing')
        assert ret_val == 0

    def test_get_author_count_s_5(self):
        ret_val = get_author_count(d_2, 'cap')
        assert ret_val == 0


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStudent)
    unittest.TextTestRunner(verbosity=2, descriptions=True).run(suite)
    sys.exit(0)