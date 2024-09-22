import streamlit as st
import pandas as pd
import sqlite3
import time

def clear_multi():
    st.session_state.multiselect = []
    return

def _mabar_content():
    st.header("Mabar VIP", divider=True)
    conn = sqlite3.connect('moba.db')
    query = "SELECT * FROM members WHERE Jml_Paket > 0"
    # Read SQL query into a DataFrame
    df = pd.read_sql_query(query, conn)
    # Close the connection
    conn.close()
    # Display the DataFrame
    party = st.empty()
    party = st.multiselect("Pilihan Party Mabar:", df.Nama, max_selections=5, key="multiselect")
    st.write("You selected:", party)
    st.session_state
    submitted = st.button("Finish Game", type="primary", use_container_width=False)
    if submitted:
        if not party:
            st.write('Anda belum memilih anggota party')
            time.sleep(2)
            st.rerun()
        else: 
            conn = sqlite3.connect('moba.db')
            cursor = conn.cursor()
            for name in party:
                cursor.execute("UPDATE members SET jml_paket = jml_paket - 1 WHERE Nama = ?", (name,))                    
                conn.commit()
                cursor.execute("INSERT INTO mabar_log (Nama) values (?)",(name,))
                conn.commit()
            conn.close()
            st.balloons()   
            progress_text = "Data diperbaharui..."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.03)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(2)
            my_bar.empty()
            del st.session_state.multiselect
            st.session_state.multiselect = []
            st.rerun()

    