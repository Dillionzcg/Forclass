#!/usr/bin/env bash
set -e

echo "Fetching data from local server..."
DATA=$(curl -fsS http://127.0.0.1:8000/packages.json)

echo "Generating summary.md..."
echo "# Package Summary Report" > summary.md
echo "" >> summary.md
echo "| Name | Version | Downloads |" >> summary.md
echo "| --- | --- | --- |" >> summary.md

echo "$DATA" | jq -r '
  [ .[] | select(.status == "active" and .downloads >= 100) ]
  | sort_by(-.downloads, .name)
  | .[]
  | "| \(.name) | \(.version) | \(.downloads) |"
' >> summary.md

echo "Report generated successfully!"
