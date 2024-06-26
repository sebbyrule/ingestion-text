Here's how you can use the script:
python file_copier.py /path/to/project/root output.txt --ignore-folders .git node_modules --ignore-files .gitignore README.md --log-file my_log.log --log-level DEBUG --max-workers 4

This command will traverse the project structure starting from /path/to/project/root, copy the contents of each file into output.txt, and ignore the .git and node_modules folders, as well as the .gitignore and README.md files.

