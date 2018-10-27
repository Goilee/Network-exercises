import socket

HOST = 'enp4s0f2'
DST = '705A0FC16812'
SRC = 'BCEE7B22E0F0'
TYPE = '0842'

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
sock.bind( ('', 0) )
payload = 'FF' * 6 + DST * 16
packet = (DST + SRC + TYPE + payload).encode()
sock.send(packet)
