#!/usr/bin/env python3
import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"[*] UDP Server listening on {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
