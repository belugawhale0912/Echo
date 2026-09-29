# Echo tests - HTTP API behaviour.
# Exercises the API against a Redis client: burn-once semantics, TTL expiry,
# payload size limits, the concurrent read race (exactly one winner) and the
# rate limiter. Uses fakeredis by default; set TEST_REDIS_URL to run the same
# suite against a real Redis instance.

