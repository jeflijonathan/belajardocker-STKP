from xmlrpc.server import SimpleXMLRPCServer

database_rekening = {
    "12345": 5500000,
    "67890": 1250000
}

def cek_saldo(nomor_rekening):
    return database_rekening.get(str(nomor_rekening), "Rekening tidak ditemukan")

def tabung(nomor_rekening, jumlah):
    no_rek = str(nomor_rekening)
    if no_rek in database_rekening:
        # Tambahkan saldo
        database_rekening[no_rek] += jumlah
        return f"Berhasil menabung Rp {jumlah:,}. Saldo terkini: Rp {database_rekening[no_rek]:,}"
    else:
        return "Rekening tidak ditemukan"

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Server Bank RPC berjalan di port 8000...")

server.register_function(cek_saldo, "cek_saldo")
server.register_function(tabung, "tabung")

# Jalankan server
server.serve_forever()