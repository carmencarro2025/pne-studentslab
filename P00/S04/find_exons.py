from pathlib import Path

FILENAME = "Sequences/ADA_EXONS.txt"

file_contents = Path(FILENAME).read_text()

print(file_contents)