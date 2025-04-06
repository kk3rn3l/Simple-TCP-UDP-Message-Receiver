#!/usr/bin/env python3
import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[*] TCP Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"[+] Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
