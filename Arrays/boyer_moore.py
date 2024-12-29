def bad_character_heuristic(pattern):
    bad_char = [-1] * 256  # Untuk semua karakter ASCII
    for i, char in enumerate(pattern):
        bad_char[ord(char)] = i
    return bad_char

def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    bad_char = bad_character_heuristic(pattern)
    s = 0  # Shift untuk pola

    while s <= n - m:
        j = m - 1
        # Cocokkan pola dari belakang
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:  # Pola ditemukan
            return s
        else:
            # Pindahkan pola menggunakan tabel karakter buruk
            s += max(1, j - bad_char[ord(text[s + j])])
    return -1  # Pola tidak ditemukan

# Contoh Penggunaan
text = "ABAAABCD"
pattern = "ABC"
result = boyer_moore(text, pattern)
print(f"Pattern found at index: {result}")