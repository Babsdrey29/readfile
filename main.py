from itertools import count

#FOLDER_PATH = /Users/drey/Desktop/story.txt

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./Users/drey/Desktop/story.txt", "r") as f:
        filename = f.read()

    return filename
filename = read_file_content("./Users/drey/Desktop/story.txt")
print(filename)

def count_words():
    text = read_file_content("./Users/drey/Desktop/story.txt")
    # [assignment] Add your code here
    count = dict()
    words = text.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(count_words())
