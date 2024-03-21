import streamlit as st

def main():
    # Initialize session state
    if 'counter' not in st.session_state:
        st.session_state['counter'] = 0

    # Increment counter
    st.session_state['counter'] += 1

    # Display counter value
    st.write("Counter:", st.session_state['counter'])

if __name__ == "__main__":
    main()