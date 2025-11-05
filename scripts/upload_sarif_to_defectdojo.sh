#!/usr/bin/env bash
# usage: upload_sarif_to_defectdojo.sh <api_url> <api_key> <product_id> <engagement_id> <scan_type> <file>
API_URL=$1
API_KEY=$2
PRODUCT=$3
ENGAGEMENT=$4
SCAN_TYPE=$5
FILE=$6

curl -s -X POST "${API_URL}/api/v2/import-scan/" \
  -H "Authorization: Token ${API_KEY}" \
  -F "file=@${FILE}" \
  -F "scan_type=${SCAN_TYPE}" \
  -F "product=${PRODUCT}" \
  -F "engagement=${ENGAGEMENT}"
