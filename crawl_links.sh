#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
  echo "Usage: ./crawl_links.sh <url>"
  exit 1
fi

echo "Starting crawl for $URL"

python scrape_links.py "$URL"

# Remove old urls.txt
if [ -f "./documents/urls.txt" ]; then
  echo "Removing old documents/urls.txt"
  rm ./documents/urls.txt
fi

# Copy new file
cp urls.txt ./documents/

echo "New urls.txt copied to documents/"