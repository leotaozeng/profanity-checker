from profanity_check import predict


def read_file(path):
    try:
        # fin is a common name for a file object used for input
        with open(path, encoding="utf-8") as fin:
            contents_of_file = fin.read()
            return contents_of_file
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def check_profanity(content):
    return bool(predict([content])[0])


file = "/Users/leozeng/Codecademy/Computer Science/profanity-checker/files/good.txt"
output = check_profanity(read_file(file))

if output:
    print("Profanity detected!")
else:
    print("This document has no curse words!")
