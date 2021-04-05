#!/usr/bin/env bash

for i in $(seq 0 $1); do
    git commit --allow-empty -m "$i" --date "$(date -d "-$i days")"
done
