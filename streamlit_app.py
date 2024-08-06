import streamlit as st

# Initialize session state for the list if it doesn't exist
if 'my_list' not in st.session_state:
    st.session_state.my_list = []

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Text input for the item to be added
new_item = st.text_input("Add a new item to the list:")

# Add to List button
if st.button("Add to List"):
    if new_item:
        st.session_state.my_list.append(new_item)
        st.success(f'Added "{new_item}" to the list!')
    else:
        st.error("Please enter an item before adding to the list.")

# Display the list
st.write("### My List")
if st.session_state.my_list:
    for item in st.session_state.my_list:
        st.write(f"- {item}")
else:
    st.write("The list is empty.")
