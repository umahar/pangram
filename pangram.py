def is_pangram(sentence):
    alphabets ="qwertyuiopasdfghjklzxcvbnm"
    
    for index in alphabets:
        if index in sentence.lower():
            continue
        else:
            return False
    return True
    
    
print(is_pangram("The the lazy dog."))