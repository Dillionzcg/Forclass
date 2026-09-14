#!/usr/bin/env bash
set -e

echo "Running ruff format check..."
ruff format --check .

echo "Running ruff check..."
ruff check .

echo "Running pytest..."
python -m pytest

echo "All quality gates passed successfully!"
