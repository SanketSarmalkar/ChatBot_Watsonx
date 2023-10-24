# Import langchain dependencies
# from langchain.document_loaders import PyPDFLoader
# from langchain.indexes import VectorstoreIndexCreator
# from langchain.chains import RetrievalQA
# from langchain.embeddings import HuggingFaceEmbedding
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# UI using Streamlit
import streamlit as st

# bring the watsonx interface
# from watsonxlangchain import LangChainInterface

# UI
st.title('Ask WatsonX a question')

# storing older messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# display the older messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Build a prompt input template to display the prompts
prompt = st.chat_input('Enter your question here')

# if the user hits enter
if prompt:
    st.chat_message('user').markdown(prompt)
    # store the prompt in the session state
    st.session_state.messages.append({
        'role': 'user',
        'content': prompt
    })