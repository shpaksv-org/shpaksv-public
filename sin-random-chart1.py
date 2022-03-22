import streamlit as st
import pandas as pd
import numpy as np


t = np.arrange(0, 10*np.pi, 0.05)
data = pd.DataFrame({
  "rand": np.random.rand(1, len(t))[0] + 10,
  "sin+rand": np.random.rand(1, len(t))[0] + 3*np.sin(t) + np.sin(t * 0.5)
})

st.line_chart(data)
