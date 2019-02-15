"""

    Converting a list 6 bits binaries to a list of 8 bits


"""


def unjustify_string_to_multiple_of_four(string_to_convert):
    """justify string to multiple of four

    Args:
        String to convert into string with a lenght of four's multiple
    Returns: string with a lenght of four's multiple
    """

    string_to_convert = string_to_convert[::-1]

    while string_to_convert[0] == "=":
        string_to_convert = string_to_convert[1:]

    return string_to_convert[::-1]


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


def convert_base64_to_integer(tab1):
    """convert base64 to integer

    Args:
       list of integer: list of base64 to convert into integer
    Returns: list of string
    """

    base64t = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+",
               "/"]

    tab1_convert = []

    for i in tab1:
        tab1_convert.append(base64t.index(i))
    return tab1_convert


def convert_list_of_integer_to_string_binary(list_ascii):
    """Convert the list's element into binary

    Args:
       list_ascii : the list of ascii to convert into binary
    Returns:
        a list of binary
    """

    list_convert_binary = []
    for element in list_ascii:
        list_convert_binary.append(bin(element)[2:])
    return list_convert_binary


def convert_dec_to_6_bit_bin(list_integer):
    """Convert a list of integers to a list of binaries in 6 bit
    Args :
        A list of integer
    Returns :
        A list of 6 bit binaries
    """

    def dec_bin_6_bit(elem):

        result_string = ""

        while elem > 0:
            result_string = str(elem % 2) + result_string
            elem = int(elem / 2)

        while len(result_string) < 6:
            result_string = "0" + result_string
        return result_string

    list_6_bit = []

    for element in list_integer:
        list_6_bit.append(dec_bin_6_bit(element))
    return list_6_bit


def justify_6_bit_element_to_8_bit(list_6_bit):
    """
        Convert the last element of the list to have a general multiple of 8 if needed
         Args :
            A list of 6 bit binaries as string
         Returns :
            The same list with a general length multiple of 8, only the last element will modified
    """

    def general_length(list_list):
        """Return the general length of the list
            Args :
                list_list : list of binaries
            Return:
                 Global length
          """
        length = 0
        for element in list_list:
            length = length + len(element)
        return length

    result_last_element = list_6_bit[-1]

    while general_length(list_6_bit) % 8 != 0:
        result_last_element = result_last_element[0:len(result_last_element) - 2]
        list_6_bit[-1] = result_last_element

    return list_6_bit


def concat_list_6_bit_element(list_6_bit):
    """
           The function concat all element of a list of 8 bit binaries as a unique string
            Args :
                A list of binaries where each element got a length of 6 as string
           Returns :
               A string with all elements concat as a string
    """
    concat_string = ""

    for element in list_6_bit:
        concat_string = concat_string + element

    return concat_string


def split_strings_into_8_bits_elements(concat_string):
    """
            The function split the string into a list where each element has a length of 6, except the last element
             if the string length is not a multiple of 8
             Args :
                A string in binaries with a length multiple of 8 as string
            Returns :
                A list, basically the same list, with the last argument modified if it was necessary

    """
    list_bloc_8_bit = []

    temp_str = ""

    for i in range(0, len(concat_string)):
        if i % 8 == 0 and i != 0:
            list_bloc_8_bit.append(temp_str)
            temp_str = ""

        temp_str = temp_str + concat_string[i]

    if len(temp_str) != 0:
        list_bloc_8_bit.append(temp_str)

    return list_bloc_8_bit


def supp_useless_0_in_8_bit(list_8_bit):
    """
         The function will erase every 0 before a 1 on left side of each element
             Args :
                A list with 8 bit binaries as string
            Returns :
                A list of binaries as string with without useless zero
    """
    list_result = []

    for element in list_8_bit:
        while element[0] == "0":
            element = element[1:len(element)]
        if element == "":
            element = "0"
        list_result.append(element)

    return list_result


def convert_binaries_to_decimal(list_8_bit):
    """

            Convert a list of binaries to a list of integers


             Args :

                A list of 8 bit binaries as list


             Returns :

                A list with all element of the list converted

    """

    def bin_to_dec(element):

        result = 0

        for i in range(0, len(element)):
            if element[(len(element) - 1) - i] == "1":
                result += 2 ** i
        return result

    list_integers = []
    for elem in list_8_bit:
        list_integers.append(bin_to_dec(elem))

    return list_integers


def convert_number_ascii(list_number):
    """Convert a number list to ascii list

    Args:
       list_number : A list of number to convert into a list
    Returns:
        list : of number
    """
    list_character = []
    for element in list_number:
        list_character.append(chr(element))
    return list_character


def concat_list_element(list_ascii):
    """
           The function concat all element of a list of ascii number as a unique string
            Args :
                A list of ascii char
           Returns :
               A string with all elements concat as a string
    """
    concat_string = ""

    for element in list_ascii:
        concat_string = concat_string + element

    return concat_string


if __name__ == "__main__":

    temp = input("String to convert :")
    print(temp)
    temp = unjustify_string_to_multiple_of_four(temp)
    print(temp)
    temp = convert_string_to_list(temp)
    print(temp)
    temp = convert_base64_to_integer(temp)
    print(temp)
    temp = convert_dec_to_6_bit_bin(temp)
    print(temp)
    temp = justify_6_bit_element_to_8_bit(temp)
    print(temp)
    temp = concat_list_element(temp)
    print(temp)
    temp = split_strings_into_8_bits_elements(temp)
    print(temp)
    temp = supp_useless_0_in_8_bit(temp)
    print(temp)
    temp = convert_binaries_to_decimal(temp)
    print(temp)
    temp = convert_number_ascii(temp)
    print(temp)
    temp = concat_list_element(temp)
    print(temp)

    pass
