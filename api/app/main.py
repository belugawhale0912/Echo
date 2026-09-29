# Echo API - FastAPI application and HTTP routes.
# Defines the /api surface (create a secret, burn-and-read a secret, status,
# config, health), the single error envelope, the harden/security-header
# middleware and the per-IP rate-limit dependencies. Builds the app through a
# create_app(settings, redis) factory so tests can inject their own client.

