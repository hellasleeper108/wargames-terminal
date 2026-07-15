#!/bin/bash
# WOPR Terminal — Start Script
# Serve locally and open in browser

PORT=${1:-8080}
DIR="$(cd "$(dirname "$0")" && pwd)"

echo -e "\033[32m"
echo "  INITIALIZING WOPR TERMINAL..."
echo "  CONNECTING AT 1200 BAUD..."
echo -e "\033[0m"

# Try xdg-open, then open, then just print url
if command -v xdg-open &>/dev/null; then
    xdg-open "http://localhost:$PORT" 2>/dev/null &
elif command -v open &>/dev/null; then
    open "http://localhost:$PORT" 2>/dev/null &
fi

cd "$DIR" && python3 serve.py "$PORT"
