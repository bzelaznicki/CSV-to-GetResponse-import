# CSV-to-GetResponse-import

This project provides a tool to process CSV files and prepare them for import into GetResponse, a popular email marketing platform.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bzelaznicki/CSV-to-GetResponse-import.git
    ```
2. Navigate to the project directory:
    ```sh
    cd CSV-to-GetResponse-import
    ```
3. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install any required dependencies (if applicable):
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the program, use the following command:
```sh
python main.py <path_to_csv_file>
```

Replace `<path_to_csv_file>` with the path to your CSV file.

### Example

```sh
python main.py /path/to/your/file.csv
```

This will process the CSV file and prepare it for import to GetResponse. The output will be saved in a format compatible with GetResponse's import requirements.

### Features

- Validates the structure of the input CSV file.
- Cleans and formats data to meet GetResponse's import specifications.
- Outputs a new CSV file ready for upload.

## Testing

To run the tests for this project, use the following command:
```sh
python test.py
```

This will execute the test suite to ensure the program is functioning as expected.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
