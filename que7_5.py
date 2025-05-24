def is_palindrome(input_string):
    
    processed_string = ''.join(filter(str.isalnum, input_string)).lower()
    return processed_string == processed_string[::-1]