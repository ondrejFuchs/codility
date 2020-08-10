import random
import string

def solution(N):
    """ Function to generate string len = N, where letters (a-z) could by only in odd count.
    
    Args:
        N (int): The length of string to generate.

    Returns:
        str: String only with odd count of the same random letters in lowercase only.

    """
    generated_list = []
    i = 0
    while i < N:
        ch = random.choice(string.ascii_lowercase)
        if ch not in generated_list:
            generated_list += ch
        else:
            if i + 2 < N:
                generated_list += 2 * [ch]
                i += 1
            else:
                i -= 1
        i += 1
    return "".join(generated_list)
