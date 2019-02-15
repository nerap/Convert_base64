
"""

    Converting a list 8 bits binaries to a list of 6 bits


"""


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

    str = list_bloc_6_bit[-1]

    while len(str) < 6:
        str = "0" + str

    list_bloc_6_bit[-1] = str
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


if __name__ == "__main__":
    list = ["1000001", "1000010", "1000011", "1000100"]
    print(list)
    list = justify_binary_to_8_bits(list)
    print(list)
    list = concat_list_element(list)
    print(list)
    list = split_strings_into_six_bits_elements(list)
    print(list)
    list = justify_last_element_to_6_bit(list)
    print(list)
    list = convert_binaries_to_decimal(list)
    print(list)

    pass
