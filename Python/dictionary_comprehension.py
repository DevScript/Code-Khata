# Dictionary Comprehension
# squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
squares = {num:num**2 for num in range(1, 11)}
print(squares)

squares2 = {f'Square of {num} is':num**2 for num in range(1, 11)}
print(squares2)

for key,value in squares2.items():
    print(f'{key} : {value}')

# Count characters in word using Dictionary Comprehension
name = 'waqar'
word_count = {char:name.count(char) for char in name}
print(word_count)
