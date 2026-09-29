# Echo API - per-IP rate limiting.
# Fixed-window counters held in Redis and incremented together with their expiry
# in a single Lua script, with separate budgets for creating and for reading
# secrets. Fails open when Redis is unavailable so the API degrades instead of
# disappearing.

