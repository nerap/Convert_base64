"""

    Convert a string entered by the user in ascii form to base64 form

"""


def get_user_input():
    """Recover the user's input

    Returns: user_input
    """
    user_input = input("Enter a string")
    return user_input


def convert_string_to_list(string_user):
    """Convert a string in a list

    Args:
       string_user : The string to convert into a list
    Returns: a list
    """
    list_character = []
    for element in string_user:
        list_character += element
    return list_character


def convert_list_element_to_ascii_integer(list_character):
    """Convert the list's element into integer ascii

    Args:
       list_character : The list of character to convert into a ascii integer
    Returns: a list of integer
    """

    list_ascii = []
    for element in list_character:
        list_ascii += [ord(element)]
    return list_ascii


def convert_list_of_integer_to_string_binary(list_ascii):
    """Convert the list's element into binary

    Args:
       list_ascii : the list of ascii to convert into binary
    Returns: a list of binary
    """

    list_convert_binary = []
    for element in list_ascii:
        list_convert_binary.append(bin(element)[2:])
    return list_convert_binary


def justify_binary_to_8_bits(list_binaries):

    """
        The function justify a list of binaries to 8 bits by adding 0 on the left hand side
         Args :
            A list of binaries as string
        Returns :
            A list where each element is 8 bits
    """

    list_8_bit = []

    for element in list_binaries:
        if len(element) < 8:
            while len(element) < 8:
                element = "0" + element
            list_8_bit.append(element)
        else:
            list_8_bit.append(element)

    return list_8_bit


def concat_list_element(list_8_bit):

    """
           The function concat all element of a list of 8 bit binaries as a unique string
            Args :
                A list of binaries where each element got a length of 8 as string
           Returns :
               A string with all elements concat as a string
    """
    concat_string = ""

    for element in list_8_bit:
        concat_string = concat_string + element

    return concat_string


def split_strings_into_six_bits_elements(concat_string):

    """
            The function split the string into a list where each element has a length of 6, except the last element
            if the string length is not a multiple of 6
             Args :
                 A string in binaries with a length multiple of 8 as string
            Returns :
                A list with the string converted as a list
    """

    list_bloc_6_bit = []

    temp_str = ""

    for i in range(0, len(concat_string)):
        if i % 6 == 0 and i != 0:
            list_bloc_6_bit.append(temp_str)
            temp_str = ""

        temp_str = temp_str + concat_string[i]

    if len(temp_str) != 0:
        list_bloc_6_bit.append(temp_str)

    return list_bloc_6_bit


def justify_last_element_to_6_bit(list_bloc_6_bit):

    """
            Justify the last element to 6 bit, only it's this element has not a length of 6
             Args :
                A list of 6 bit binaries with a last element tht might be not on 6 bit
             Returns :
                A list of the split string as a string with a length of 6, each element as a length of 6 if possible,
                The last element will contains the rest
    """

    string = list_bloc_6_bit[-1]

    while len(string) < 6:
        string = string + "0"

    list_bloc_6_bit[-1] = string
    return list_bloc_6_bit


def convert_binaries_to_decimal(list_6_bit):
    """
            Convert a list of binaries to a list of integers
             Args :
                A list of 6 bit binaries as string
             Returns :
                A list with all element of the list converted
    """

    def bin_to_dec(element):

        result = 0

        for i in range(0, len(element) - 1):
            if element[(len(element) - 1) - i] == "1":
                result += 2 ** i
        return result

    list_integers = []
    for elem in list_6_bit:
        list_integers.append(bin_to_dec(elem))

    return list_integers


def convert_integer_to_base64(tab1):
    """convert integer to base 64

    Args:
       list of integer: list of integer to convert into base 64
    Returns: list of string
    """

    base64t = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+",
               "/"]

    tab1_convert = []

    for i in tab1:
        tab1_convert.append(base64t[i])
    return tab1_convert


def convert_list_to_string(tab1_convert):
    """convert the list to string

    Args:
        The list of string to convert into string
    Returns: string
    """

    tab1_convert_to_string = "".join(tab1_convert)
    return tab1_convert_to_string


def justify_string_to_multiple_of_four(tab1_convert_to_string):
    """justify string to multiple of four

    Args:
        String to convert into string with a lenght of four's multiple
    Returns: string with a lenght of four's multiple
    """

    while len(tab1_convert_to_string) % 4 != 0:
        tab1_convert_to_string += "="
    return tab1_convert_to_string


if __name__ == "__main__":

    temp = get_user_input()
    print(temp)
    temp = convert_string_to_list(temp)
    print(temp)
    temp = convert_list_element_to_ascii_integer(temp)
    print(temp)
    temp = convert_list_of_integer_to_string_binary(temp)
    print(temp)
    temp = justify_binary_to_8_bits(temp)
    print(temp)
    temp = concat_list_element(temp)
    print(temp)
    temp = split_strings_into_six_bits_elements(temp)
    print(temp)
    temp = justify_last_element_to_6_bit(temp)
    print(temp)
    temp = convert_binaries_to_decimal(temp)
    print(temp)
    temp = convert_integer_to_base64(temp)
    print(temp)
    temp = convert_list_to_string(temp)
    print(temp)
    temp = justify_string_to_multiple_of_four(temp)

    print(temp)
