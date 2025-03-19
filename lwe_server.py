import socket
import numpy as np
import pickle  # To serialize and send objects

# Parameters
n = 10       # Dimension of the secret vector
q = 97       # Modulus
sigma = 2.0  # Noise standard deviation

# Key Generation
def keygen():
    A = np.random.randint(0, q, size=(n, n))  # Public matrix A
    s = np.random.randint(0, 2, size=(n, 1))  # Secret key (binary vector)
    e = np.random.normal(0, sigma, size=(n, 1)).astype(int) % q  # Small noise
    b = (np.dot(A, s) + e) % q  # Compute public key part
    return A, b, s

# Decryption Function
def decrypt(A, s, x, c):
    """ Decrypts the ciphertext back to 0 or 1 """
    decrypted_value = (c - np.dot(x.T, np.dot(A, s))) % q
    return int(np.abs(decrypted_value - q // 2) < q // 4)

# Server Setup
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

A, b, s = keygen()  # Generate keys

print("\n=== Server Started ===")
print("Public Key (A):\n", A)
print("\nPublic Key (b):\n", b)
print("\nSecret Key (s):\n", s)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("\nServer is listening for connections...")

    conn, addr = server.accept()
    with conn:
        print("\nConnected to:", addr)
        
        # Send public keys to client
        conn.sendall(pickle.dumps((A, b)))

        # Receive encrypted data
        encrypted_data = pickle.loads(conn.recv(4096))
        x, c = encrypted_data

        print("\nReceived Ciphertext (c):", c)
        print("Received Random Vector (x):\n", x)

        # Decrypt Message
        decrypted_message = decrypt(A, s, x, c)

        print("\nDecrypted Message:", decrypted_message)

        # Send acknowledgment
        conn.sendall(pickle.dumps(decrypted_message))

