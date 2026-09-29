# Echo API - environment-driven configuration.
# Defines the immutable Settings object (Redis URL, payload size limit, TTL
# bounds, rate-limit budgets, proxy trust, CORS origins) and validates it on
# construction; populated from environment variables via Settings.from_env().

