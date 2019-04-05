"""
strin_util.py
A sample repo for MolSSI workshop

Misc. string processing functions
"""

import warnings


def title_case(sentence):
    """Convert a string to title case.
    Parameters
    -----------
    sentence : string
        string to be converted to title case

    Returns
    ----------
    title_case_sentence : string
        String converted to title case

    Example
    ----------
    >>> title_case('ThIS iS  a StrInG to BE ConVerTed.')
        'This Is A String To Be Converted.'
    """

    #check that input is string
    if not isinstance(sentence, str):
        raise TypeError('Invalid input %s - Input type must be type string' % (sentence))
    
    if sentence=='':
        warnings.warn('Input %s is empty' % (sentence))

    sent = sentence.split()
    title_case_sentence = ''
    for word_ind in range(len(sent)):
        for char_ind in range(len(sent[word_ind])):
            if char_ind == 0:
                title_case_sentence += sent[word_ind][char_ind].upper()
            else:
                title_case_sentence += sent[word_ind][char_ind].lower()
        if word_ind != len(sent) - 1:
            title_case_sentence += ' '
    return title_case_sentence
