# EXIF Toucher

EXIF Toucher is a Python script that updates the file timestamps and renames JPEG images based on their EXIF data. The script reads the `DateTimeOriginal` tag from the EXIF metadata, sets the file's modification and access times to match this date, and renames the file to the format `IMG_YYYYMMDD_HHMMSS.JPEG`.

## Features

- Reads EXIF `DateTimeOriginal` tag from JPEG images.
- Updates the file's modification and access timestamps to match the EXIF date.
- Renames the file to the format `IMG_YYYYMMDD_HHMMSS.JPEG`, converting `.jpg` to `.jpeg` if necessary.

## Requirements

- Python 3.x
- `exifread` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/EXIF-Toucher.git
    cd EXIF-Toucher
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script with the JPEG file as an argument:

```bash
python update_timestamp.py <photo-file>
