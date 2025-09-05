# Cold-Email-Generator--Gen-AI:
  A Streamlit app that takes a job posting URL, extracts the role/skills/experience with an LLM, and drafts a tailored cold email. It also adds a “Portfolio highlights”     section by matching required skills to your own links using embeddings + FAISS.

Features:
  Paste a careers-page URL
  Clean and normalize the scraped text
  Extract role, skills, experience with LangChain + Groq’s Llama-3.3-70B Versatile
  Generate a personalized cold email to the hiring manager
  Insert a Portfolio highlights block with links selected via Sentence Transformers (all-MiniLM-L6-v2) + FAISS


Tech stack:
  UI: Streamlit
  LLM: Groq (Llama-3.3-70B Versatile) via langchain-groq
  Retrieval: Sentence Transformers (all-MiniLM-L6-v2) + FAISS (faiss-cpu)
  Orchestration: LangChain
  Utils: pandas, python-dotenv, regex
  Dev: PyCharm for app/modules, Jupyter for quick tests on embeddings, FAISS queries, and prompt iterations


Project structure:
app/
  resource/
    portfolio sample.csv
main.py
chains.py
portfolio.py
utils.py
.env              # GROQ_API_KEY=...
