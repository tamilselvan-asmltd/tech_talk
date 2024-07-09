import streamlit as st
import pandas as pd

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

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = get_firewall_logs()

# Title of the app
st.title('Editable Firewall Logs Table')

# Refresh button
if st.button('Refresh Table'):
    st.session_state.df = get_firewall_logs()

# Display the table with checkboxes for each row
edited_df = st.data_editor(st.session_state.df, key='data_editor')

# Save button
if st.button('Save Selected Rows'):
    if edited_df['Select'].any():
        save_selected_rows(edited_df)
        st.success('Selected rows have been saved to user_feedback.csv')
    else:
        st.warning('No rows selected')

# Delete button
if st.button('Delete Selected Rows'):
    if edited_df['Select'].any():
        st.session_state.df = delete_selected_rows(edited_df)
        st.success('Selected rows have been deleted')
    else:
        st.warning('No rows selected')
