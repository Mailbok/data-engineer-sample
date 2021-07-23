from src.some_storage_library import SomeStorageLibrary

"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""



if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    SomeStorageLibrary().merge_headers_and_data()
