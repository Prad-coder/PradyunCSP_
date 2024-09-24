string = "Brawl Stars is a fun game!"
string2 = "Tacocat"
print("String 1:")
length = len(string)
print(length)
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
print(count_vowels(string))
def average_word_length(input_string):
    words = input_string.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length
print(average_word_length(string))
def palindrome(input_string):
    string = input_string.replace(" ","").lower()
    return string == string[::-1]
print(palindrome(string))
print("String 2:")
length2 = len(string2)
print(length2)
print(count_vowels(string2))
print(average_word_length(string2))
print(palindrome(string2))