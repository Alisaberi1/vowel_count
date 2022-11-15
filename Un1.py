"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
try:
    Word=input()
    def get_count(Word):
        count_a_number,count_e_number,count_i_number,count_o_number,count_u_number=Word.count("a"),Word.count("e"),Word.count("i"),Word.count("o"),Word.count("u")
        return(count_o_number + count_a_number + count_i_number + count_u_number + count_e_number )
    print(get_count(Word))
except EOFError as e:
    print(end="")
