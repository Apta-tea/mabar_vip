import streamlit as st
import pandas as pd
import sqlite3
import time


def _profile_content():
    st.header("Admin", divider=True)
    conn = sqlite3.connect('moba.db')
    query = "SELECT * FROM users"
    # Read SQL query into a DataFrame
    df = pd.read_sql_query(query, conn)
    # Close the connection
    conn.close()
    # Display the DataFrame
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
    submitted = st.button("Simpan", type="primary")
    if submitted:
        conn = sqlite3.connect('moba.db') 
        # Save DataFrame to SQLite database
        edited_df.to_sql('users', conn, if_exists='replace', index=False)
        # Close the connection
        conn.close()
        with st.spinner('Data disimpan!'):
            time.sleep(1)
        st.rerun()

