# import jwt
#
# key = "secret"
# encoded = jwt.encode({"some": "payload"}, key, algorithm="HS256")
# print(encoded)
# # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg
# # key = 'bb'
# decoded = jwt.decode(encoded, key, algorithms="HS256")
# print(decoded)
# # {'some': 'payload'}


import jwt

private_key = b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
public_key = b"-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEAC..."

encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256")
print(encoded)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg
decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
print(decoded)
# {'some': 'payload'}
