##Uni Directional Flow where client sends and server receives
##Server decrypts and prints the message
import socket
import random

def encrypt(msg, key):
    encrypted_msg = ''
    for c in msg:
        encrypted_msg += chr(ord(c) ^ key)
    return encrypted_msg

def decrypt(msg, key):
    decrypted_msg = ''
    for c in msg:
        decrypted_msg += chr(ord(c) ^ key)
    return decrypted_msg

HOST = '192.168.160.110'
PORT = 1552

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Generate random key
    key = random.randint(0, 255)
    print('Generated key:', key)
    # Send key to server
    s.sendall(str(key).encode('utf-8'))
    while True:
        msg = input('Enter message to send (type "quit" to exit): ')
        if msg == 'quit':
            break
        encrypted_msg = encrypt(msg, key)
        print('Encrypted message:', encrypted_msg)
        s.sendall(encrypted_msg.encode('utf-8'))
