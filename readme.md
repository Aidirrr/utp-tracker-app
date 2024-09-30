# UTPTrackerApp

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview
The **UTPTrackerApp** is a web application designed for students of Universiti Teknologi PETRONAS (UTP) to manage and visualize their academic and extracurricular achievements. This app allows users to track events they have joined, organized, or volunteered for, club involvements, certifications, and exam results, all in one place.

## Features
- **Event Tracking**: Add and manage events you've joined, organized, or volunteered for, including details like name, date, description, involvement, and additional information.
- **Club Involvement**: Record your participation in clubs and societies, including your position, description, and additional info.
- **Achievements/Certifications**: Keep track of your achievements and certifications with descriptions.
- **Exam Results**: Store and visualize your GPA, year of study, and semester results.
- **Data Visualization**: Generate visual representations of your data for better insight into your involvement at UTP.

## Technologies Used
- **Python**: Programming language used for the backend.
- **Streamlit**: Framework for building the web application interface.
- **gspread**: Library for accessing Google Sheets.
- **pandas**: Library for data manipulation and analysis.
- **matplotlib**: Library for data visualization.
- **Google Cloud Platform**: For hosting Google Sheets and API management.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/utp-tracker-app.git
   cd utp-tracker-app

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   
4. **Set Up Google Sheets API**:
- Enable the Google Sheets API and Google Drive API in the Google Cloud Console.
- Create credentials (service account) and download the ```credentials.json``` file.
- Share your Google Sheets file with the service account email.

5. **Run the Application**:
   ```bash
   streamlit run app.py
   
## Usage

- Open your web browser and go to ```http://localhost:8501``` to access the application.
- Follow the prompts to add, view, and visualize your events, club involvements, achievements, and exam results.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.



   