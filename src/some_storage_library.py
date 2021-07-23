import os
import pathlib
import shutil
import datetime


project_root = pathlib.Path(__file__).parent.parent.resolve()

destination_dir = os.path.join(project_root, 'data', 'destination')
source_dir = os.path.join(project_root, 'data', 'source')
processing_dir = os.path.join(project_root, 'data', 'processing')

data_source_filename = 'SOURCEDATA.txt'
headers_source_filename = 'SOURCECOLUMNS.txt'

final_filename_suffix = ' Data.txt'

class SomeStorageLibrary:

    def __init__(self) -> None:
        print('Instantiating storage library...')
        for dir in [destination_dir, processing_dir]:
            if not os.path.isdir(dir):
                os.mkdir(dir)

    def load_csv(self, src_path: str) -> None:
        print(f'Loading the following file to storage medium: {src_path}')
        shutil.move(src_path, destination_dir)
        print('Load completed!')

    def merge_headers_and_data(self) -> None:
        final_filename = str(datetime.datetime.utcnow()) + final_filename_suffix

        headers_source_path = os.path.join(source_dir, headers_source_filename)
        data_source_path = os.path.join(source_dir, data_source_filename)
        data_destination_path = os.path.join(processing_dir, final_filename)

        headers = self.read_csv(headers_source_path)
        headers = self.format_headers(headers)

        data = self.read_csv(data_source_path)

        print('Merging data')
        data = '\n'.join([headers, data])
        print('Data merged')

        self.write_csv(data, data_destination_path)
        self.load_csv(data_destination_path)

        self.cleanup()


    def read_csv(self, filename: str) -> str:
        """Reads a file from disk and returns the contents"""
        print(f'Reading file: {filename}')
        f = open(filename)
        return f.read()

    def write_csv(self, data: str, path: str) -> str:
        """Writes a file to disk and returns the path"""
        print(f'Writing file: {path}')
        file = open(path, 'w')
        file.write(data)
        file.close()
        return path

    def format_headers(self, headers: str) -> str:
        """Takes the headers as input, sorts by the value, then returns just
            the header names in a pipe delimited string"""
        headers = headers.split('\n')
        headers = sorted(headers, key=lambda x: int(x.split('|')[0]))
        headers = [x.split('|')[1] for x in headers]
        headers = '|'.join(headers)

        return headers

    def cleanup(self) -> None:
        """Removes all files from the processing directory"""
        print('Process complete, cleaning up temp files...')
        shutil.rmtree(processing_dir)
