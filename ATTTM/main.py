from flask import Flask, render_template, request, send_file
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ENCRYPTED_FOLDER'] = 'encrypted'
app.config['DECRYPTED_FOLDER'] = 'decrypted'
KEY = b'ThisIsASecretKey'  # 16 bytes AES key (hoặc 32 bytes)

def pad(data):
    padding = 16 - len(data) % 16
    return data + bytes([padding] * padding)

def unpad(data):
    padding = data[-1]
    return data[:-padding]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)

        with open(file_path, 'rb') as f:
            data = f.read()

        iv = get_random_bytes(16)
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        encrypted = iv + cipher.encrypt(pad(data))

        encrypted_path = os.path.join(app.config['ENCRYPTED_FOLDER'], f"encrypted_{uploaded_file.filename}")
        with open(encrypted_path, 'wb') as f:
            f.write(encrypted)

        return send_file(encrypted_path, as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)

        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        iv = encrypted_data[:16]
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted_data[16:]))

        decrypted_path = os.path.join(app.config['DECRYPTED_FOLDER'], f"decrypted_{uploaded_file.filename}")
        with open(decrypted_path, 'wb') as f:
            f.write(decrypted)

        return send_file(decrypted_path, as_attachment=True)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['ENCRYPTED_FOLDER'], exist_ok=True)
    os.makedirs(app.config['DECRYPTED_FOLDER'], exist_ok=True)
    app.run(debug=True)
