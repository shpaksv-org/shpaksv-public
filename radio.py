import streamlit as st

radio = st.radio('Selecte your favorite radio', options=('radio ga ga', 'radio', 'tapok')
if radio == "radio ga ga":
  st.video('youtube.com/watch?v=azdwsXLmrHE')
elif radio == "radio":
  st.video('https://www.youtube.com/watch?v=z0NfI2NeDHI')
else:
  st.video('https://www.youtube.com/watch?v=fV8d4Grhej8')
