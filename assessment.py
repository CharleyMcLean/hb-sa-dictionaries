"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # Create an empty dictionary to hold the words and their frequencies.
    word_dict = {}

    # Create a list of words in the phrase (including duplicates).
    line_words = phrase.split(" ")

    for word in line_words:
        word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # Create a dictionary containing the melon names and their prices.
    melon_dict = {"Watermelon": 2.95,
                    "Cantaloupe": 2.50,
                    "Musk": 3.25,
                    "Christmas": 14.25}

    # Return a statement if melon is not in the dictionary.
    # Return the melon price if it is in the dictionary.
    if melon_name not in melon_dict:
        return 'No price found'
    else:
        return melon_dict[melon_name]



def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    # Create an empty dictionary to contain the word lengths and words.
    word_length_dict = {}

    # Add word lengths and their corresponding words to a dictionary.
    for word in words:
        word_length = len(word)
        if word_length not in word_length_dict:
            word_length_dict[word_length] = [word]
        else:
            word_length_dict[word_length].append(word)


    word_length_tuples = word_length_dict.items()

    final_list = []
    for tuples in word_length_tuples:
        final_list.append((tuples[0], sorted(tuples[1])))

    return final_list


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_to_pirate_dict = {"sir": "matey",
                                "hotel": "fleabag inn",
                                "student": "swabbie",
                                "man": "matey",
                                "professor": "foul blaggart",
                                "restaurant": "galley",
                                "your": "yer",
                                "excuse": "arr",
                                "students": "swabbies",
                                "are": "be",
                                "restroom": "head",
                                "my": "me",
                                "is": "be"}


    # Create a list of words in the phrase.
    engl_words = phrase.split(" ")


    # Create a list of pirate words
    pirate_words = []
    for word in engl_words:
        if word not in english_to_pirate_dict:
            pirate_words.append(word)
        else:
            pirate_words.append(english_to_pirate_dict[word])


    # Create empty string to hold pirate translation.
    # Could have skipped this step and just returned " ".join(pirate_words),
    # but set a variable to make it clear what we are returning.
    pirate_phrase = " ".join(pirate_words)

    return pirate_phrase


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Create the game list and add the first word from the names list.
    game_list = [names[0]]
    # Delete that word from the names list so it cannot be reused.
    del names[0]

    names_dict = {name:name[0] for name in names}

    # Next first letter is last letter of last word in generated game list.
    for i in range(len(names)):

        # Next first letter is last letter of last word in generated game list.
        next_first_letter = game_list[-1][-1]
        
        # List of words that meet the criteria.  Use dictionary to check.
        possible_next_words = [name for name in names if names_dict[name] == next_first_letter]
        
        # Return the final game list if no words match the criteria.
        if possible_next_words == []:
            return game_list

        # Append the first avaiable word to the game list and remove it from
        # the original names list.
        game_list.append(possible_next_words[0])
        names.remove(possible_next_words[0])

    return game_list

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
