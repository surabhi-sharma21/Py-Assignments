input_string=input('Enter a string:')

s=len(input_string)

def reverse_string(input_string):
    return input_string[s+1::-1] #Starting from last s+1 move previous.....-1 step back!

def check_palindrome(input_string):
    reverse_str=reverse_string(input_string)
    if reverse_str == input_string :
        return True
    return False
return_value=check_palindrome(input_string)
if return_value == True:
    print('Entered string {0} is a palindrome string'.format(input_string))
else:
    print('Entered string {0} is not a palindrome string'.format(input_string))


