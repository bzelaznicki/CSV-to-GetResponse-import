import unicodedata
import re
import csv
from constants import *
from io import StringIO
import os

def get_and_convert_headers(raw_headers):
    if not raw_headers:
        raise ValueError('Headers appear to be empty')
        
    headers = []
    seen_headers = set()  # Track seen headers
    for header in raw_headers:
        converted_header = convert_header(header)
        if converted_header == '':
            continue
        if converted_header in seen_headers:  # Check for duplicates
            raise ValueError(f'Duplicate header found: {converted_header}')
        seen_headers.add(converted_header)
        headers.append(converted_header)

    if len(headers) == 0:
        raise ValueError('All headers were invalid or empty after conversion')
    return headers

def remove_accents(text):
    text = text.replace('ß', 'ss') #replace ß with ss
    #remove all accents from text
    return ''.join(NON_NFKD_MAP[c] if c in NON_NFKD_MAP else c \
                   for part in unicodedata.normalize('NFKD', text) for c in part
                   if unicodedata.category(part) != 'Mn')
    

def convert_header(header):
    
    converted = remove_accents(header)

    converted = converted.lower()
    
    if converted in FIELD_MAPPINGS:
        converted = FIELD_MAPPINGS[converted]
    
    converted = re.sub(r'[^a-z0-9_\s]', '_', converted)
    
    converted = converted.replace(' ', '_')
    converted = converted.strip('_')
    converted = re.sub(r'_+', '_', converted)
    
    return converted

def convert_tag(tag):
    
    converted = remove_accents(tag) #removes accents

    converted = converted.lower() #converts to lowercase  
    converted = re.sub(r'[^a-z0-9_]', '_', converted) #removes all non-alphanumeric characters except spaces and underscore
    
    converted = converted.replace(' ', '_') #replaces spaces with underscores
    converted = converted.strip('_')#removes leading and trailing underscores
    converted = re.sub(r'_+', '_', converted) #replaces multiple underscores with a single underscore
    converted = converted[:64] #limits the tag to 50 characters
    return converted

def is_tags_column(header):
    return header == TAGS_COLUMN


def process_row(headers, row):
    processed_row = {}
    for header, value in zip(headers, row):
        if is_tags_column(header):
            processed_row[header] = process_tags(value)
        else:
            processed_row[header] = value.strip()
    
    return processed_row

def process_tags(tag_string):
    if not tag_string:
        return []
    
    # Split by comma and clean each tag
    tags = tag_string.split(',')
    # Remove whitespace and empty tags
    tags = [tag.strip() for tag in tags if tag]
    
    return tags

def detect_delimiter(csv_data):
    stripped_data = csv_data.strip()
    if not stripped_data:
        return ','
    
    sample = '\n'.join(stripped_data.splitlines()[:10])
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=[',', ';'])
        return dialect.delimiter
    except csv.Error:
        first_line = stripped_data.splitlines()[0]
        if first_line.count(';') > first_line.count(','):
            return ';'
        return ','

def process_csv_data(csv_data):
    if not csv_data.strip():
        raise ValueError('Empty CSV data')
    
    # Normalize line endings to \n
    csv_data = csv_data.replace('\r\n', '\n').replace('\r', '\n')
    
    delimiter = detect_delimiter(csv_data)
    
    csv_reader = csv.reader(StringIO(csv_data), quotechar='"', delimiter=delimiter)
    headers = get_and_convert_headers(next(csv_reader))
    expected_columns = len(headers)

    processed_data = []
    for row_num, row in enumerate(csv_reader, start=1):
        if len(row) != expected_columns:
            raise ValueError(f'Row {row_num} has {len(row)} columns, expected {expected_columns}')
        processed_row = process_row(headers, row)
        processed_data.append(processed_row)

    return processed_data

def get_unique_tags(row_tags):
    tags = set()
    for tag_list in row_tags:  
        for tag in tag_list:   
            cleaned_tag = convert_tag(tag)
            if cleaned_tag:
                tags.add(cleaned_tag)
    return sorted(tags)

def convert_csv(input_data):
    processed_csv = process_csv_data(input_data)
    
    # Get all headers
    headers = list(processed_csv[0].keys())
    
    # Check if tags column exists
    has_tags = TAGS_COLUMN in headers
    
    if has_tags:
        # Get all headers except 'tags'
        base_headers = [h for h in headers if h != TAGS_COLUMN]
        unique_tags = get_unique_tags(row[TAGS_COLUMN] for row in processed_csv)
        tag_headers = [f'tag:{tag}' for tag in unique_tags]
        
        # Combine headers
        final_headers = base_headers + tag_headers
        
        # Generate rows with tags
        rows = []
        for row in processed_csv:
            new_row = [row[header] for header in base_headers]
            row_tags = [convert_tag(tag) for tag in row[TAGS_COLUMN]]
            
            for tag in unique_tags:
                new_row.append('1' if tag in row_tags else '0')
            rows.append(new_row)
    else:
        # No tags processing needed
        final_headers = headers
        rows = [[row[header] for header in headers] for row in processed_csv]
    
    return final_headers, rows  

def get_output_filename(input_filename):
    # Split the filename and extension
    base, ext = os.path.splitext(input_filename)
    return f"{base}_converted{ext}"

def read_csv(input_filepath):
    with open(input_filepath, 'r') as csvfile:
        # Read entire file as a string
        return csvfile.read()
    
def write_csv(headers, rows, input_filepath):
    # Get the directory of the input file
    input_dir = os.path.dirname(input_filepath)
    input_filename = os.path.basename(input_filepath)
    
    # Create output filename
    base, ext = os.path.splitext(input_filename)
    output_filename = f"{base}_converted{ext}"
    
    # Combine directory with new filename
    output_filepath = os.path.join(input_dir, output_filename)
    
    with open(output_filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)
    return output_filepath
