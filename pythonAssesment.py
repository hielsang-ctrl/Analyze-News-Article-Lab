def count_specific_word(text: str, word: str) -> int:
    return text.lower().split().count(word.lower())


sample_text = "The quick brown fox jumps over the lazy dog. The dog barked."
search_word = "the"

count = count_specific_word(sample_text, search_word)
print(f'The word "{search_word}" appears {count} time(s).')
