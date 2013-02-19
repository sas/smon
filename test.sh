#!/bin/sh

cd web/

if [ ! -f data.json ]; then
  sudo python -B ../data/generate-data.py data.json
fi

python -m SimpleHTTPServer
