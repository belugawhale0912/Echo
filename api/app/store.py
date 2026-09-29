# Echo API - Redis storage for encrypted payloads.
# Owns the secret keyspace: writes a ciphertext record with a TTL, and enforces
# single-use "burn" semantics by fetching and deleting a record inside one
# atomic Lua script, so exactly one request can ever receive a given secret.

