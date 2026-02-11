if __name__ == "__main__":

    text = "  Hello, World! Welcome to Python Programming.  "
    text_stripped = text.strip("  ")
    print(f"Stripped: {text_stripped}")
    text_split = text_stripped.split(" ")
    print(f"Word count: {len(text_split)}")
    print(f"Title case: {text_stripped.title()}")
    print(f"Starts with Hello: {text_stripped.startswith('Hello')}")
    print(f"Ends with ing.: {text_stripped.endswith('ing')}")
    print(f"Python position: {text_stripped.find('Python')}")
    print(f"Joined: {' - '.join(text_split)}")