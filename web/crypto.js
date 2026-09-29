/**
 * Echo frontend - client-side cryptography.
 * AES-256-GCM helpers built on WebCrypto: generate, export and import keys,
 * encrypt text locally, and decrypt a sealed record. The key travels in the URL
 * fragment and is never sent to the server. Written so the same file runs in
 * the browser and under Node >= 19, which lets the round-trip checks run
 * headless too.
 */

