def counting_vowels(word):
    counter = 0
    any_vowel = "aeiouy"
    for letter in word.lower():
        if letter in any_vowel:
            counter +=1
    return counter
print(counting_vowels("Temirbek"))
#algorithm course, sudo code, 