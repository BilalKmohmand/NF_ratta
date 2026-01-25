#!/usr/bin/env bash
set -e
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
