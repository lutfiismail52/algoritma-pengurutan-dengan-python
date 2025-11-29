# Program Sorting dengan 3 Algoritma

def bubble_sort(data):
    """Algoritma Bubble Sort"""
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def insertion_sort(data):
    """Algoritma Insertion Sort"""
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

def selection_sort(data):
    """Algoritma Selection Sort"""
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

# Program Utama
print("=" * 50)
print("PROGRAM SORTING DATA")
print("=" * 50)

# Input data
print("\nMasukkan data yang ingin diurutkan")
print("(pisahkan dengan spasi, contoh: 5 2 8 1 9)")
input_data = input("Data: ")

# Konversi input menjadi list
try:
    data = [int(x) for x in input_data.split()]
except ValueError:
    # Jika bukan angka, gunakan sebagai string
    data = input_data.split()

print(f"\nData yang belum terurut: {data}")

# Menu pilihan
print("\n" + "=" * 50)
print("PILIH METODE SORTING:")
print("=" * 50)
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Selection Sort")
print("=" * 50)

pilihan = input("Masukkan pilihan (1/2/3): ")

# Proses sorting
data_copy = data.copy()

if pilihan == '1':
    print("\n>>> Menggunakan BUBBLE SORT <<<")
    hasil = bubble_sort(data_copy)
elif pilihan == '2':
    print("\n>>> Menggunakan INSERTION SORT <<<")
    hasil = insertion_sort(data_copy)
elif pilihan == '3':
    print("\n>>> Menggunakan SELECTION SORT <<<")
    hasil = selection_sort(data_copy)
else:
    print("\nPilihan tidak valid!")
    hasil = None

# Tampilkan hasil
if hasil:
    print(f"\nData yang sudah terurut: {hasil}")
    print("\n" + "=" * 50)
    print("SORTING SELESAI!")
    print("=" * 50)
