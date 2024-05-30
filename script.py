import base64


original_string = "Hello, World!"
encoded_bytes = base64.b64encode(original_string.encode('utf-8'))
encoded_string = encoded_bytes.decode('utf-8')

print(f"Encoded: {encoded_string}")

decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
decoded_string = decoded_bytes.decode('utf-8')

print(f"Decoded: {decoded_string}")
