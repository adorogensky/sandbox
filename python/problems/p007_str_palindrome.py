def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] == ' ':
            i += 1
        elif s[j] == ' ':
            j -= 1
        elif s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1

    return True
    
