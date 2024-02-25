#(Integer Value of a Character) Here’s a peek ahead. In this chapter, you
#learned about strings. Each of a string’s characters has an integer
#representation. The set of characters a computer uses together with the
#characters’ integer representations is called that computer’s character set.
#You can indicate a character value in a program by enclosing that
#character in quotes, as in 'A'. To determine a character’s integer value,
#call the built-in function ord:
#In [1]: ord('A')
#Out[1]: 65
#Display the integer equivalents of B C D b c d 0 1 2 $ * + and
#the space character.


print(ord('B'), ord('C'), ord('D'), ord('b'), ord('c'), ord('d'), ord('0'), ord('1'), ord('2'), ord('$'), ord('*'), ord('+'), ord(' '))

#solution
#66 67 68 98 99 100 48 49 50 36 42 43 32
