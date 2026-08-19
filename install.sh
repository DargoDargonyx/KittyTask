#!/bin/sh

set -eu

PREFIX="/usr/local"
BINARY="ktask"
PRINT_INFO="\033[36m[INFO]\033[0m "

echo -e "${PRINT_INFO} Building release..."
make clean
make release
make copy_libs

if [ ! -f "dist/release/$BINARY" ]; then
    echo "[ERROR] Release binary was not created."
    exit 1
fi

echo -e "${PRINT_INFO} Installing $BINARY..."

sudo install -Dm755 \
    "dist/release/$BINARY" \
    "$PREFIX/bin/$BINARY"

if [ -d "dist/release/lib" ]; then
    sudo mkdir -p "$PREFIX/lib/$BINARY"
    sudo cp -r dist/release/lib/. "$PREFIX/lib/$BINARY/"
fi

#if [ -d "dist/release/assets" ]; then
#    sudo mkdir -p "$PREFIX/share/$BINARY"
#    sudo cp -r dist/release/assets/* "$PREFIX/share/$BINARY/"
#fi

echo -e "${PRINT_INFO} Installation complete."

if ! command -v "$BINARY" >/dev/null 2>&1; then
    echo "[ERROR] $BINARY is not in PATH."
    exit 1
fi

echo -e "${PRINT_INFO} Installed binary:"
command -v "$BINARY"

echo -e "${PRINT_INFO} Installation successful."
