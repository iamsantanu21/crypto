import random

def generate_private_key(prime):
    return random.randint(2, prime - 2)

def generate_public_key(private_key, prime, generator):
    return pow(generator, private_key, prime)

def compute_shared_secret(public_key, private_key, prime):
    return pow(public_key, private_key, prime)

prime = 23  
generator = 5  

# Alice's keys
alice_private_key = generate_private_key(prime)
alice_public_key = generate_public_key(alice_private_key, prime, generator)

# Bob's keys
bob_private_key = generate_private_key(prime)
bob_public_key = generate_public_key(bob_private_key, prime, generator)

# Exchange public keys and compute shared secrets
alice_shared_secret = compute_shared_secret(bob_public_key, alice_private_key, prime)
bob_shared_secret = compute_shared_secret(alice_public_key, bob_private_key, prime)

print("Alice's Private Key:", alice_private_key)
print("Alice's Public Key:", alice_public_key)
print("Bob's Private Key:", bob_private_key)
print("Bob's Public Key:", bob_public_key)
print("Alice's Shared Secret:", alice_shared_secret)
print("Bob's Shared Secret:", bob_shared_secret)