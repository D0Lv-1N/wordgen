#!/usr/bin/env python3
import itertools
import random
import time

def random_caps(word):
    """Ubah tiap huruf jadi random uppercase/lowercase."""
    return ''.join(
        ch.upper() if random.random() > 0.5 else ch.lower()
        for ch in word
    )

def duplicate_random_char(word):
    """Duplikasi salah satu huruf random jadi 2–3 kali."""
    idx = random.randint(0, len(word) - 1)
    repeat = random.randint(2, 3)
    return word[:idx] + word[idx] * repeat + word[idx+1:]

def generate_numbers(base):
    """Base + angka 1–999."""
    for i in range(1, 1000):
        yield f"{base}{i}"

def main():
    print("=== MORPH WORDLIST GENERATOR ===")

    base = input("Input kata dasar: ").strip()
    output = input("Nama output file (default: morph.txt): ").strip() or "morph.txt"

    print("\nMulai proses morphing...\n")

    results = set()

    with open(output, "w", encoding="utf-8") as f:
        
        # variasi awal
        forms = set()
        forms.add(base.lower())
        forms.add(base.upper())
        forms.add(base.capitalize())

        # 30 variasi kapital acak
        for _ in range(30):
            forms.add(random_caps(base))

        # 30 variasi huruf double/triple
        for _ in range(30):
            forms.add(duplicate_random_char(base))

        # Tulis satu-satu + tampilkan prosesnya
        counter = 0
        for w in forms:
            if w not in results:
                results.add(w)
                f.write(w + "\n")
                print(w)
                counter += 1
                time.sleep(0.001)

            # generate angka 1–999
            for num in generate_numbers(w):
                combo = num
                if combo not in results:
                    results.add(combo)
                    f.write(combo + "\n")
                    print(combo)
                    counter += 1
                    # biar ga flooding terminal, sleep kecil
                    time.sleep(0.0001)

    print("\nSelesai cuy 🔥")
    print(f"Total word: {counter}")
    print(f"File saved → {output}")

if __name__ == "__main__":
    main()
