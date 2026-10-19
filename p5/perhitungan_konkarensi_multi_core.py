import multiprocessing
import time
import psutil

angka = [1, 2, 3, 4]


def tugas_a(data, queue):
    # Core 1
    proses = psutil.Process()
    proses.cpu_affinity([0])

    hasil = 0

    for angka in data:
        kuadrat = angka * angka
        hasil += kuadrat

        print(
            f"Tugas A menghitung angka {angka} "
            f"-> {angka} * {angka} = {kuadrat} "
            f"(Core 1)",
            flush=True
        )

        time.sleep(1)

    queue.put(("A", hasil))


def tugas_b(data, queue):
    # Core 2
    proses = psutil.Process()
    proses.cpu_affinity([1])

    hasil = 0

    for angka in data:
        kuadrat = angka * angka
        hasil += kuadrat

        print(
            f"Tugas B menghitung angka {angka} "
            f"-> {angka} * {angka} = {kuadrat} "
            f"(Core 2)",
            flush=True
        )

        time.sleep(1)

    queue.put(("B", hasil))


if __name__ == "__main__":

    print("=== PERHITUNGAN KUADRAT MULTI-CORE ===")
    print(f"Data = {angka}")

    jumlah_core = multiprocessing.cpu_count()
    print(f"Jumlah CPU/Core tersedia = {jumlah_core}")

    print("Core yang digunakan = Core 1 dan Core 2")
    print()

    # Pembagian otomatis:
    # index 0, 2, 4, 6, ... -> Tugas A
    # index 1, 3, 5, 7, ... -> Tugas B
    data_a = angka[0::2]
    data_b = angka[1::2]

    print("Pembagian tugas:")
    print(f"Tugas A = {data_a} -> Core 1")
    print(f"Tugas B = {data_b} -> Core 2")
    print()

    queue = multiprocessing.Queue()

    proses_a = multiprocessing.Process(
        target=tugas_a,
        args=(data_a, queue)
    )

    proses_b = multiprocessing.Process(
        target=tugas_b,
        args=(data_b, queue)
    )

    print("=== PROSES DIMULAI ===")
    print()

    waktu_mulai = time.time()

    proses_a.start()
    proses_b.start()

    proses_a.join()
    proses_b.join()

    waktu_selesai = time.time()

    hasil_a = 0
    hasil_b = 0

    for _ in range(2):
        nama_tugas, hasil = queue.get()

        if nama_tugas == "A":
            hasil_a = hasil
        elif nama_tugas == "B":
            hasil_b = hasil

    hasil_akhir = hasil_a + hasil_b

    waktu = waktu_selesai - waktu_mulai

    print()
    print("=== HASIL AKHIR ===")
    print(f"Hasil Tugas A = {hasil_a}")
    print(f"Hasil Tugas B = {hasil_b}")
    print(f"Hasil = {hasil_akhir}")
    print(f"Waktu proses = {waktu:.2f} detik")