import streamlit as st
import pandas as pd
import sqlite3
#from streamlit_option_menu import option_menu

def _dashboard_content():
   st.header("Dashboard", divider=True)
   st.write("Selamat datang di Dashboard!")
   conn = sqlite3.connect('moba.db')
   query = "SELECT Nama, COUNT(id) AS FREQ FROM mabar_log WHERE date > DATETIME('now', '-30 day') GROUP BY Nama"
   # Read SQL query into a DataFrame
   df1 = pd.read_sql_query(query, conn)
   # Close the connection
   conn.close()
   chart_data = pd.DataFrame(
    {
        "VIP Member": df1.Nama,
        "Freq": df1.FREQ,
    }
   )
   st.bar_chart(chart_data, x="VIP Member", y="Freq")