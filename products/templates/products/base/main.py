# import base64
#
# encoded_text = "WgAERjp352Y3N2Lno7EGbv1VI578E5Jzf9Jbj5JX2N8Jg5IgF6LTEy4NEXDPIhC5L8VnxsngigXVUZ1I724E5AkR79It1E+hK7Jn6IYFHaJsolpLSOZOEoWUlV9NuwXDtizmgos4AsQgVxUNlFgyUoU7AhRTuGK6J6EF0JEhJhTrpEAslGIKF3L0YCeS5JLz7JAqcUEsDBBQACAgIAGEhd1JAAAAAAAAAAAAAAAASAAAAd2VyR751YW_541LpbmcueG1NpZNNTsMwEIVPwB0E7VskFSAUNe2ECjbs4VtKdsAqxbU7J4VIpe8JtC2VsT1IzaX5LtlD6Y8LUSvZ7IvMFL_762InrGRT536YB_24L/3IXVsciHE0IYA5JsJKi6NFyDkECO/DsmeqaDmHOiklxviJlghZI1JhSe9NNxtFVXN5JavhIK/5Ee0EozBj3Jzm0ExcYP9VGWPWAcPMNUEsHCEkTQ3VoAQAAPQUAAFBLAwQUAAgICABhIXdnxKCY0JJA647ERYUeMKd0IIEG7JX3YoH703EP87Eh5ARGE343YCPF4N8I6Ex5NuqNmJTiK4IXN817IMAAAAAAAA0A804NOcbLQAAAfiAAAAAEQAAAHdvcmQvc2Y0AGluE781JG1JpZXNbtS358JfYO8Y6A7Ao0I2IHV6J0LPuy2NXWOqc9YILT5N2ILhEjXO6YBKLGE247ESm0JsrZQQ4LzV1AsC550IESmhw7LA4A+ckT9NtGjGqRE593VhYCoaNH513YUihqophOv6YCDMD7JDyrHArqHSXjImh3JegpGS633Jm7EV5YxMC241YLHtsJ7VPQAjybYQfUGS4JXtJ8LW1NRA4LanSH+SP9IMTT8E/RV8AaLGMiVLlK1JtKASK8AkXaI/rz+W3IDCOpAEuJK0JGde4JR4EOv"
# decoded_bytes = base64.b64decode(encoded_text)
# print(decoded_bytes.decode('utf-8', errors='ignore'))



# import hashlib
#
# def hash_text(text):
#     return hashlib.sha1(text.encode()).hexdigest()
#
# sample_text = ("WgAERjp352Y3N2Lno7EGbv1VI578E5Jzf9Jbj5JX2N8Jg5IgF6LTEy4NEXDPIhC5L8VnxsngigXVUZ1I724E5"
#                "AkR79It1E+hK7Jn6IYFHaJsolpLSOZOEoWUlV9NuwXDtizmgos4AsQgVxUNlFgyUoU7AhRTuGK6J6EF0JEhJhTrpEA"
#                "slGIKF3L0YCeS5JLz7JAqcUEsDBBQACAgIAGEhd1JAAAAAAAAAAAAAAAASAAAAd2VyR751YW_541LpbmcueG1NpZNNTsM"
#                "wEIVPwB0E7VskFSAUNe2ECjbs4VtKdsAqxbU7J4VIpe8JtC2VsT1IzaX5LtlD6Y8LUSvZ7IvMFL_762InrGRT536YB_24L/"
#                "3IXVsciHE0IYA5JsJKi6NFyDkECO/DsmeqaDmHOiklxviJlghZI1JhSe9NNxtFVXN5JavhIK/5Ee0EozBj3Jzm0ExcYP9VGWPWA"
#                "cPMNUEsHCEkTQ3VoAQAAPQUAAFBLAwQUAAgICABhIXdnxKCY0JJA647ERYUeMKd0IIEG7JX3YoH703EP87Eh5ARGE343YCPF4N8I6E"
#                "x5NuqNmJTiK4IXN817IMAAAAAAAA0A804NOcbLQAAAfiAAAAAEQAAAHdvcmQvc2Y0AGluE781JG1JpZXNbtS358JfYO8Y6A7Ao0I2IH"
#                "V6J0LPuy2NXWOqc9YILT5N2ILhEjXO6YBKLGE247ESm0JsrZQQ4LzV1AsC550IESmhw7LA4A+ckT9NtGjGqRE593VhYCoaNH513"
#                "YUihqophOv6YCDMD7JDyrHArqHSXjImh3JegpGS633Jm7EV5YxMC241YLHtsJ7VPQAjybYQfUGS4JXtJ8LW1NRA4LanSH+SP9IMT"
#                "T8E/RV8AaLGMiVLlK1JtKASK8AkXaI/rz+W3IDCOpAEuJK0JGde4JR4EOv")
#
# print("SHA-1 hash:", hash_text(sample_text))

#
# import base64
# import binascii
# import urllib.parse
#
# # Base64 dekodlash
# def decode_base64(data):
#     try:
#         return base64.b64decode(data).decode('utf-8', errors='ignore')
#     except Exception as e:
#         return f"Base64 decode failed: {e}"

# URL dekodlash
# def decode_url(data):
#     try:
#         return urllib.parse.unquote(data)
#     except Exception as e:
#         return f"URL decode failed: {e}"
#
# # Hex dekodlash
# def decode_hex(data):
#     try:
#         return binascii.unhexlify(data).decode('utf-8', errors='ignore')
#     except Exception as e:
#         return f"Hex decode failed: {e}"
#
# encoded_text = "WgAERjp352Y3N2Lno7EGbv1VI578E5Jzf9Jbj5JX2N8Jg5IgF6LTEy4NEXDPIhC5L8VnxsngigXVUZ1I724E5AkR79It1E+hK7Jn6IYFHaJsolpLSOZOEoWUlV9NuwXDtizmgos4AsQgVxUNlFgyUoU7AhRTuGK6J6EF0JEhJhTrpEAslGIKF3L0YCeS5JLz7JAqcUEsDBBQACAgIAGEhd1JAAAAAAAAAAAAAAAASAAAAd2VyR751YW_541LpbmcueG1NpZNNTsMwEIVPwB0E7VskFSAUNe2ECjbs4VtKdsAqxbU7J4VIpe8JtC2VsT1IzaX5LtlD6Y8LUSvZ7IvMFL_762InrGRT536YB_24L/3IXVsciHE0IYA5JsJKi6NFyDkECO/DsmeqaDmHOiklxviJlghZI1JhSe9NNxtFVXN5JavhIK/5Ee0EozBj3Jzm0ExcYP9VGWPWAcPMNUEsHCEkTQ3VoAQAAPQUAAFBLAwQUAAgICABhIXdnxKCY0JJA647ERYUeMKd0IIEG7JX3YoH703EP87Eh5ARGE343YCPF4N8I6Ex5NuqNmJTiK4IXN817IMAAAAAAAA0A804NOcbLQAAAfiAAAAAEQAAAHdvcmQvc2Y0AGluE781JG1JpZXNbtS358JfYO8Y6A7Ao0I2IHV6J0LPuy2NXWOqc9YILT5N2ILhEjXO6YBKLGE247ESm0JsrZQQ4LzV1AsC550IESmhw7LA4A+ckT9NtGjGqRE593VhYCoaNH513YUihqophOv6YCDMD7JDyrHArqHSXjImh3JegpGS633Jm7EV5YxMC241YLHtsJ7VPQAjybYQfUGS4JXtJ8LW1NRA4LanSH+SP9IMTT8E/RV8AaLGMiVLlK1JtKASK8AkXaI/rz+W3IDCOpAEuJK0JGde4JR4EOv"
#
# print("Base64 Decoded:", decode_base64(encoded_text))
# print("URL Decoded:", decode_url(encoded_text))
# print("Hex Decoded:", decode_hex(encoded_text))


# def xor_decrypt(data, key):
#     return ''.join(chr(b ^ key) for b in data)
#
# # Xor qilish uchun kalit va malumotni aniqlash
# encoded_bytes = b'...'
# key = 0xAA  # Misol uchun kalit, bu yerda kalitni topish kerak bo'lishi mumkin
#
# decoded_text = xor_decrypt(encoded_bytes, key)
# print("XOR Decoded:", decoded_text)


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def decrypt_aes(cipher_text, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(cipher_text) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
    return decrypted.decode('utf-8', errors='ignore')

# AES shifrlash uchun misol, asl kalit va iv kerak
key = b'0123456789abcdef'
iv = b'0123456789abcdef'
cipher_text = b'...'  # Shifrlangan matn

print("AES Decrypted:", decrypt_aes(cipher_text, key, iv))
