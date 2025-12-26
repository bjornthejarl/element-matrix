# Matrix Synapse + Element (Docker Compose for Dokploy)

This repository is configured to deploy a Matrix homeserver (Synapse) and Element Web client to Dokploy using Docker Compose.

## 🚀 Deployment Instructions (Dokploy)

1. **Create App**: In Dokploy, create a new Application.
2. **Deployment Method**: Select **Docker Compose**.
3. **Connect Repository**: Link this repository (`https://github.com/bjornthejarl/element-matrix.git`).
4. **Environment Variables**: Add the following variables in the Dokploy Environment tab:

```env
# Domain Settings
MATRIX_SERVER_NAME=jpmxruytgigenavmmqwwoo.valpha.dev
POSTGRES_USER=synapse
POSTGRES_PASSWORD=YOUR_SECURE_PASSWORD
POSTGRES_DB=synapse

# Synapse Secrets (Generate random strings for these)
SYNAPSE_REGISTRATION_SHARED_SECRET=GENERATE_RANDOM_STRING
SYNAPSE_MACAROON_SECRET_KEY=GENERATE_RANDOM_STRING
SYNAPSE_FORM_SECRET=GENERATE_RANDOM_STRING

# Signing Key (Generate one if you don't have it)
# Format: "ed25519 a_vAlp..."
SYNAPSE_SIGNING_KEY=ed25519 YOUR_KEY_HERE

# WebRTC (LiveKit/TURN)
RTC_DOMAIN=rtc.valpha.dev
TURN_SHARED_SECRET=GENERATE_RANDOM_STRING
```

5. **Deploy**: Click **Deploy**.

## 🌐 Domains & Routing
The `docker-compose.yml` uses Traefik labels to serve everything on a **single domain**:

- `https://your-domain/_matrix/*` -> **Synapse**
- `https://your-domain/_synapse/*` -> **Synapse**
- `https://your-domain/*` -> **Element Web**

Everything happens automatically via the `dokploy-network`.
