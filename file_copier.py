import os
import argparse
import logging
from typing import List, Optional
import concurrent.futures
import mimetypes

def setup_logging(log_file: str, log_level: str) -> None:
    """Set up logging configuration."""
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level}')
    
    logging.basicConfig(
        filename=log_file,
        level=numeric_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def is_text_file(file_path: str) -> bool:
    """Check if a file is a text file based on its MIME type."""
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is not None and mime_type.startswith('text/'):
        return True
    
    # Add common text file extensions that might not be recognized by mimetypes
    text_extensions = {'.txt', '.md', '.py', '.js', '.jsx', '.ts', '.tsx', '.html', '.css', '.json', '.xml', '.yaml', '.yml'}
    return os.path.splitext(file_path)[1].lower() in text_extensions

def copy_file_contents(file_path: str, out_file) -> None:
    """Copy the contents of a file to the output file."""
    try:
        if is_text_file(file_path):
            with open(file_path, 'r', encoding='utf-8') as in_file:
                contents = in_file.read()
                out_file.write(f"File: {file_path}\n\n")
                out_file.write(contents)
                out_file.write("\n\n")
                logging.info(f"Successfully copied contents of {file_path}")
        else:
            logging.warning(f"Skipped non-text file: {file_path}")
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")

def process_directory(
    root_dir: str,
    output_file: str,
    ignore_folders: List[str] = [],
    ignore_files: List[str] = [],
    max_workers: Optional[int] = None
) -> None:
    """
    Recursively traverse the root directory, copy the contents of each file to the output file,
    and ignore specified folders and files.
    """
    with open(output_file, 'w', encoding='utf-8') as out_file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for root, dirs, files in os.walk(root_dir):
                # Remove ignored folders from the list of directories
                dirs[:] = [d for d in dirs if d not in ignore_folders]

                for file in files:
                    if file not in ignore_files:
                        file_path = os.path.join(root, file)
                        futures.append(executor.submit(copy_file_contents, file_path, out_file))

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)

def main():
    parser = argparse.ArgumentParser(description="Copy file contents to a single text file.")
    parser.add_argument("root_dir", help="Root directory of the project structure")
    parser.add_argument("output_file", help="Output text file to store file contents")
    parser.add_argument("--ignore-folders", nargs="+", default=[], help="Folders to ignore (space-separated)")
    parser.add_argument("--ignore-files", nargs="+", default=[], help="Files to ignore (space-separated)")
    parser.add_argument("--log-file", default="file_copier.log", help="Log file name")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Logging level")
    parser.add_argument("--max-workers", type=int, default=None, help="Maximum number of worker threads")

    args = parser.parse_args()

    setup_logging(args.log_file, args.log_level)
    
    logging.info(f"Starting file copying process from {args.root_dir} to {args.output_file}")
    process_directory(args.root_dir, args.output_file, args.ignore_folders, args.ignore_files, args.max_workers)
    logging.info("File copying process completed")

if __name__ == "__main__":
    main()