import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
load_dotenv()

google_credential = os.getenv("GOOGLE_CREDENTIAL")


# Set up Google Sheets API credentials
def connect_to_gsheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(google_credential, scope)
    client = gspread.authorize(creds)
    return client

# Function to fetch data from Google Sheets
def fetch_data(sheet_name):
    client = connect_to_gsheets()
    sheet = client.open("UTPTrackerData").worksheet(sheet_name)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

# Function to add a new entry to Google Sheets
def add_entry(sheet_name, row_data):
    client = connect_to_gsheets()
    sheet = client.open("UTPTrackerData").worksheet(sheet_name)
    sheet.append_row(row_data)

# Streamlit app
st.title("UTP Tracker App")

# Navigation
category = st.sidebar.selectbox("Select Category", ["Events", "Clubs", "Achievements", "Exam Results", "Dashboard"])

# Event Form
if category == "Events":
    st.subheader("Add New Event")
    with st.form(key='event_form'):
        event_name = st.text_input("Event Name")
        date = st.date_input("Date")
        description = st.text_area("Description")
        involvement = st.selectbox("Involvement", ["Joined", "Organized", "Volunteered"])
        additional_info = st.text_input("Additional Info")
        submit_button = st.form_submit_button("Add Event")

        if submit_button:
            add_entry("Events", [event_name, str(date), description, involvement, additional_info])
            st.success("Event added successfully!")

# Clubs Form
elif category == "Clubs":
    st.subheader("Add New Club Involvement")
    with st.form(key='club_form'):
        club_name = st.text_input("Club Name")
        position = st.text_input("Position")
        club_description = st.text_area("Description")
        club_additional_info = st.text_input("Additional Info")
        submit_button = st.form_submit_button("Add Club")

        if submit_button:
            add_entry("Clubs", [club_name, position, club_description, club_additional_info])
            st.success("Club added successfully!")

# Achievements Form
elif category == "Achievements":
    st.subheader("Add New Achievement/Certification")
    with st.form(key='achievement_form'):
        achievement_name = st.text_input("Achievement Name")
        achievement_description = st.text_area("Description")
        submit_button = st.form_submit_button("Add Achievement")

        if submit_button:
            add_entry("Achievements", [achievement_name, achievement_description])
            st.success("Achievement added successfully!")

# Exam Results Form
elif category == "Exam Results":
    st.subheader("Add New Exam Result")
    with st.form(key='exam_result_form'):
        year_of_study = st.text_input("Year of Study (e.g., Foundation, 1st Year, etc.)")
        semester = st.number_input("Semester", min_value=1, max_value=12)
        gpa = st.number_input("GPA", format="%.2f", step=0.01)
        submit_button = st.form_submit_button("Add Exam Result")

        if submit_button:
            add_entry("Exam Results", [year_of_study, semester, gpa])
            st.success("Exam result added successfully!")

# Dashboard
elif category == "Dashboard":
    st.subheader("Dashboard Visualization")

    # Fetching data for visualization
    events_df = fetch_data("Events")
    clubs_df = fetch_data("Clubs")
    achievements_df = fetch_data("Achievements")
    exam_results_df = fetch_data("Exam Results")

    # Event Count Visualization
    event_counts = events_df['Involvement'].value_counts()
    st.subheader("Events Involvement Count")
    st.bar_chart(event_counts)

    # Exam Results Visualization
    st.subheader("Exam Results GPA Distribution")
    gpa_distribution = exam_results_df['GPA'].value_counts()
    plt.figure(figsize=(10, 5))
    plt.bar(gpa_distribution.index, gpa_distribution.values)
    plt.xlabel("GPA")
    plt.ylabel("Number of Students")
    plt.title("GPA Distribution")
    st.pyplot()

    # Achievement Count
    achievement_counts = achievements_df['Achievement Name'].value_counts()
    st.subheader("Achievements Count")
    st.bar_chart(achievement_counts)

    # Club Involvement Count
    club_counts = clubs_df['Club Name'].value_counts()
    st.subheader("Clubs Participation Count")
    st.bar_chart(club_counts)
