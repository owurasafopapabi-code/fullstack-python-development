# JSON Sample Manager

A beginner command-line Python application for managing laboratory sample records using JSON storage.

## Description

JSON Sample Manager is a menu-based command-line application that allows users to add, view, search, filter, and update laboratory sample records. The project uses Python dictionaries and lists to structure data, and JSON to save records persistently.

This project was built as part of my Fullstack Python Development mentorship journey to practice clean program structure, input validation, file handling, JSON storage, and Git/GitHub workflow.

## Features

- Add new sample records
- View all saved sample records
- Search for a sample by sample ID
- Filter samples by interpretation: Low, Normal, or High
- Update a sample result value
- Automatically recalculate interpretation after updating a result
- Save records persistently using JSON
- Load saved records when the program starts
- Validate empty text input
- Validate numeric result input

## Technologies Used

- Python
- JSON
- Git
- GitHub
- VS Code

## Project Structure

```text
json_sample_manager/
├── json_sample_manager.py
├── samples.json
└── README.md
```

## How to Run

- From the main repository folder, run:
```bash
python projects/json_sample_manager/json_sample_manager.py
```

or open the project folder in VS Code and run:
```bash
python json_sample_manager.py
```

## Sample Data Format

Records are stored in `samples.json` as a list of dictionaries:
```JSON
[
    {
        "sample_id": "S001",
        "patient_name": "Ama Mensah",
        "test_name": "Fasting Blood Sugar",
        "result_value": 95.0,
        "interpretation": "Normal"
    }
]
```

## What I Learned

Through this project, I practiced:

- organizing code into functions
- using a menu system
- validating user input
- storing records as dictionaries
- managing multiple records with lists
- saving and loading data with JSON
- searching and filtering records
- updating records and dependent fields
- using Git and GitHub for version control

## Project Status

This is a beginner learning project. It is not production-ready, but it demonstrates important foundations for future backend and fullstack development.

## Future Improvements

Planned improvements include:

- Add delete sample functionality
- Prevent duplicate sample IDs
- Add better error handling for corrupted JSON files
- Add automated tests
- Improve folder structure further
- Later migrate storage from JSON to a database

## Author

Kwadwo Safo