import sys
import socket
import time

mode = sys.argv[1]

if mode == 'server2':
    s = socket.socket()
    s.bind(('0.0.0.0', 5002))
    s.listen(1)
    print("Server 2 (Pajak) siap...")
    while True:
        conn, addr = s.accept()
        jumlah = float(conn.recv(1024).decode())
        pajak = jumlah * 0.15
        total = jumlah + pajak
        conn.send(f"{pajak},{total}".encode())
        conn.close()