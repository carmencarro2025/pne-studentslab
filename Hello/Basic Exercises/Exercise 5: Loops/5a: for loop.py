def word_length(words):
    for word in words:
        print(f"{word} -> {len(word)} characters")


if __name__ == "__main__":

    words = ["Python", "is", "a", "programming", "language"]

    word_length(words)


