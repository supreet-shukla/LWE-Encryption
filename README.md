### S U P R E E T   S H U K L A


# LWE Secure Communication over Sockets

This project demonstrates a Learning With Errors (LWE) encryption** scheme for secure communication between a client and a server using Python sockets. The client encrypts a message (0 or 1), sends it to the server, and the server decrypts it.

# Features
- LWE-based Encryption: Uses the LWE problem for secure communication.
- Client-Server Model: Communicates using Python sockets.
- Key Exchange: The server generates public-private keys and shares public keys with the client.
- Serialization: Uses `pickle` for transmitting complex objects over sockets.

---

# Installation & Setup

### Prerequisites
- Python 3.x installed
- Required libraries: `numpy`, `socket`, `pickle`


Step 1: Install Dependencies
pip install numpy

-------------------------------------------

# How to run this: 

Step 2: Run the Server
Open a terminal and start the server:
python3 lwe_server.py

Step 3: Run the Client
In another terminal, start the client:
python3 lwe_client.py



