# Echo API - container image definition.
# Multi-stage build: the builder stage installs requirements.txt into a
# virtualenv, and the slim runtime stage copies that virtualenv, drops to a
# non-root user (uid 10001) and starts the API with uvicorn.

