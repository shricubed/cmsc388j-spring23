import pytest

import random
import collections
import operator

import practice as p


def test_hello_world():
    assert 'Hello, World!' == p.hello_world()


def test_empty_sum_unique():
    l = []
    assert 0 == p.sum_unique(l)


def test_sum_unique():
    copies = random.randint(2, 10)

    assert 9 == p.sum_unique(([5] * copies) + [4])

    copies = random.randint(2, 10)
    l1 = [1, 2, 4, 5] * copies
    random.shuffle(l1)

    assert 12 == p.sum_unique(l1)

    copies = random.randint(2, 10)

    assert 4 == p.sum_unique([4] * copies)


def test_single_element_palindrome():
    assert p.palindrome('')
    assert p.palindrome('f')
    assert p.palindrome('7')


def test_longer_palindromes():
    assert p.palindrome('aa')
    assert p.palindrome(33)
    assert not p.palindrome('ab')
    assert not p.palindrome(48)


def test_even_longer_palindromes():
    assert p.palindrome('racecar')
    assert p.palindrome(1337331)
    assert not p.palindrome('python')
    assert not p.palindrome(1234567)


def test_small_sum_multiples():
    assert 0 == p.sum_multiples(2)
    assert 0 == p.sum_multiples(3)

    assert 3 == p.sum_multiples(5)
    assert 8 == p.sum_multiples(6)
    assert 14 == p.sum_multiples(7)


def test_large_sum_multiples():
    assert 60 == p.sum_multiples(16)
    assert 143 == p.sum_multiples(25)
    assert 354858 == p.sum_multiples(1234)


def test_empty_lists_num_func_mapper():
    nums = []
    funs = [p.sum_unique, sum]
    assert [0, 0] == p.num_func_mapper(nums, funs)

    nums = [2, 2, 2, 4, 5]
    funs = []
    assert [] == p.num_func_mapper(nums, funs)


def test_num_func_mapper_1():
    nums = [2, 2, 2, 4, 5]
    funs = [p.sum_unique, sum]
    assert [11, 15] == p.num_func_mapper(nums, funs)


def test_num_func_mapper_2():
    def most_occurring(nums):
        c = collections.Counter(nums)
        # Returns key in dict with highest value
        return max(c.items(), key=operator.itemgetter(1))[0]

    nums = [2, 2, 2, 4, 5, 8, 9]
    funs = [sum, max, most_occurring]
    assert [32, 9, 2] == p.num_func_mapper(nums, funs)


def test_pythagorean_triples():
    assert [(3, 4, 5)] == p.pythagorean_triples(10)
    assert [(3, 4, 5), (6, 8, 10)] == p.pythagorean_triples(11)
    assert [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)] == p.pythagorean_triples(20)

def test_custom_sort():
    assert [1, 3, 5, 2, 4] == p.custom_sort([1, 2, 3, 4, 5])
    assert [5, 5, 5, 4, 4, 4] == p.custom_sort([4, 5, 4, 5, 5, 4])
    
