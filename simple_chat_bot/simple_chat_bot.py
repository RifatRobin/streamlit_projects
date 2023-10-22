import streamlit as st

st.markdown("# Mirror Bot ❄️")
st.sidebar.markdown("# Mirror Bot ❄️")

#initializing the chat history
if "messages" not in st.session_state:
    st.session_state.messages =[]

#display the chat messages from the history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# React to user input
if prompt := st.chat_input("What is up?"):
    # We used the := operator to assign the user's input to the prompt variable
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

response = f"Bot: {prompt}"
# Display assistant response in chat message container

with st.chat_message("assistant"):
    st.markdown(response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})