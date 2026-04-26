#!/bin/bash

echo "Executing Pre-API Helpers"

echo "=== Running VPC creation script ==="

python3 "$DEFAULT_PATH/$CUSTOMIZATION/api_helpers/python/vpc.py"

echo "=== Done ==="