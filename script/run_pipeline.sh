#!/bin/bash
cd "$(dirname "$0")/.."
echo "Pipeline started: $(date)" > logs/pipeline.log
python main.py >> logs/pipeline.log