import sys
import os
import time
import exifread

def get_exif_date(photo_file):
    with open(photo_file, 'rb') as f:
        tags = exifread.process_file(f)
        if 'EXIF DateTimeOriginal' in tags:
            return tags['EXIF DateTimeOriginal'].values
        else:
            print("No EXIF DateTimeOriginal found.")
            return None

def change_file_timestamp(photo_file, exif_date):
    # Convert EXIF date format to timestamp
    exif_date = exif_date.replace(':', '').replace(' ', '')
    timestamp = time.mktime(time.strptime(exif_date, '%Y%m%d%H%M%S'))
    
    # Change the file timestamp
    os.utime(photo_file, (timestamp, timestamp))

def rename_file(photo_file, exif_date):
    exif_date = exif_date.replace(':', '').replace(' ', '_')
    file_dir, file_ext = os.path.split(photo_file)
    new_filename = f"IMG_{exif_date}.JPEG"

    if file_ext.lower() == ".jpg":
        new_filepath = os.path.join(file_dir, new_filename)
        os.rename(photo_file, new_filepath)
        return new_filepath
    else:
        new_filepath = os.path.join(file_dir, new_filename)
        os.rename(photo_file, new_filepath)
        return new_filepath

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_timestamp.py <photo-file>")
        sys.exit(1)

    photo_file = sys.argv[1]

    if not os.path.isfile(photo_file):
        print(f"File not found: {photo_file}")
        sys.exit(1)

    exif_date = get_exif_date(photo_file)

    if exif_date:
        change_file_timestamp(photo_file, exif_date)
        new_file = rename_file(photo_file, exif_date)
        print(f"Timestamps updated and file renamed to {new_file}")
    else:
        print(f"Failed to update timestamps for {photo_file}")

if __name__ == "__main__":
    main()
