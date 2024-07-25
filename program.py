import hashlib
import os
import time
import shutil
import argparse
import logging


def sync_folders(source, replica, log_file, time_interval):
    if not os.path.isdir(replica):
        os.makedirs(replica)

 # Check if the “replica” directory exists. If not, create it using os.makedirs.

    if not os.path.isdir(source):
        raise argparse.ArgumentError(None, "The source folder doesn't exist.")
    
 # Check if the “source” directory exists. If not, it sends the error “The source folder doesn't exist.”

    logging.info(f"Start with parameters:\nsource:{source}\nreplica:{replica}\nlog:{log_file}\ntime_interval:{time_interval}\n")

 # Records the initial execution information in the log

    while True:
        try:
            compare_folders(source, replica)
            time.sleep(time_interval)
        except KeyboardInterrupt:
            print("The Program is terminated!")
            raise SystemExit

 # Calls “compare_folders” to synchronize the folders.
 # Waits for the time interval entered using “time.sleep”.
 # If there is a keyboard interruption (Ctrl+C), prints a message and terminates the program.

def compare_files(file1, file2):
    with open(file1, "rb") as folder_1, open(file2, "rb") as folder_2:
        return hashlib.md5(folder_1.read()).hexdigest() == hashlib.md5(folder_2.read()).hexdigest()
    
 # Opens both files in binary mode.
 # Calculates the MD5 hash of each file.
 # Returns True if the hashes are equal (identical files), otherwise False.


def compare_folders(source_file, replica_file):
    f_source = os.listdir(source_file)
    f_replica = os.listdir(replica_file)

 # Lists the files in source_f and replica_f.

    for file in f_source:
        source_file_path = os.path.join(source_file, file)
        replica_file_path = os.path.join(replica_file, file)

        if file in f_replica:
            if compare_files(source_file_path, replica_file_path):
                log_message = f"{file} is up to date."
            else:
                os.remove(replica_file_path)
                shutil.copy2(source_file_path, replica_file_path)
                log_message = f"{file} has been updated."
        else:
            shutil.copy2(source_file_path, replica_file_path)
            log_message = f"{file} has been copied."

 # If the file exists in the replica, it compares the files.
 # If the files are the same, it registers that the file is up to date.
 # If the files are different, it removes the file in replica and copies the new file from source to replica.

        logging.info(log_message)
        print(log_message)

    for file in f_replica:
        if file not in f_source:
            os.remove(os.path.join(replica_file, file))
            log_message = f"{file} has been deleted."
            logging.info(log_message)
            print(log_message)
 # For each file in replica that is not in source, remove it and record the action.

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Folder synchronization program')
    parser.add_argument('--source', type=str, default="source", help='Source folder path')
    parser.add_argument('--replica', type=str, default="replica", help='Replica folder path')
    parser.add_argument('--log-file', type=str, default='log.txt', help='Log file path')
    parser.add_argument('--time-interval', type=int, default=60, help='Time interval for synchronization in seconds')
    args = parser.parse_args()

 # Defines arguments for the command line: source, replica, log-file and time-interval.

    logging.basicConfig(filename=args.log_file, level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')
    sync_folders(args.source, args.replica, args.log_file, args.time_interval)

 # Starts synchronizing the folders with the given arguments.