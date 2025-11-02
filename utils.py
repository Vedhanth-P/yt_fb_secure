import os, json, hashlib, binascii
from pathlib import Path

APP_DIR = Path(__file__).parent.resolve()
CONFIG_FILE = APP_DIR / "config.json"
ENV_FILE = APP_DIR / ".env"

def save_env(values: dict):
    lines = []
    for k, v in values.items():
        lines.append(f"{k}={v or ''}")
    ENV_FILE.write_text("\n".join(lines))

def load_env():
    if not ENV_FILE.exists():
        return {}
    res = {}
    for line in ENV_FILE.read_text().splitlines():
        if not line.strip() or line.strip().startswith('#'):
            continue
        if '=' in line:
            k, v = line.split('=',1)
            res[k.strip()] = v.strip()
    return res

def is_password_set():
    return CONFIG_FILE.exists()

def set_password(password: str):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    data = {'salt': salt.decode('ascii'), 'hash': pwdhash.decode('ascii')}
    CONFIG_FILE.write_text(json.dumps(data))

def verify_password(password: str):
    if not CONFIG_FILE.exists():
        return False
    data = json.loads(CONFIG_FILE.read_text())
    salt = data['salt'].encode('ascii')
    stored_hash = data['hash']
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_hash
