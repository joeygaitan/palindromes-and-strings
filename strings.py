#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    pattern_index = 0

    if pattern == "":
        return True

    for index in range(len(text)):
        print(text[index], index)
        if text[index] == pattern[pattern_index]:
            print(text[index], pattern[pattern_index],pattern_index,len(pattern))
            if pattern_index == len(pattern) - 1:
                return True
            pattern_index += 1
        else:
            pattern_index = 0

            if text[index] == pattern[pattern_index]:
            
                if pattern_index == len(pattern) - 1:
                    return True
                pattern_index += 1

    return False



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    pattern_index = 0
    index_array = []

    if pattern == "":
        return 0

    for index in range(len(text)):
        print(text, pattern, text[index], pattern_index, index)
        if text[index] == pattern[pattern_index]:
            index_array.append(index)
            if pattern_index == len(pattern) - 1:
                print("here")
                return index_array[0]
            pattern_index += 1
        else:
            pattern_index = 0
            index_array.clear()
            if text[index] == pattern[pattern_index]:
                index_array.append(index)
                if pattern_index == len(pattern) - 1:
                    return index_array[0]
                pattern_index += 1
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    pattern_index = 0
    intial_pattern_index = 0
    index_array = []

    if pattern == "":
        for i in range(len(text)):
            index_array.append(i)
        return index_array

    for index in range(len(text)):
        print(text, pattern, text[index], pattern[pattern_index], index, pattern_index, intial_pattern_index)
        if text[index] == pattern[pattern_index]:
            if text[index] == pattern[0] and pattern_index == 0:
                intial_pattern_index = index
            if pattern_index == len(pattern) - 1:
                index_array.append(intial_pattern_index)
                intial_pattern_index = index
                pattern_index = 0
                if pattern_index == len(pattern) - 1:
                    pass
                else:
                    pattern_index += 1
            else:
                pattern_index += 1
        else:
            pattern_index = 0
            if text[index] == pattern[pattern_index]:
                if text[index] == pattern[0]:
                    intial_pattern_index = index
                if pattern_index == len(pattern) - 1:
                    index_array.append(intial_pattern_index)
                    pattern_index = 0
                pattern_index += 1
    print (index_array)
    return index_array


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    print(find_all_indexes('aaa', 'aa'))