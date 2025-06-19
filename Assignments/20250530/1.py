"""
写一个程序找到文件中最长的英文单词。
"""


def find_longest_word(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            words = [word for word in content.split() if word.isalpha()]

            if not words:
                return ""

            longest_word = max(words, key=len)
            return longest_word
    except FileNotFoundError:
        return "Error: File not found"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    path = "./test1.txt"
    result = find_longest_word(path)
    print(f"The longest word is: {result}")
