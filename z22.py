import os
from tqdm import tqdm

#  ЗАДАНИЕ 22
def read_reverse(filepath):

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in reversed(lines):
        print(line.strip())


# ---------- ПРИМЕР ----------
if __name__ == "__main__":

    file_path = input("Введите путь к файлу для чтения: ").strip()
    print("\n=== Задание 22 ===")
    read_reverse(file_path)

