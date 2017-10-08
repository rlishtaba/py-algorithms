import re


class Challenges:
    @staticmethod
    def first_factorial(number: int) -> int:
        """
        Iterative approach

        :param number: an input, first factorial of a number
        :return: factorial
        """
        found = 1
        step = 2
        while step <= number:
            found *= step
            step += 1

        return found

    @staticmethod
    def longest_word(sentence: str) -> str:
        """
        Detect longest word in a sentence
        :param sentence:
        :return:
        """
        trimmed = re.compile('[^a-zA-Z0-9 ]').sub('', sentence)
        chunks = trimmed.split(' ')
        longest = 0
        index = -1
        for i, x in enumerate(chunks):
            if len(x) > longest:
                longest = len(x)
                index = i

        return chunks[index]

    @staticmethod
    def letter_mutation(string):
        """
        Coderbyte challenge: Letter Changes
        :param string: a sentence
        :return: str, transformed sentence
        """
        alphabet = list(range(97, 123))
        alphabet_len = len(alphabet) - 1
        ret = ''
        vowels = list('aeiou')

        for x in list(string):
            r = x
            if ord(x) in alphabet:
                if ord(x) == alphabet[alphabet_len]:
                    r = chr(alphabet[0])
                else:
                    r = chr(ord(x) + 1)
            if r in vowels:
                r = r.upper()
            ret += r

        return ret
