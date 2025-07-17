import streamlit as st
from chatbot import ChatbotAssistant, launch_to_mars # Make sure chatbot.py is present with these

# Load the chatbot only once
@st.cache_resource
def load_chatbot():
    assistant = ChatbotAssistant('intents.json', function_mappings={'launch_to_mars': launch_to_mars})

    assistant.parse_intents()
    assistant.load_model('chatbot_model.pth', 'dimensions.json')
    return assistant

assistant = load_chatbot()

# Streamlit UI
st.title("🧠 AI Buddy")
st.markdown("Type your message below and press Enter.")

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("", "")

if user_input:
    if user_input.lower() == '/quit':
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", "Session ended."))
    else:
        response = assistant.process_message(user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", response))

# Display chat history with yellow "You"
for speaker, msg in st.session_state.history:
    if speaker == "You":
        st.markdown(
            f'<span style="color: #FFD600; font-weight: bold;">{speaker}:</span> {msg}',
            unsafe_allow_html=True
        )
    else:
        st.markdown(f"**{speaker}:** {msg}")
