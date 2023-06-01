import socket

def decrypt(msg, key):
    encrypted_msg = ''
    for c in msg:
        encrypted_msg += chr(ord(c) ^ key)
    return encrypted_msg

def encrypt(msg, key):
    decrypted_msg = ''
    for c in msg:
        decrypted_msg += chr(ord(c) ^ key)
    return decrypted_msg

HOST = '192.168.160.189'
PORT = 1552

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server listening on', (HOST, PORT))
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        with conn:
            # Receive key from client
            key = int(conn.recv(1024).decode('utf-8'))
            ###print('Received key:', key)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                msg = data.decode('utf-8')
                print('***********')
                print('Received:', msg)
                decrypted_msg = decrypt(msg, key)
                print('*************')
                print('Decrypted message:', decrypted_msg)

