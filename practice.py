"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # First check if list is empty.
    if words == []:
        return []

    # Convert the list of words to a set in order to remove the duplicates.
    word_set = set(words)

    # Convert the set back into a list (desired format).
    no_dup_word_list = list(word_set)

    return no_dup_word_list


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # Convert the two lists into sets, find the intersection, and convert back
    # to a list.  If one or both lists is empty, an empty set will be returned.
    unique_common_items_list = list(set(items1) & set(items2))

    return unique_common_items_list

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    zero_sum_pairs = []

    list_length = len(numbers)

    # first_num = 0
    # last_num = list_length - 1

    # for number in numbers:
    #     if numbers[first_num] + numbers[last_num] == 0:
    #         zero_sum_pairs.append((numbers[first_num], numbers[last_num]))
    #         first_num += 1
    #         last_num -= 1

    # If 0 is in the list, add a (0, 0) pair
    for number in numbers:
        if number == 0:
            zero_sum_pairs.append((0, 0))

    # Sort the numbers and check if sums equal 0.
    sorted_numbers = sorted(numbers)
    for i in range(list_length/2):
        for j in range(i, list_length):
            if sorted_numbers[i] + sorted_numbers[j] == 0:
                zero_sum_pairs.append((sorted_numbers[i], sorted_numbers[j]))

    # Convert the list to a set to remove duplicates, then back to list.
    zero_sum_pairs = list(set(zero_sum_pairs))
    return sorted(zero_sum_pairs)


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # Create an empty dictionary to store the characters and their frequencies.
    char_dict = {}

    # Remove the spaces.
    char_str = phrase.replace(" ", "")
    
    for char in char_str:
        char_dict[char] = char_dict.get(char, 0) + 1

    # Create a list of sorted values to determine maximum value.
    char_count_list = sorted(char_dict.values())
    max_char_count = max(char_count_list)

    # Use list comprehension to make final list of key(s) that equal the max value.
    final_list = [key for key in char_dict if char_dict[key] == max_char_count]


    return final_list

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
