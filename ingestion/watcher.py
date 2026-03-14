import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from ingestion.ingest import ingest_document


DOCUMENT_FOLDER = "./documents"


def wait_for_file_complete(file_path):
    """
    Wait until file copy finishes.
    Prevents PermissionError when watchdog detects file early.
    """

    previous_size = -1

    while True:
        try:
            current_size = os.path.getsize(file_path)
            if current_size == previous_size:
                break
            previous_size = current_size
            time.sleep(1)

        except FileNotFoundError:
            time.sleep(1)


def ingest_urls(file_path):
    """
    Read URLs from a text file and ingest them
    """
    print(f"\nProcessing URL list: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        urls = f.readlines()
    for url in urls:
        url = url.strip()
        if not url:
            continue
        try:
            print(f"Ingesting URL: {url}")
            ingest_document(url)
        except Exception as e:
            print(f"Error ingesting URL {url}: {e}")

class DocumentHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return
        file_path = event.src_path
        print(f"\nNew file detected: {file_path}")
        wait_for_file_complete(file_path)

        try:
            # If file contains URLs
            if file_path.endswith(".urls") or file_path.endswith("urls.txt"):
                ingest_urls(file_path)
            else:
                ingest_document(file_path)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")


def start_watcher():

    print("Watching documents folder...")
    event_handler = DocumentHandler()
    observer = Observer()
    observer.schedule(event_handler, DOCUMENT_FOLDER, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        print("Watcher stopped.")

    observer.join()