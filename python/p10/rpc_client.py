import xmlrpc.client

# Menghubungkan client ke server XML-RPC yang berjalan di localhost port 8000
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

no_rek = "12345"

print("--- 1. CEK SALDO AWAL ---")
print(f"Meminta pengecekan saldo untuk rekening: {no_rek}...")
hasil_saldo = proxy.cek_saldo(no_rek)
print(f"Hasil dari Server - Saldo Anda: Rp {hasil_saldo:,}\n")

print("--- 2. MELAKUKAN TRANSAKSI TABUNG ---")
jumlah_setoran = 500000
print(f"Menyetorkan uang sebesar Rp {jumlah_setoran:,} ke rekening {no_rek}...")
respon_tabung = proxy.tabung(no_rek, jumlah_setoran)
print(f"Hasil dari Server: {respon_tabung}\n")

print("--- 3. CEK SALDO AKHIR ---")
hasil_saldo_akhir = proxy.cek_saldo(no_rek)
print(f"Hasil dari Server - Saldo Terbaru: Rp {hasil_saldo_akhir:,}")