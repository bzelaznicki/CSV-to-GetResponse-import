import unicodedata
import re
import csv
from constants import *
from io import StringIO

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
    
    converted = remove_accents(header) #removes accents

    converted = converted.lower() #converts to lowercase
    if converted in FIELD_MAPPINGS: #checks if the header is in the FIELD_MAPPINGS dictionary
        converted = FIELD_MAPPINGS[converted]    
    converted = re.sub(r'[^a-z0-9_\s]', '_', converted) #removes all non-alphanumeric characters except spaces and underscore
    
    converted = converted.replace(' ', '_') #replaces spaces with underscores
    converted = converted.strip('_')#removes leading and trailing underscores
    converted = re.sub(r'_+', '_', converted) #replaces multiple underscores with a single underscore

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
    #print(f"Processing row: {row}")
    processed_row = {}
    for header, value in zip(headers, row):
        #print(f"Header: {header}, Value: {value}")
        # ... rest of your code
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

def process_csv_data(csv_data):
    if not csv_data.strip():
        raise ValueError('Empty CSV data')
    
    # Normalize line endings to \n
    csv_data = csv_data.replace('\r\n', '\n').replace('\r', '\n')
    
    csv_reader = csv.reader(StringIO(csv_data), quotechar='"', delimiter=',')
    headers = get_and_convert_headers(next(csv_reader))
    expected_columns = len(headers)

    processed_data = []
    for row_num, row in enumerate(csv_reader, start=1):
        if len(row) != expected_columns:
            raise ValueError(f'Row {row_num} has {len(row)} columns, expected {expected_columns}')
        processed_row = process_row(headers, row)
        processed_data.append(processed_row)

    return processed_data

def data_to_csv(data):
    if not data:
        return ''
    
    header = list(data[0].keys())

def get_unique_tags(row_tags):
    tags = set()
    for tag in row_tags:
        cleaned_tag = process_tags(tag)
        tags.add(cleaned_tag)
    
    tags = sorted(tags)
    return list(tags)