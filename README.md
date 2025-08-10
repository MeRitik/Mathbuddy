# MathBuddy

MathBuddy is an interactive AI-powered chatbot web app designed to help users solve and understand math problems step-by-step. Built with Streamlit and LangChain, MathBuddy leverages OpenAI's GPT models and Wikipedia to provide detailed explanations, calculations, and helpful tips in a friendly, conversational manner.

## Features

- **Conversational Math Assistant:**
  - Ask any math question in natural language.
  - Get step-by-step solutions, explanations, and tips.
  - Friendly, approachable responses with LaTeX-style math formatting.

- **Integrated Tools:**
  - **Calculator:** Solves mathematical expressions and equations.
  - **Wikipedia Search:** Fetches relevant information for math-related queries.
  - **Reasoning Tool:** Provides structured, detailed explanations for complex problems.

- **Modern UI:**
  - Chat interface powered by Streamlit's chat components.
  - Real-time response streaming and progress indication.

## How It Works

1. **User Input:** Enter your math problem in the chat input box.
2. **Processing:** MathBuddy uses a combination of reasoning, calculation, and Wikipedia search tools to solve your query.
3. **Response:** The assistant replies with a step-by-step solution, explanations, and tips, using LaTeX formatting for math expressions.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd mathbuddy
```

### 2. Install Dependencies
It is recommended to use a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## File Structure

- `app.py` — Main Streamlit application file.
- `requirements.txt` — Python dependencies.
- `LICENCE` — License information.

## Requirements
- Python 3.8+
- OpenAI API key

## Customization
- You can modify the prompt in `app.py` to change the assistant's personality or instructions.
- Add or remove tools in the `tools` list to extend MathBuddy's capabilities.

## Troubleshooting
- **API Errors:** Ensure your OpenAI API key is valid and has sufficient quota.
- **Wikipedia Tool Issues:** Requires internet access to fetch data.
- **LaTeX Rendering:** Streamlit's `st.markdown` supports basic LaTeX. For complex math, use `st.latex()`.

## License
See `LICENCE` for details.

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [OpenAI](https://openai.com/)
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)

---

Enjoy learning and solving math with MathBuddy!
