# Folder Synchronization Project

Folder Sync is a program to synchronize the content of a source folder with a replica folder. The program compares the files in the two folders and copies, updates, or removes files as needed to keep the replica identical to the source.  

## Installation

### Prerequisites
 * Python 3.x

### Installation Steps
 1. Clone the repository
 2. Install dependencies

## Usage
 
 To synchronize two folders, use the following command:
  
  python sync_folders.py --source /path/to/source --replica /path/to/replica --log-file /path/to/log.txt --time-interval 60

 ## Arguments
  
 * --source: Path to the source folder.
 * --replica: Path to the replica folder.
 * --log-file: Path to the log file.
 * --time-interval: Time interval (in seconds) for synchronization.

 # Example

 python sync_folders.py --source ./source --replica ./replica --log-file ./sync.log --time-interval 30