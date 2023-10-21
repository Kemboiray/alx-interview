import sys

count = 1
# Read input from stdin line by line
for line in sys.stdin:
    # Process each line as needed
    processed_line = line.strip()  # Remove leading/trailing whitespace
    # Perform your processing on 'processed_line'

    # Example: Print the processed line
    print(f"Processed line {count}:", processed_line)
    count += 1
