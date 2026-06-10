# Repo Scanner

A Python-based repository analysis tool that scans a directory and generates useful repository statistics.

## Features

* Counts Python, JSON, Text, and Markdown files
* Calculates total lines of code
* Finds the largest file in the repository
* Generates a repository analysis report

## Technologies Used

* Python
* Pathlib
* File Handling

## How It Works

1. Enter a repository path.
2. The program scans all files recursively.
3. It counts supported file types.
4. It calculates line counts.
5. It identifies the largest file.
6. It prints a summary report.

## Usage

Run the script:

```bash
python repo_scanner.py
```

Then enter the repository path when prompted.

Example:

```text
Enter the path: C:\Projects\MyRepository
```

## Sample Output

```text
========================================
REPOSITORY ANALYSIS REPORT
========================================

Total Files: 5

Python Files   : 2 | Lines: 100
JSON Files     : 1 | Lines: 15
Text Files     : 1 | Lines: 10
Markdown Files : 1 | Lines: 20

Total Lines: 145

Largest File:
main.py - 70 lines

========================================
```

## Future Improvements

* Support more programming languages
* Export reports to a file
* Show directory statistics
* Generate visual reports
