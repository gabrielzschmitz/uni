#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m'

# Compile and run function
compile_and_run() {
    local file=$1
    local output="${file%.cpp}.out"

    echo -e "${GREEN}Compiling ${file}...${NC}"
    g++ "$file" -o "$output"
    if [ $? -eq 0 ]; then
        echo -e "${BLUE}Compiling ${file}: Success!${NC}"
    else
        echo -e "${RED}Compiling ${file}: Failed!${NC}"
        exit 1
    fi

    echo -e "${YELLOW}Running ${output}...${NC}"
    ./"$output"
    echo -e ""

    rm -f "$output"
}

# Test each file
compile_and_run "1.cpp"
compile_and_run "2.cpp"
compile_and_run "3.cpp"
compile_and_run "4.cpp"
compile_and_run "5.cpp"
compile_and_run "6.cpp"
compile_and_run "7.cpp"
