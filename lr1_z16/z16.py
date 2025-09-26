import os
from tqdm import tqdm

def copy_with_progress(src: str, dst: str) -> None:
    try:
        size = os.path.getsize(src)
    except FileNotFoundError:
        print(f"Ошибка: файл '{src}' не найден.")
        return
    except OSError as e:
        print(f"Ошибка при доступе к файлу: {e}")
        return

    try:
        with open(src, "rb") as fsrc, open(dst, "wb") as fdst, tqdm(
            total=size, unit="B", unit_scale=True, desc="Копирование"
        ) as pbar:
            while byte := fsrc.read(1):
                fdst.write(byte)
                pbar.update(1)
        print(f"\nФайл успешно скопирован в '{dst}'")
    except OSError as e:
        print(f"Ошибка копирования: {e}")


if __name__ == "__main__":
    file_path = input("Введите путь к файлу для копирования: ").strip()

    print("\nЗадание 16")

    base, ext = os.path.splitext(file_path)
    dst_path = f"{base}_copy{ext}"

    copy_with_progress(file_path, dst_path)

