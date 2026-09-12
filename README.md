# File Organizer

A simple Python program that automatically organizes files into different folders based on their file extensions.

## Features

* Organizes files by type
* Automatically creates destination folders when needed
* Skips existing folders
* Prevents files from being overwritten
* Supports multiple common file types
* Uses `Misc` for unrecognized file types

## Categories

| Category  | File Types                               |
| --------- | ---------------------------------------- |
| Images    | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp` |
| Documents | `.txt`, `.docx`, `.pdf`                  |
| Code      | `.py`, `.html`                           |
| Videos    | `.mp4`, `.mkv`, `.mov`, `.avi`           |
| Misc      | Other file types                         |

## How It Works

The program asks for the path of a folder and then checks the files directly inside it.

Each file is:

1. Identified by its extension
2. Assigned to a category
3. Given a destination folder
4. Moved to that folder

If the destination folder doesn't exist, it is created automatically.

Subfolders are currently skipped.

## Requirements

* Python 3.x
* No external libraries required

## Usage

Run the program:

```bash
python main.py
```

Then enter the folder you want to organize:

```text
Enter folder to be organized: C:\Users\YourName\Downloads
```

### Example

Before:

```text
Downloads/
├── photo.jpg
├── assignment.pdf
├── video.mp4
├── program.py
└── random.xyz
```

After:

```text
Pictures/
└── photo.jpg

Documents/
└── assignment.pdf

Videos/
└── video.mp4

Code/
└── program.py

Misc/
└── random.xyz
```

## Current Limitations

* Only files directly inside the selected folder are organized.
* Subfolders are not processed.
* Files are classified using their extensions.
* Destination folders are currently defined in the code.
* Files with duplicate names are skipped.
* The program currently uses a terminal interface.

## Future Plans

* GUI interface
* Windows File Explorer integration
* More file categories
* Custom destination folders
* Better duplicate-file handling
* Dry-run/preview mode
* Logging

## Version

**v1.0 — Initial Release**

