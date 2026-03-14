import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from ingestion.ingest import ingest_document


DOCUMENT_FOLDER = "./documents"


def wait_for_file_complete(file_path):
    """
    Wait until file copy finishes.
    This prevents PermissionError when watchdog detects file early.
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


class DocumentHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return
        file_path = event.src_path
        print(f"\nNew file detected: {file_path}")
        # wait until file copy finishes
        wait_for_file_complete(file_path)

        try:
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