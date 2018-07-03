#! /usr/bin/env bash
out=$(ifconfig | grep  'Mask:' | grep -v '127.0.0.1' | awk '{print $NF}' | tr -d 'Mask:' | mask.py)
echo "$out"
