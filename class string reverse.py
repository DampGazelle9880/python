class StringReverse():
    def reverse_words(string):
        words = string.split()
        reversed_words = words[::-1]
        return ''.join(reversed_words)
    
    
input_str = "Hi! I am Zohan!"
print(StringReverse.reverse_words(input_str))