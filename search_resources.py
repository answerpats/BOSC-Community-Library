import sys
import os

def search_resources(keyword):
    resources_file = 'RESOURCES.md'
    if not os.path.exists(resources_file):
        print(f"Error: {resources_file} not found.")
        return

    print(f"Searching for '{keyword}' in {resources_file}...\n")
    found = False
    with open(resources_file, 'r', encoding='utf-8') as f:
        for line in f:
            if keyword.lower() in line.lower():
                if '|' in line: # Likely a table row
                    print(line.strip())
                    found = True
    
    if not found:
        print("No matches found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_resources.py <keyword>")
    else:
        search_resources(sys.argv[1])
