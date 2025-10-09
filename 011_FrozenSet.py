fs1 = frozenset([1, 2, 3, 4, 5])
print(type(fs1), fs1)
# st = set()

# st.symmetric_difference_update

lst = [1, 2, ['a', 'b'], ['p', 'q']]
# st = {1, 2, {'a', 'b'}, {'p', 'q'}}
st = {1, 2, frozenset({'a', 'b'}), frozenset({'p', 'q'})}
print(st)