#!/usr/bin/env python3

import subprocess
import sys

def flip(command, args):
    # Invert the last two arguments
    inverted_args = args[-1:-3:-1] + args[:-2]
    
    # Form the complete command
    full_command = [command] + inverted_args
    
    # Execute the command
    subprocess.run(full_command)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: flip <command> <arg1> <arg2> [...]")
        sys.exit(1)
    
    # Extract the command and arguments from command-line arguments
    command = sys.argv[1]
    args = sys.argv[2:]
    
    # Run the flip function
    flip(command, args)