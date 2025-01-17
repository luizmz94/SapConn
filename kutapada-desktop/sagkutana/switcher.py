""" Module for text Switcher / decryption """

class Switcher:
    """ Simple class to encrypt / decrypt values """

    _DECRPYTED = "1234567890qwertyuopasdfghjklizxcvbnm*-,.<é!'^+%&/()=?_';>:QWERTYUIOPASDFGHJKLZXCVBNM" # pylint: disable=C0301
    _ENCRYPTED = "DH8G+.(YgJMx-6P:%)^sr>&<ob5f_wNKyiXRC7eIz!V4Z3EcjWnOa2?LmA/kpB'QlU=u;9Dh0T'SFdqé1t,v" # pylint: disable=C0301

    @staticmethod
    def decrypt_text(text: str) -> str:
        """ Hidden -> regular text """
        return Switcher._get_replaced_string(text, Switcher._DECRPYTED, Switcher._ENCRYPTED)

    @staticmethod
    def encrypt_text(text: str) -> str:
        """ Regular -> hidden text """
        return Switcher._get_replaced_string(text, Switcher._ENCRYPTED, Switcher._DECRPYTED)

    @staticmethod
    def _get_replacement_char(original_char: str, source_array: str, target_array: str) -> str:
        pos = source_array.find(original_char)
        if pos <= 0:
            return original_char
        return target_array[pos]

    @staticmethod
    def _get_replaced_string(original_string: str, source_array: str, target_array: str) -> str:
        output = ""
        for original_char in original_string:
            output += Switcher._get_replacement_char(original_char, source_array, target_array)
        return output
