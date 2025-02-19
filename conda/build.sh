#!/bin/bash
set -ex

# Create the bin directory in the conda prefix if it doesn't exist.
mkdir -p "$PREFIX/bin"

# Copy the rmlst.py script to the bin directory and rename to 'rmlst'.
cp rmlst.py "$PREFIX/bin/rmlst"

# Make sure the script is executable.
chmod +x "$PREFIX/bin/rmlst"
