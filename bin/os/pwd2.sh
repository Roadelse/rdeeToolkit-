#!/bin/bash

echo "$(cd "$(dirname "$1")"; pwd)/$(basename "$1")"
