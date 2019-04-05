"""
molssi_math.py
sample project for molssi workshop

Some math functions.
"""
def mean(num_list):
    """
    calculate mean/average from a list of numbers.
    
    Parameters
    -----------
    num_list : list
        The list to take the average of

    Returns
    -----------
    mean_list : float
        The mean of the list
    """

    mean_n=0
    for i in range(len(num_list)):
        mean_n+=num_list[i]

    print("You're dumb")

    return mean_n/len(num_list)

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
