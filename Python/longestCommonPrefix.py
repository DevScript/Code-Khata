# Longest Common Prefix
def longestCommonPrefix(words): # Input: List of Strings
    if not words: # if words is empty
        return "" # return empty string
    if len(words) == 1: # if words has only one element
        return words[0] # return the element
    prefix = words[0] # set prefix to the first element
    for i in range(1, len(words)): # for each element in words
        while words[i].find(prefix) != 0: # while the element does not start with prefix
            prefix = prefix[:-1] # remove the last character of prefix
            if prefix == "": # if prefix is empty
                return "" # return empty string
    return prefix # Output: String of the longest common prefix

# Driver to test the function
print(longestCommonPrefix(["flower","flow","flight"])) # Output: "fl"
print(longestCommonPrefix(["dog","racecar","car"])) # Output: ""
print(longestCommonPrefix(["a"])) # Output: "a"
print(longestCommonPrefix(["aa","a"])) # Output: "a"
