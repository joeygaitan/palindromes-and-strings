#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

def palindrome_parser(text):
    # lowers each alphabetical character
    text = text.lower()
    # loop over and only add in text letters from the string that a through z then resulting in a new string
    text = ''.join(letter for letter in text.lower() if 'a' <= letter <= 'z')

    return text


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


    if text == "":
        return True
    

    # lower all characters
    text = text.lower()
    # loop over and only add in text letters from the string that a through z then resulting in a new string
    text = ''.join(letter for letter in text.lower() if 'a' <= letter <= 'z')
    print(text)
    tail_index = len(text) - 1

    for index in range(len(text) // 2):
        print(index, tail_index)
        if text[index] == text[tail_index]:
            tail_index -= 1
        else:
            return False 
    return True

def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    
    if text == "":
        return True
    
    text = palindrome_parser(text)

    if left == None and right == None:
        left = 0
        right = len(text) - 1
    
    print(left,right,text[left],text[right])
    if text[left] == text[right] and right > (len(text) - 1) // 2:
        return is_palindrome_recursive(text, left+1,right-1)

    if text[left] != text[right]:
        return False

    if text[left] == text[right] and right == (len(text) - 1) // 2:
        return True

    
    

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()

    stuff = 'race fast safe car'
    print(is_palindrome_recursive('race fast safe car'))