import streamlit as st
import numpy as np
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.stateful_button import button
from streamlit_theme import st_theme
import matplotlib.pyplot as plt

def nested_sliders(labels,
                         key,
                         min_value=0,
                         max_value=100,
                         value=0,
                         help_dialog=None,
                         ):
    """Creates nested sliders which are expanded with a checkbox
    
    Parameters
        ----------
        labels : str or list of str
            Labels for the sliders. First label is for the main slider,
            subsequent labels are for nested sliders shown when checkbox is
            checked
        key : str
            Key for the widget
        min_value : int or float, optional
            Minimum value for all sliders, by default 0
        max_value : int or float, optional
            Maximum value for all sliders, by default 100
        value : int or float, optional
            Initial value for all sliders, by default 0
        Returns
        -------
        list
            Returns list of values for all sliders, repeating the value of the
            first slider for all other sliders if checkbox is not checked.
    
    """

    if key+"_is_open" not in st.session_state:
        st.session_state[key+"_is_open"] = False
    if key+"_value_base" not in st.session_state:
        st.session_state[key+"_value_base"] = 0
    
    if st.session_state[key+"_is_open"]:
        icon = "➖"
    else:
        icon = "➕"

    # Convert labels to list if it is a string
    if np.isscalar(labels):
        labels = [labels]

    # Initialize values
    values = []

    col_ratio = (1,3,6)
    cols = st.columns(col_ratio)

    with cols[2]:
        value_base = st.slider(labels[0],
            min_value=min_value,
            max_value=max_value,
            value=value,
            disabled=st.session_state[key+"_is_open"],
            label_visibility='collapsed',
            key=key+"_slider_0"
            )
        
    with cols[0]:
        if len(labels) > 1:
            if st.button(
                label=icon,
                type="tertiary",
                key=key+"opener_button_icon"):
                
                st.session_state[key+"_is_open"] = not st.session_state[key+"_is_open"]
                st.rerun()

    with cols[1]:
        if help_dialog is not None:
            if st.button(
                label=labels[0],
                type="tertiary",
                key=key+"opener_button_text"):
                    help_dialog()
                # st.session_state[key+"_is_open"] = not st.session_state[key+"_is_open"]
                # st.rerun()
        else:
            st.text(labels[0])            
        
    if st.session_state[key+"_is_open"]:
        for i, l in enumerate(labels[1:]):

            cols_nested = st.columns(col_ratio)

            with cols_nested[1]:
                st.caption(labels[i+1])
            
            with cols_nested[2]:
                val = st.slider(
                    l,
                    min_value=min_value,
                    max_value=max_value,
                    value=value_base,
                    label_visibility='collapsed',
                    key=key+"_slider_"+l
                    )
                values.append(val)

        return values        


    else:
        if len(labels) > 1:
            return [value_base for i in range(len(labels)-1)]
        else:
            return value_base        

def segmented_control_with_checkbox(labels,
                                    options,
                                    key_preffix="",
                                    help_dialog=None):
    """Creates nested segment controls which are expanded with a checkbox
    
    Parameters
        ----------
        labels : str or list of str
            Labels for the sement controls. First label is for the main control,
            subsequent labels are for nested controls shown when checkbox is
            checked
        options : list of str
            Options for the segment controls
        key_preffix : str, optional
            String to append to the key for the widgets, by default ""
        help_dialog : function, optional
    
        Returns
        -------
        list
            Returns list of values for all controls, repeating the value of the
            first slider for all other controls if checkbox is not checked.
    
    """

    # Convert labels to list if it is a string
    if np.isscalar(labels):
        labels = [labels]

    # Initialize values
    values = []

    col_ratio = (1e-6,4,7,1)
    cols = st.columns(col_ratio)

    with cols[1]:
        if len(labels) > 1:
            open = button(
                    label=labels[0],
                    type="tertiary",
                    key=key_preffix + "button_segment_" + labels[0],
                    )
        else:
            st.text(labels[0])
            open = False

    with cols[2]:
        value_base = st.segmented_control(
            labels[0],
            options=options,
            disabled=open,
            label_visibility='collapsed',
            format_func=lambda x: "‎ "*6,
            key=key_preffix + "segmented_control_" + labels[0],
            default=options[0]
            )
        
    with cols[3]:
        if st.button(":information_source:", key=key_preffix + "help_button_" + labels[0], type="tertiary"):
            if help_dialog is not None:
                help_dialog()

    if open:
        for i, l in enumerate(labels[1:]):

            cols_nested = st.columns(col_ratio)
            with cols_nested[1]:
                st.caption(labels[i+1])
            with cols_nested[2]:
                val = st.segmented_control(
                    l,
                    options=options,
                    default=value_base,
                    label_visibility='collapsed',
                    key=key_preffix + "segmented_control_"+l,
                    format_func=lambda x: "‎ "*6
                    )
                values.append(val)

        return values

    else:
        if len(labels) > 1:
            return [value_base for i in range(len(labels)-1)]
        else:
            return value_base

