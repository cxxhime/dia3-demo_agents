import streamlit as st
from llm_agent import ConversationAgent


st.set_page_config(page_title="Jarvis")
st.title("Barbe-Quasar")

class ConversationAgent:
	def __init__(self):
		self.conversation_agent = ConversationAgent()
  
	conversation_agent = st.session_state.conversation_agent

	for message in conversation_agent.conversation_history:
		if message["role"] != "system":
			with st.chat_message(message["role"]):
				st.markdown(message["content"])
    
	user_input = st.chat_input(
		"Que veux tu moussaillon ?",
		accept_file=False,
		accept_audio=False,
	)
	if user_input :
		conversation_agent.ask_llm(user_input)
  
		with st.chat_message("user"):
			st.markdown(user_input)
   
		with st.chat_message("system"):
			st.markdown(conversation_agent.conversation_history[-1]["content"])

