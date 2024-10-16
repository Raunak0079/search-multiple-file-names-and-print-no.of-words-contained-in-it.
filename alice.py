from pathlib import Path
path = Path("employee.txt")
def count_words(filename):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"sorry there is no file named {path}")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {path} had about {num_words} words.")
filenames = ["employee.txt","computerscience.txt","gandu.txt"]
for filename in filenames:
    path = Path(filename)
    count_words(path)
    
