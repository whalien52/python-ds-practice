def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1freq = {}
    num2freq = {}

    for char in str(num1):
        num1freq[char] = num1freq.get(char, 0) + 1
    
    for char in str(num2):
        num2freq[char] = num2freq.get(char, 0) + 1

    return num1freq == num2freq