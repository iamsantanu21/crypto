import hashlib

text = input("Enter the text: ")
sha1 = hashlib.sha1()    
sha1.update(text.encode('utf-8'))
digest = sha1.hexdigest()
print(f"The SHA-1 digest of '{text}' is: {digest}")