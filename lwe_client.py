import socket
import numpy as np
import pickle  # To serialize and send objects

# Parameters
q = 97       # Modulus
sigma = 2.0  # Noise standard deviation
n = 10       # Dimension

# Encryption Function
def encrypt(A, b, message):
    """ Encrypts a bit (0 or 1) """
    x = np.random.randint(0, 2, size=(n, 1))  # Random binary vector
    noise = np.random.normal(0, sigma, 1).astype(int) % q  # Small noise
    c = (np.dot(x.T, b) + (message * q // 2) + noise) % q  # Ciphertext
    return x, c

# Client Setup
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to connect to

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    # Receive public keys from server
    A, b = pickle.loads(client.recv(4096))

    print("\n=== Client Connected ===")
    print("Received Public Key (A):\n", A)
    print("\nReceived Public Key (b):\n", b)

    message = int(input("\nEnter message to encrypt (0 or 1): "))  # User input
    x, c = encrypt(A, b, message)

    print("\nCiphertext (c):", c)
    print("Random Vector (x):\n", x)

    # Send encrypted data to server
    client.sendall(pickle.dumps((x, c)))

    # Receive acknowledgment
    decrypted_message = pickle.loads(client.recv(4096))
    print("\nServer Decrypted Message:", decrypted_message)