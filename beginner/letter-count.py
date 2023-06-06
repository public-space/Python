
# * Counts How many times a letter is in a word

def letter_count(word, letter): 
    count = 0
    for char in word: 
        if char == letter:
            count += 1
            return count

how_may = letter_count('banana', 'a')
print(f"there are {how_may} a's in banana")