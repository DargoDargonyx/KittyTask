#!/bin/sh

set -eu

PREFIX="/usr/local"
BINARY="$PREFIX/bin/ktask"
LIB_DIR="$PREFIX/lib/ktask"
ASSET_DIR="$PREFIX/share/ktask"
DATA_DIR="${HOME}/.local/share/ktask"

if [ ! -f "$BINARY" ] && \
   [ ! -d "$LIB_DIR" ] && \
   [ ! -d "$ASSET_DIR" ]; then
    echo "ktask is not installed."
    exit 0
fi

echo "Removing ktask..."

if [ "$(id -u)" -eq 0 ]; then
    rm -f "$BINARY"
    rm -rf "$LIB_DIR"
    rm -rf "$ASSET_DIR"
	rm -rf "$DATA_DIR"
else
    sudo rm -f "$BINARY"
    sudo rm -rf "$LIB_DIR"
    sudo rm -rf "$ASSET_DIR"
	sudo rm -rf "$DATA_DIR"
fi

echo "ktask has been uninstalled."
