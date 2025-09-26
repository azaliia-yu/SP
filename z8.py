import os


#  ЗАДАНИЕ 8
def find_duplicates(directory):
    files = {}
    duplicates = []

    for root, _, file_list in os.walk(directory):
        for file in file_list:
            path = os.path.join(root, file)
            try:
                with open(path, "rb") as f:
                    content = f.read()
            except:
                continue

            if content in files.values():
                duplicates.append(path)
            else:
                files[path] = content

    return duplicates


if __name__ == "__main__":

    path1 = input("Напишите путь к папке: ").strip()
    print(" Задание 8 ")
    print("Дубликаты:", find_duplicates(path1))









