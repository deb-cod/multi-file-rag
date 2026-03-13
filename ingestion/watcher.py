from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from ingestion.ingest import ingest_document

class DocumentHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            print("New file detected:", event.src_path)
            ingest_document(event.src_path)

def start_watcher():

    path = "./documents"

    observer = Observer()
    observer.schedule(DocumentHandler(), path, recursive=True)
    observer.start()

    print("Watching documents folder...")

    while True:
        time.sleep(1)