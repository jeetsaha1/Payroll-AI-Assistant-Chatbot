from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import request, jsonify

# Mock user data for demonstration purposes
users = {
    "admin": {
        "password": generate_password_hash("admin123"),
        "role": "admin"
    },
    "employee": {
        "password": generate_password_hash("employee123"),
        "role": "employee"
    }
}

def authenticate(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth = request.authorization
            if not auth or not authenticate(auth.username, auth.password):
                return jsonify({"message": "Authentication required"}), 401
            
            user = users[auth.username]
            if user["role"] != role:
                return jsonify({"message": "Access denied"}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def encrypt_data(data):
    # Placeholder for encryption logic
    return data  # In a real implementation, return encrypted data

def decrypt_data(encrypted_data):
    # Placeholder for decryption logic
    return encrypted_data  # In a real implementation, return decrypted data