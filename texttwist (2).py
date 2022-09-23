def test_word(word, letters):
    for each_letter in word:
        try:
            letters.remove(each_letter)
        except ValueError:
            return False
    return True
