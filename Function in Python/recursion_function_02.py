def check_palindrome(string):
    length = len(string)
    if length <= 1:
        return 'yes'
    else:
        if string[0] == string[-1]:
            return check_palindrome(string[1:-1])
        else:
            return 'no'

            

print(check_palindrome('madam'))
print(check_palindrome('shubham'))
print(check_palindrome('m'))
print(check_palindrome('AABCCBAA'))
print(check_palindrome('AA'))