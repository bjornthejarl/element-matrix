# Matrix Synapse + Element (Nixpacks Deployment)

This repository is configured to deploy a Matrix homeserver (Synapse) bundled with Element Web to Dokploy using Nixpacks.

## 🚀 Deployment Instructions (Dokploy)

1. **Connect Repository**: Add this repo to Dokploy and select "Nixpacks" as the build type.
2. **Environment Variables**: Add the following variables in the Dokploy Environment tab:

```env
MATRIX_SERVER_NAME=jpmxruytgigenavmmqwwoo.valpha.dev
POSTGRES_HOST=postgres (or your db host)
POSTGRES_USER=synapse
POSTGRES_PASSWORD=YOUR_DB_PASSWORD
POSTGRES_DB=synapse
SYNAPSE_REGISTRATION_SHARED_SECRET=GENERATE_RANDOM_STRING
SYNAPSE_MACAROON_SECRET_KEY=GENERATE_RANDOM_STRING
SYNAPSE_FORM_SECRET=GENERATE_RANDOM_STRING
SYNAPSE_SIGNING_KEY=ed25519 a_vAlp H2kPqT8mN5xR7wY3bF9jL4vC6dS1gK8hM2nP5qW7tU0= (Or generate your own)
RTC_DOMAIN=rtc.valpha.dev
TURN_SHARED_SECRET=GENERATE_RANDOM_STRING
```

3. **Domains**:
   - `jpmxruytgigenavmmqwwoo.valpha.dev` -> Port `8008` (Serves both Matrix API and Element Web)


