import pytest

def get_length_of_longest_substring(s):
    chars_to_index = {}
    current_min = 0
    current_max = 0
    ret = 0
    for index, char in enumerate(s):
        if char not in chars_to_index:
            chars_to_index[char] = index
        else:
            current_min = chars_to_index[char] + 1
            chars_to_index[char] = index
        current_max = index + 1
        ret = max(ret, current_max - current_min)
    
    return ret
        
            
@pytest.mark.parametrize("s, expected", [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('', 0),
    ('a', 1),
    ('abcdefghijklmnopqrstuvwxyz', 26),
    ('aA', 2)
    ])
def test_positive(s, expected):
    assert get_length_of_longest_substring(s) == expected
