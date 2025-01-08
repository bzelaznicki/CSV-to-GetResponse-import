from constants import *
from converter import *
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert CSV file with tags to expanded format')
    parser.add_argument('input_file', help='Path to the input CSV file')
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        # Read the input CSV
        input_data = read_csv(args.input_file)
        
        # Convert the data
        headers, rows = convert_csv(input_data)
        
        # Write the converted data
        output_filepath = write_csv(headers, rows, args.input_file)
        print(f"Converted file saved to: {output_filepath}")
        
    except FileNotFoundError:
        print(f"Error: Could not find file '{args.input_file}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()