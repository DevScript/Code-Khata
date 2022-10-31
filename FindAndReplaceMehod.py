# replace() method
string="she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))

print(string.replace("is","was",1))    # To change only first is

# find() method: To find the index of a word or a character in a string
print(string.find("is"))
string="is she is beautiful and she is good dancer"
print(string.find("is"))

print(string.find("is",1))          # means start finding from index 1
string="she is beautiful and she is good dancer"

# If you want to search second 'is' but dont know its position then you will do like thiss
is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)
