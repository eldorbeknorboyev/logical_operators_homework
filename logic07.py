def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return bool(a<0 or b<0)
print(main(-3,8))
print(main(4,1))