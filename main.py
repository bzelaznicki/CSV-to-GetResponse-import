from constants import *
from converter import *


csv_data = """E-mail,Name,Street Address,Telefon Komórkowy,Telefon służbowy,City,Country,Tags
user@example.com,John Doe,Sample Street 123,Gotham,UK,Metropolis,United Kingdom,"attended_event,promo2024,high_value"
user2@example.com,Jane Doe,Sample Street 123,Gotham,UK,Gotham,United Kingdom,"attended_event,high_value"
"""



def main():
    file_data = process_csv_data(csv_data)
    print(file_data)


if __name__ == '__main__':
    main()