def longest_palindrome(s):
    longest = ""
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if substring == substring[::-1]:  
                if len(substring) > len(longest):
                    longest = substring
    return longest

print(longest_palindrome("babad"))  
print(longest_palindrome("cbbd"))    
print(longest_palindrome("racecar")) 