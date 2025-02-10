import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from streamlit_extras.stylable_container import stylable_container
from nested_sliders import nested_sliders, segmented_control_with_checkbox
from help_dialogs import help_dialog

# ----------
#    Main
# ----------

st.set_page_config(layout='wide',
                   initial_sidebar_state='expanded',
                   page_title="Agrifood Calculator",
                   page_icon="images/fof_icon.png")

cols = st.columns(4)

# Nested sliders
with cols[0]:
    params_dict={}
    with st.container(border=True, height=800):
        with st.expander("Consumption :spaghetti:", expanded=True):
            params_dict["Beef and lamb"], params_dict["Pork, chicken, turkey"] = \
            nested_sliders(
                ['Meat',
                 'Beef and lamb',
                 'Pork, chicken, turkey'],
                min_value=0,
                max_value=100,
                value=0,
                key="meat",
                help_dialog=help_dialog
                )
            params_dict["Milk"], params_dict["Cheese"], params_dict["Eggs"] = \
            nested_sliders(
                ['Dairy', 'Milk', 'Cheese', 'Eggs'],
                min_value=0,
                max_value=100,
                value=0,
                key="dairy"
                )
            
            params_dict["Fruits and vegetables"] = \
            nested_sliders(
                "Fruits and vegetables",
                min_value=0,
                max_value=100,
                value=0,
                key="fruits",
                help_dialog=help_dialog
                )
           
            
        st.write(params_dict)

# Nested segmented controls
with cols[1]:
    with st.container(border=True, height=800):
        with st.expander("Consumption :spaghetti:", expanded=True):
            with stylable_container(
                key="stylable_container_1",
                css_styles=f"""
                    /* Style for enabled segmented control */
                    [data-testid="stBaseButton-segmented_controlActive"]{{
                        background-color: rgba(30, 165, 30);
                        border-color: #000000;
                    }}

                    /* Style for disabled segmented control */
                    [data-testid="stBaseButton-segmented_controlActive"][disabled]{{
                        border-color: #000000;
                        opacity: 0.1;
                    }}
                    
                    """
                    ):
                
                params_dict["Beef and lamb"], params_dict["Pork, chicken, turkey"] = \
                segmented_control_with_checkbox(
                    ['Meats ', 'Beef and lamb', 'Pork, chicken, turkey'],
                    options=np.arange(1,5),
                    key_preffix="d_",
                    help_dialog=help_dialog
                    )

            with stylable_container(
                key="stylable_container_2",
                css_styles=f"""
                    /* Style for enabled segmented control */
                    [data-testid="stBaseButton-segmented_controlActive"]{{
                        background-color: rgba(165, 30, 30);
                        border-color: #000000;
                    }}

                    /* Style for disabled segmented control */
                    [data-testid="stBaseButton-segmented_controlActive"][disabled]{{
                        border-color: #000000;
                        opacity: 0.1;
                    }}"""
                    ):
                
                params_dict["Milk"], params_dict["Cheese"], params_dict["Eggs"] = \
                segmented_control_with_checkbox(
                    ['Dairy ', 'Milk', 'Cheese', 'Eggs'],
                    options=np.arange(1,5),
                    key_preffix="d_",
                    help_dialog=help_dialog
                    )
            
            with stylable_container(
                key="stylable_container_3",
                css_styles=f"""
                    /* Style for enabled segmented control */
                    [data-testid="stBaseButton-segmented_controlActive"]{{
                        background-color: rgba(30, 30, 165);
                        border-color: #000000;
                    }}

                    /* Style for disabled segmented control */
                    [data-testid="stBaseButton-segmented_controlActive"][disabled]{{
                        border-color: #000000;
                        opacity: 0.1;
                    }}"""
                    ):

                params_dict["Fruits and vegetables"] = \
                segmented_control_with_checkbox(
                    "Fruits and vegetables ",
                    options=np.arange(1,5),
                    key_preffix="d_",
                    help_dialog=help_dialog
                    )
        st.write(params_dict)
            
