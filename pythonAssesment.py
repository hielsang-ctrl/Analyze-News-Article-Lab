from collections import Counter
import re


def count_specific_word(text: str, word: str) -> int:
    return text.lower().split().count(word.lower())


def identify_most_common_word(text: str) -> str | None:
    words = text.lower().split()
    return Counter(words).most_common(1)[0][0] if words else None


def calculate_average_word_length(text: str) -> float:
    words = [re.sub(r'[^a-zA-Z0-9]', '', w) for w in text.split()]
    words = [w for w in words if w]
    return sum(len(w) for w in words) / len(words) if words else 0


def count_paragraphs(text: str) -> int:
    paragraphs = [p for p in re.split(r'\n\s*\n', text) if p.strip()]
    return len(paragraphs) if paragraphs else 1


def count_sentences(text: str) -> int:
    sentences = re.findall(r'[^.!?]*[.!?]', text)
    return len(sentences) if sentences else 1


sample_text = "The quick brown fox jumps over the lazy dog. The dog barked."
search_word = "the"

count = count_specific_word(sample_text, search_word)
print(f'The word "{search_word}" appears {count} time(s).')

most_common = identify_most_common_word(sample_text)
print(f'The most common word is: "{most_common}".')

avg_length = calculate_average_word_length(sample_text)
print(f'The average word length is: {avg_length:.2f}.')

paragraph_count = count_paragraphs(sample_text)
print(f'The number of paragraphs is: {paragraph_count}.')

sentence_count = count_sentences(sample_text)
print(f'The number of sentences is: {sentence_count}.')
