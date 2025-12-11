#!/usr/bin/env python3
import random

def random_caps(word: str) -> str:
    """Ubah tiap huruf jadi random upper/lower dari kata input."""
    return "".join(
        ch.upper() if random.random() > 0.5 else ch.lower()
        for ch in word
    )

def duplicate_random_char(word: str) -> str:
    """Duplikasi 1 huruf random jadi 2–3 kali."""
    if len(word) == 0:
        return word
    idx = random.randint(0, len(word) - 1)
    repeat = random.randint(2, 3)
    return word[:idx] + word[idx] * repeat + word[idx+1:]

def write_one(w, f, seen):
    """Tulis ke file + print ke layar, hindari duplikat."""
    if w in seen:
        return
    seen.add(w)
    f.write(w + "\n")
    print(w)

def duplicate_and_caps(word):
    """Double huruf lalu acak kapitalisasinya."""
    # pilih huruf random buat di-double
    idx = random.randint(0, len(word) - 1)
    repeated = word[idx] * random.randint(2, 3)
    doubled = word[:idx] + repeated + word[idx+1:]
    # acak kapitalisasi hasil doubled
    return "".join(
        ch.upper() if random.random() > 0.5 else ch.lower()
        for ch in doubled
    )

def main():
    print("=== WORDLIST-GENERATOR ===")
    base = input("Input kata dasar: ").strip()
    if not base:
        print("Kata kosong bang, mau ngelist apa 😅")
        return

    out_name = input("Nama file output (default: wordlist.txt): ").strip() or "wordlist.txt"

    # berapa banyak variasi kapitalisasi & double huruf
    CAPS_VARIANTS = 30
    DUP_VARIANTS = 30

    # KUMPULIN VARIASI
    caps_set = set()
    dup_set = set()

    # kapitalisasi acak
    for _ in range(CAPS_VARIANTS):
        caps_set.add(random_caps(base))

   # double huruf + kapitalisasi acak
    dup_caps_set = set()
    for _ in range(30):
        dup_caps_set.add(duplicate_and_caps(base))
    dup_caps_list = list(dup_caps_set)

    # double huruf
    for _ in range(DUP_VARIANTS):
        dup_set.add(duplicate_random_char(base))

    caps_list = list(caps_set)
    dup_list = list(dup_set)

    print("\nGenerating wordlist...\n")

    seen = set()
    total = 0

    with open(out_name, "w", encoding="utf-8") as f:
        # 1) base normal (tanpa angka)
        write_one(base, f, seen)
        total += 1

        # 2) semua kapitalisasi acak (tanpa angka)
        for w in caps_list:
            before = len(seen)
            write_one(w, f, seen)
            if len(seen) > before:
                total += 1

        # 3) semua double huruf (tanpa angka)
        for w in dup_list:
            before = len(seen)
            write_one(w, f, seen)
            if len(seen) > before:
                total += 1
       # 3b) double huruf + kapitalisasi acak (tanpa angka)
        for w in dup_caps_list:
            before = len(seen)
            write_one(w, f, seen)
            if len(seen) > before:
                total += 1

        # 4) base normal + angka 1–999
        for i in range(1, 1000):
            w = f"{base}{i}"
            before = len(seen)
            write_one(w, f, seen)
            if len(seen) > before:
                total += 1
         # 4b) base normal + angka 000–999
        for i in range(0, 1000):
            w = f"{base}{str(i).zfill(3)}"
            before = len(seen)
            write_one(w, f, seen)
            if len(seen) > before:
                total += 1

        # 5) kapitalisasi acak + angka 1–999
        for base_var in caps_list:
            for i in range(1, 1000):
                w = f"{base_var}{i}"
                before = len(seen)
                write_one(w, f, seen)
                if len(seen) > before:
                    total += 1
# 5b) kapitalisasi acak + angka 000–999
        for base_var in caps_list:
            for i in range(0, 1000):
                w = f"{base_var}{str(i).zfill(3)}"
                before = len(seen)
                write_one(w, f, seen)
                if len(seen) > before:
                    total += 1

        # 6) double huruf + angka 1–999
        for base_var in dup_list:
            for i in range(1, 1000):
                w = f"{base_var}{i}"
                before = len(seen)
                write_one(w, f, seen)
                if len(seen) > before:
                    total += 1
# 6b) double huruf + angka 000–999
        for base_var in dup_list:
            for i in range(0, 1000):
                w = f"{base_var}{str(i).zfill(3)}"
                before = len(seen)
                write_one(w, f, seen)
                if len(seen) > before:
                    total += 1
# 7) double huruf + kapitalisasi acak + angka 1–999
        for base_var in dup_caps_list:
            for i in range(1, 1000):
                w = f"{base_var}{i}"
                before = len(seen)
                write_one(w, f, seen)
                if len(seen) > before:
                    total += 1
# 7b) double huruf + kapitalisasi acak + angka 000–999
        for base_var in dup_caps_list:
            for i in range(0, 1000):
                w = f"{base_var}{str(i).zfill(3)}"
                before = len(seen)
                write_one(w, f, seen)
                if len(seen) > before:
                    total += 1

    print("\nSelesai!")
    print(f"Total word unik: {total}")
    print(f"Disimpan di: {out_name}")

if __name__ == "__main__":
    main()
