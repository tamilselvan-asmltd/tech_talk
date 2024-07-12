import streamlit as st
import pandas as pd
import subprocess

# Function to load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to save selected rows to user_feedback.csv
def save_selected_rows(df):
    selected_df = df[df['Select'] == True]
    selected_df.drop(columns=['Select'], inplace=True)
    selected_df.to_csv('user_feedback.csv', index=False)

# Function to delete selected rows
def delete_selected_rows(df):
    df = df[df['Select'] == False]
    return df

# Load firewall logs data
def get_firewall_logs():
    firewall_logs = load_data('firewall_logs.csv')
    firewall_logs['Select'] = False
    return firewall_logs

# Load rules data
def get_rules_data():
    return load_data('/Users/tamilselvans/tech_talk/rules.csv')

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = get_firewall_logs()

if 'rules_df' not in st.session_state:
    st.session_state.rules_df = get_rules_data()

# Title of the app
st.title('Editable Firewall Logs Table')

# Layout for the top buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button('Traffic Generator'):
        try:
            subprocess.Popen(['python', '/Users/tamilselvans/tech_talk/firewall.py'])
            st.success('Traffic script is running in the background.')
        except Exception as e:
            st.error(f"Failed to run traffic script: {e}")

with col2:
    if st.button('Refresh'):
        st.session_state.df = get_firewall_logs()

# Display the table with checkboxes for each row
edited_df = st.data_editor(st.session_state.df, key='data_editor')

# Layout for the bottom buttons
col3, col4, col5 = st.columns([1, 1, 1])
with col3:
    if st.button('Save'):
        if edited_df['Select'].any():
            save_selected_rows(edited_df)
            st.success('Selected rows have been saved to user_feedback.csv')
        else:
            st.warning('No rows selected')

with col4:
    if st.button('Delete'):
        if edited_df['Select'].any():
            st.session_state.df = delete_selected_rows(edited_df)
            st.success('Selected rows have been deleted')
        else:
            st.warning('No rows selected')

with col5:
    if st.button('Run Model'):
        try:
            subprocess.run(['python', '/Users/tamilselvans/tech_talk/ml_model.py'], check=True)
            st.success('Model script has run successfully.')
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to run model script: {e}")

# Display rules.csv file as a table at the bottom
st.subheader('Rules Table')

if st.button('Refresh Rules Table'):
    st.session_state.rules_df = get_rules_data()

st.write(st.session_state.rules_df)
