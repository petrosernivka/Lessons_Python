def longest_palindrome (s):
    
    if len(s) < 2:
        return len(s)
        
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            if s[j:i + j] == s[j:i + j][::-1]:
                return i
