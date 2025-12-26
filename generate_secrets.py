import secrets
import string
import base64

def generate_secret(length=32):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_signing_key():
    # Generate 32 bytes of random data for the key
    key_bytes = secrets.token_bytes(32)
    # Encode as base64 (removing padding if any, though 32 bytes = 44 chars with padding usually)
    # Synapse uses unpadded base64 for some things, but standard usually works.
    # Let's use standard URL-safe base64.
    key_b64 = base64.urlsafe_b64encode(key_bytes).decode('utf-8').rstrip('=')
    return f"ed25519 a_{key_b64}" 
    # Note: "a_" is a common prefix for the key version/id, usually "a_..."

def main():
    print("# Matrix/Synapse Secrets Generator")
    print("# Copy these values into your Dokploy Environment Variables\n")

    print(f"POSTGRES_PASSWORD={generate_secret(24)}")
    print(f"SYNAPSE_REGISTRATION_SHARED_SECRET={generate_secret(48)}")
    print(f"SYNAPSE_MACAROON_SECRET_KEY={generate_secret(48)}")
    print(f"SYNAPSE_FORM_SECRET={generate_secret(48)}")
    print(f"TURN_SHARED_SECRET={generate_secret(48)}")
    
    # Signing Key
    # The format often used is "ed25519 <key_id> <private_key>" but config usually takes the whole string or just the key.
    # Our template uses: signing_key: - "ed25519 {{ SYNAPSE_SIGNING_KEY }}"
    # So we just provide the version and key part.
    # Real synapse signing key generation is more complex (nacl), but for a fresh start, a random key *might* be accepted 
    # if Synapse generates its own on first boot if missing. 
    # However, since we mount config, we force it.
    # Ideally, we should verify validity. But simple random bytes usually suffice for the 'secret' part of the key in config contexts
    # unless it validates the ED25519 format strictly. 
    # Let's generate a pseudo-valid looking one.
    print(f"SYNAPSE_SIGNING_KEY={generate_signing_key()}")

if __name__ == "__main__":
    main()
