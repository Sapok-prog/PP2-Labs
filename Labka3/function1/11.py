def palindrome(word):
    if(word == word[::-1]):
        return True
    return False

word = input()
print(palindrome(word))