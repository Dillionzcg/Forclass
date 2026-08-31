from merge_sort import merge_sort

def test_merge_sort_given():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_merge_sort_duplicates():
    assert merge_sort([5, 2, 2, 1, 8, 3]) == [1, 2, 2, 3, 5, 8]
    assert merge_sort([7]) == [7]
    assert merge_sort([]) == []
