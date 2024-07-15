def palindrome(text):
    text = text.replace(" ","").lower()

    for i in range(len(text) // 2):
        if (text[i] != text[- i - 1]):
            return False
        return text , True
    
print(palindrome("malayalam"))