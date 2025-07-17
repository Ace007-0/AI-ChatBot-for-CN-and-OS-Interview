# AI-ChatBot-for-CN-and-OS-Interview

Welcome to the **AI Buddy** project! This is a conversational AI assistant built using Python, PyTorch, and Streamlit, tailored to help users prepare for interviews focused on Operating Systems (OS) and Computer Networks (CN). The bot is designed to provide concise answers and explanations for a wide range of fundamental OS and CN concepts.

## Features

- **Conversational Interface**: Chat with the bot through an intuitive Streamlit web UI.
- **Coverage of Key Topics**: Includes OS concepts like processes, threads, scheduling, memory management, deadlocks, file systems, and synchronization, as well as CN topics such as the OSI model, protocols, encryption, networking devices, and security.
- **Dynamic Response Generation**: Uses an intent-based JSON to identify queries and provide relevant, structured answers.
- **Custom Functions Integration**: Supports function mappings for specialized tasks or fun responses.
- **History Tracking**: View your conversation context during the session.

## Quick Start

### 1. **Clone the Repository**
```bash
git clone https://github.com/Ace007-0/AI-ChatBot-for-CN-and-OS-Interview.git
cd AI-ChatBot-for-CN-and-OS-Interview
```

### 2. **Install Requirements**
```bash
pip install -r requirements.txt
# Make sure you have nltk data: wordnet, punkt
python -m nltk.downloader wordnet punkt
```

### 3. **Run the Application**
```bash
streamlit run app.py
```
Open your browser and navigate to the URL provided by Streamlit.

## Project Structure

| File          | Description                                              |
|---------------|---------------------------------------------------------|
| `app.py`      | Streamlit app for the web-based user interface.         |
| `chatbot.py`  | Core chatbot logic: parsing intents, training/loading the model, and processing user input. |
| `intents.json`| Contains the curated intents, patterns, and responses for interview question coverage.  |

## How It Works

1. **Intent Parsing**: The bot uses `intents.json` to associate sample patterns with intent tags and select appropriate responses.
2. **Preprocessing**: User queries are tokenized and lemmatized for accurate intent recognition.
3. **Model Inference**: A small neural network predicts the user's intent from their input.
4. **Response Generation**: The bot selects a suitable answer (or runs a mapped function) and returns it to the user.

## Customization

- **Expand the Question Set**: Add new intents, questions, and responses by editing `intents.json`.
- **Retrain the Model**: Modify the model or retrain on your updated dataset through `chatbot.py`.
- **Add Functions**: Map intents to Python functions for interactive or dynamic behavior.

## Sample Questions Supported

- *What is a process in OS?*
- *Explain types of CPU scheduling.*
- *Describe the OSI model layers.*
- *What is VPN?*
- *Difference between thread and process.*

## Images
<img width="778" height="448" alt="image" src="https://github.com/user-attachments/assets/62ae485d-dff5-4bea-9701-c1e7b3762197" />
<img width="811" height="668" alt="image" src="https://github.com/user-attachments/assets/c94dad05-18c7-4f08-997d-e7c863c84a0d" />
<img width="807" height="672" alt="image" src="https://github.com/user-attachments/assets/6323b33a-c242-42f9-a1e3-b4b451bc6eea" />




## Acknowledgments

- Built with [Streamlit](https://streamlit.io), [PyTorch](https://pytorch.org), and [NLTK](https://www.nltk.org).
- Inspired by classic interview preparation resources for OS and CN fundamentals.


## Contributing

Feel free to fork the repository, open issues, or submit pull requests for improvements and additional functionality!

## Contact

For questions or suggestions, please reach out via the repository issues or mail.
