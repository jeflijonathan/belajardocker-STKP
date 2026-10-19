# perhitungan_konkarensi.py

import multiprocessing
import time
import psutil


# =========================
# DATA
# =========================

angka = [1, 2, 3, 4, 5, 6]


# =========================
# TUGAS A
# =========================

def tugas_a(data, queue):

    # Membatasi Tugas A menggunakan Core 0
    proses = psutil.Process()
    proses.cpu_affinity([0])

    hasil = 0

    for angka in data:

        kuadrat = angka * angka
        hasil += kuadrat

        print(
            f"Tugas A menghitung angka {angka} "
            f"-> {angka} * {angka} = {kuadrat} "
            f"(Core 0)",
            flush=True
        )

        time.sleep(1)

    queue.put(hasil)


# =========================
# TUGAS B
# =========================

def tugas_b(data, queue):

    # Membatasi Tugas B menggunakan Core 0
    proses = psutil.Process()
    proses.cpu_affinity([0])

    hasil = 0

    for angka in data:

        kuadrat = angka * angka
        hasil += kuadrat

        print(
            f"Tugas B menghitung angka {angka} "
            f"-> {angka} * {angka} = {kuadrat} "
            f"(Core 0)",
            flush=True
        )

        time.sleep(1)

    queue.put(hasil)


# =========================
# PROGRAM UTAMA
# =========================

if __name__ == "__main__":

    print("=== PERHITUNGAN KUADRAT KONKURENSI ===")
    print(f"Data = {angka}")
    print("CPU yang digunakan = 1 Core")
    print("Core yang digunakan = Core 0")
    print()

    # =========================
    # PEMBAGIAN DATA
    # =========================

    # Tugas A menghitung angka ganjil
    data_a = [1, 3, 5]

    # Tugas B menghitung angka genap
    data_b = [2, 4, 6]

    print(f"Tugas A = {data_a}")
    print(f"Tugas B = {data_b}")
    print()

    # =========================
    # QUEUE
    # =========================

    queue = multiprocessing.Queue()

    # =========================
    # MEMBUAT PROSES
    # =========================

    proses_a = multiprocessing.Process(
        target=tugas_a,
        args=(data_a, queue)
    )

    proses_b = multiprocessing.Process(
        target=tugas_b,
        args=(data_b, queue)
    )

    # =========================
    # MENJALANKAN PROSES
    # =========================

    print("=== PROSES DIMULAI ===")
    print()

    proses_a.start()
    proses_b.start()

    # =========================
    # MENUNGGU PROSES SELESAI
    # =========================

    proses_a.join()
    proses_b.join()

    # =========================
    # MENGAMBIL HASIL
    # =========================

    hasil_a = queue.get()
    hasil_b = queue.get()

    # =========================
    # HASIL AKHIR
    # =========================

    hasil = hasil_a + hasil_b

    print()
    print("=== HASIL AKHIR ===")
    print(f"Hasil Tugas A = {hasil_a}")
    print(f"Hasil Tugas B = {hasil_b}")
    print(f"Hasil = {hasil}")