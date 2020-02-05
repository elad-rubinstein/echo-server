from threading import Thread
import socket


def accept1(socket, lst_of_clients):
    while True:
        obj, add = socket.accept()
        lst_of_clients.append(obj)


def recv(address, massage):
    massage = address.recv()


def send(lst_of_clients):
    for i in lst_of_clients:
        massage = b""
        thread = Thread(target=recv, args=(i, massage))


import socket
import select


def main():
    host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host.bind(("127.0.0.7", 1234))
    host.listen(2)
    lst = []
    all_connected_r = [host]

    while True:
        readable, writable, xable = select.select(all_connected_r, [], [])

        for r in readable:
            if r is host:
                all_connected_r.append(r.accept())
