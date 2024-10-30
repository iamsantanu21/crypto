import hashlib

text = input("Enter the text: ")
md5 = hashlib.md5()    
md5.update(text.encode('utf-8'))
digest = md5.hexdigest()
print(f"The MD-5 digest of '{text}' is: {digest}")