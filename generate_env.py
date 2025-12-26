import secrets
import string
import base64

# Configuration
DOMAIN = "jpmxruytgigenavmmqwwoo.valpha.dev"
RTC_DOMAIN = "rtc.valpha.dev"
POSTGRES_USER = "synapse"
POSTGRES_DB = "synapse"

def generate_secret(length=32):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_signing_key():
    # Generate 32 bytes of random data for the key
    key_bytes = secrets.token_bytes(32)
    # Encode as base64 and STRIP PADDING '='
    # 32 bytes -> 43 chars    # Synapse uses unpadded URL-safe base64
    key_b64 = base64.urlsafe_b64encode(key_bytes).decode('utf-8').rstrip('=')
    return f"ed25519 a_0 {key_b64}" 

def main():
    print(f"# --- COPY BELOW THIS LINE TO DOKPLOY ---")
    
    # Domain & Infrastructure
    print(f"MATRIX_SERVER_NAME={DOMAIN}")
    print(f"RTC_DOMAIN={RTC_DOMAIN}")
    
    # Database
    print(f"POSTGRES_USER={POSTGRES_USER}")
    print(f"POSTGRES_DB={POSTGRES_DB}")
    print(f"POSTGRES_PASSWORD={generate_secret(24)}")
    
    # Synapse Secrets
    print(f"SYNAPSE_REGISTRATION_SHARED_SECRET={generate_secret(48)}")
    print(f"SYNAPSE_MACAROON_SECRET_KEY={generate_secret(48)}")
    print(f"SYNAPSE_FORM_SECRET={generate_secret(48)}")
    print(f"TURN_SHARED_SECRET={generate_secret(48)}")
    
    # Signing Key
    print(f"SYNAPSE_SIGNING_KEY={generate_signing_key()}")

if __name__ == "__main__":
    main()
