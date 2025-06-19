"""
写一个程序将一个字符串列表写入文件
"""


def write_strings_to_file(string_list, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for string in string_list:
                file.write(string + "\n")
        return "Strings written to file successfully"
    except FileNotFoundError:
        return "Error: Invalid directory or file path"
    except Exception as excpt:
        return f"Error: {str(excpt)}"


if __name__ == "__main__":
    strings = []
    while True:
        try:
            s = input()
            if s:
                strings.append(s)
            else:
                break
        except EOFError:
            break

    path = "./out1.txt"
    result = write_strings_to_file(strings, path)
    print(result)
