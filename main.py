from constants import *
from converter import *


csv = """E-mail,Name,Street Address,Telefon Komórkowy,Telefon służbowy,City,Country,Tags
user@example.com,John Doe,Sample Street 123,Gotham, UK,"attended_event,promo2024,high_value
user2@example.com,Jane Doe, Sample Street 123, Gotham, UK, "attended_event,high_value"""



def main():
    headers = get_and_convert_headers(csv)
    print(headers)


if __name__ == '__main__':
    main()