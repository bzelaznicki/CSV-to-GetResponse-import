import unicodedata
import re
import csv
from constants import *
from io import StringIO

def get_and_convert_headers(csv_data):
    if not csv_data:
        raise ValueError('CSV appears to be empty')
        
    csv_reader = csv.reader(StringIO(csv_data))
    try:
        raw_headers = next(csv_reader)  # Gets first row
    except StopIteration:
        raise ValueError('CSV appears to be empty')
    headers = []
    for header in raw_headers:
        converted_header = convert_header(header)
        if converted_header == '':
            continue
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