def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def quick_select(arr, l, r, k):
    if l <= r:
        pivot = partition(arr, l, r)
        if pivot == k - 1:  # Elemen ke-k ditemukan
            return arr[pivot]
        elif pivot > k - 1:  # Cari di bagian kiri
            return quick_select(arr, l, pivot - 1, k)
        else:  # Cari di bagian kanan
            return quick_select(arr, pivot + 1, r, k)
    return -1  # Jika k tidak valid

# Contoh Penggunaan
arr = [10, 4, 5, 8, 6, 11, 26]
k = 1
result = quick_select(arr, 0, len(arr) - 1, k)
print(f"Elemen ke-{k} terkecil adalah: {result}")