import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )
+Simple

valor = int(input('ingrsaa:  '))


def funcion_1():
    print(1)

def funcion_2():
    print(2)

funcion_1() if valor > 0 else funcion_2()

print(espero)


            dflen = df[df['codreq'].str.len() == 8]
            dflen = len(dflen)


                        df = df[df['codreq'].str.len() == 8]