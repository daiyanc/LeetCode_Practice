def remove_duplicates(lst):
    """@params lst
    Your method should sort the array in ascending order
    then remove duplicates
    """
    pass




try:
  assert remove_duplicates([1, 1, 5, 2, 4, 9, 3, 6, 2, 4, 9, 0, 8, 0, 5, 7]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  assert remove_duplicates([7, 23, 8, 12, 40, 21, 6, 9, 0, 61, 4, 7]) == [0, 4, 6, 7, 8, 9, 12, 21, 23, 40, 61]
except:
  AssertionError('Testcase does not work properly')
