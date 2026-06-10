import re
from collections import Counter

def count_specific_word(text, search_word):
    """
    Counts the number of occurrences of a specific word.
    Returns an integer.
    """
    words = re.findall(r'\b\w+\b', text.lower())

    count = 0

    for word in words:
        if word == search_word.lower():
            count += 1

    return count


def identify_most_common_word(text):
    """
    Identifies the most common word in the text.
    Returns the word as a string.
    Returns None for an empty string.
    """
    if text.strip() == "":
        return None

    words = re.findall(r'\b\w+\b', text.lower())

    if len(words) == 0:
        return None

    word_counts = Counter(words)

    return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    """
    Calculates the average word length.
    Returns a float.
    Returns 0 for an empty string.
    """
    words = re.findall(r'\b\w+\b', text)

    if len(words) == 0:
        return 0

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)


def count_paragraphs(text):
    """
    Counts paragraphs based on blank lines.
    Returns an integer.
    Returns 1 for an empty string.
    """
    if text.strip() == "":
        return 1

    paragraphs = [paragraph for paragraph in text.split("\n\n") if paragraph.strip()]

    return len(paragraphs)


def count_sentences(text):
    """
    Counts sentences based on periods, exclamation marks, and question marks.
    Returns an integer.
    Returns 1 for an empty string.
    """
    if text.strip() == "":
        return 1

    sentences = re.split(r'[.!?]+', text)

    count = 0

    for sentence in sentences:
        if sentence.strip():
            count += 1

    return count


# Read the news article from the text file
try:
    with open("news_article.txt", "r", encoding="utf-8") as file:
        article_text = file.read()

except FileNotFoundError:
    print("Error: news_article.txt was not found.")
    article_text = ""


if __name__ == "__main__":

    # While loop required by rubric
    while True:

        search_word = input(
            "\nEnter a word to search for (or type 'quit' to exit): "
        )

        # If/Else statement required by rubric
        if search_word.lower() == "quit":
            print("Program ended.")
            break

        else:
            specific_word_count = count_specific_word(
                article_text,
                search_word
            )

            most_common_word = identify_most_common_word(
                article_text
            )

            average_word_length = calculate_average_word_length(
                article_text
            )

            paragraph_count = count_paragraphs(
                article_text
            )

            sentence_count = count_sentences(
                article_text
            )

            print("\n===== NEWS ARTICLE ANALYSIS =====")
            print(f"Occurrences of '{search_word}': {specific_word_count}")
            print(f"Most common word: {most_common_word}")
            print(f"Average word length: {average_word_length:.2f}")
            print(f"Number of paragraphs: {paragraph_count}")
            print(f"Number of sentences: {sentence_count}")
