import streamlit as st
import pandas as pd

def main():

    # Make Some Data
    st.title("Demo for an Intern")

    # Show me the code
    st.subheader("Show me the code")
    st.code("""
def main():
    st.title("Demo for an Intern")

    # Show me the code
    st.subheader("Show me the code")
    '''
    THATS THIS SECTION
    '''
            
    # Show me the Editors
    st.subheader("Show me the Editor")
    data_editor_key = "data_editor"
    data_frame = pd.DataFrame({
        'column 1': [1, 2, 3, 4],
        'column 2': [10, 20, 30, 40],
        'column 3': [100, 200, 300, 400]
    })
    st.text(f"data editor key is {data_editor_key}")
    st.data_editor(data_frame, key=data_editor_key)
    
    # Show me the State Changes of the Data Editor
    st.subheader("Show me your state changes")
    st.write(st.session_state[data_editor_key])

if __name__ == "__main__":
    main()
"""
    )
    # Show me the Editors
    st.subheader("Show me the Editor")
    data_editor_key = "data_editor"
    data_frame = pd.DataFrame({
        'column 1': [1, 2, 3, 4],
        'column 2': [10, 20, 30, 40],
        'column 3': [100, 200, 300, 400]
    })
    st.text(f"data editor key is {data_editor_key}")
    st.data_editor(data_frame, key=data_editor_key)
    
    # Show me the State Changes of the Data Editor
    st.subheader("Show me your state changes")
    st.write(st.session_state[data_editor_key])

if __name__ == "__main__":
    main()