import unicodedata
import re
from constants import *

def get_and_convert_headers(csv):
    raw_headers = csv.split('\n')[0].split(',')
    headers = []
    for header in raw_headers:
        converted_header = convert_header(header)
        headers.append(converted_header)
    return headers

def remove_accents(text):
    #remove all accents from text
    return ''.join(NON_NFKD_MAP[c] if c in NON_NFKD_MAP else c \
                   for part in unicodedata.normalize('NFKD', text) for c in part
                   if unicodedata.category(part) != 'Mn')
    

def convert_header(header):
    
    converted = remove_accents(header) #removes accents

    converted = converted.lower() #converts to lowercase

    converted = re.sub(r'[^a-z0-9_\s]', '', converted) #removes all non-alphanumeric characters except spaces and underscores
    
    if converted in FIELD_MAPPINGS: #checks if the header is in the FIELD_MAPPINGS dictionary
        converted = FIELD_MAPPINGS[converted]
    
    converted = converted.replace(' ', '_') #replaces spaces with underscores

    converted = re.sub(r'_+', '_', converted) #replaces multiple spaces with a single underscore
    return converted