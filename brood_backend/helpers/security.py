import hashlib
import os
import binascii


def hash_password(plain_password: str) -> str:
    # Hash a password for storing.
    salt = hashlib.sha256(os.urandom(60)).hexdigest()
    password_hash = hashlib.pbkdf2_hmac(
        hash_name="sha512",
        password=plain_password.encode("utf-8"),
        salt=salt.encode("ascii"),
        iterations=100000,
    )
    password_hash = binascii.hexlify(password_hash)
    return (salt + password_hash).decode("ascii")


def verify_password(plain_password: str, stored_password: str) -> bool:
    # Verify a stored password against one provided by user.
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    password_hash = hashlib.pbkdf2_hmac(
        hash_name="sha512",
        password=plain_password.encode("utf-8"),
        salt=salt.encode("ascii"),
        iterations=100000,
    )
    password_hash = binascii.hexlify(password_hash)
    return password_hash.decode("ascii") == stored_password
