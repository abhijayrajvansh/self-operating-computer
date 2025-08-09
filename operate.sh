#!/bin/bash
# Self-Operating Computer Launch Script
cd "$(dirname "$0")"
source .venv/bin/activate
python -m operate.main "$@"
