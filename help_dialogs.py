import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

@st.dialog("Help dialog", width="large")
def help_dialog():
    st.write("""
This dialog box provides detailed information and guidance about specific
interventions. It contains explanations and important considerations to help
users better understand and choose intervention values effectively.
""")

    st.markdown("""# Charts
It can also contain charts""")
    
    cols = st.columns((1,3,1))
    with cols[1]:
        f, ax = plt.subplots()
        ax.plot(np.random.randn(100))
        st.pyplot(f)

    st.markdown("""# Links
We can add [links to external websites](https://www.fixourfood.org)""")