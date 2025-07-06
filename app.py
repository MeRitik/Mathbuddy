from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains import LLMChain, LLMMathChain
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.callbacks import StreamlitCallbackHandler


load_dotenv()

# Streamlit Configurations
st.set_page_config(layout="centered", page_title="Chatbot", page_icon=":robot:", initial_sidebar_state="expanded")

# Load the Chat Model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3, streaming=True)

# Tools
wikipedia_wrapper = WikipediaAPIWrapper()
math_chain = LLMMathChain(llm=llm)

calc = Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for solving mathematical problems with pure mathematical expressions."
)

wikipedia = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching information on any topic with Wikipedia API."
)

prompt = """
    You are MathBuddy, a well renowned mathematician. You also happens to my friend.

    Your job is to help me understand and solve math problems with: 
    1. First solve the equation(s) to find the value(s) of variable(s)
    2. Then substitute these value(s) into the expression
    3. Output the resulting numerical expression only so that it can be evaluated by a calculator (without any variable)
    2. Step-by-step detailed explanation.
    3. Helpful tips and alternative ways when possible.
    4. Friendly tone.
    5. LaTeX style formatting for math (if available)


    Question: {question}
"""

prompt_template = PromptTemplate(template=prompt, input_variables=["question"])

chain = LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="A tool for solving math problems with clear, structured approach, step-by-step detailed explanation"
)

tools = [reasoning_tool, calc, wikipedia]

# Agents

# --- Initialize ---
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# Chat 
# -- Memory
if "messages" not in st.session_state:
    st.session_state.messages = [{
            "role": "assistant",
            "content": "Hey buddy! I can solve any math problem you throw at me. What would you like to solve?"
        }]


# -- Display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -- Input
question = st.chat_input("Enter your math problem here...")

# -- Solve
if question:
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.write(question)

    with st.spinner("👨🏻‍🔬Solving your problem..."):
        st_sb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = agent.run(question, callbacks=[st_sb])
        st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response, unsafe_allow_html=True) # For LaTeX