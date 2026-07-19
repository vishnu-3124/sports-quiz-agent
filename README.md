# Sports Quiz Agent (RAG-Powered)

An intelligent, AI-driven Sports Quiz Agent that generates real-time multiple-choice quizzes using a hybrid Retrieval-Augmented Generation (RAG) pipeline. The system combines local historical knowledge (stored in a vector database) with live web context to ensure accurate, hallucination-free question generation.

## 🚀 Features
* **Hybrid Context Retrieval:** Blends historical data from an offline vector store with live web news.
* **Vector Store Integration:** Uses **ChromaDB** to index and query structured historical sports data.
* **Advanced AI Generation:** Leverages the modern **Google GenAI SDK** and the `gemini-2.5-flash` model to generate custom quizzes.
* **Interactive Dashboard:** Built using **Streamlit** for a seamless user experience.

---

## 🛠️ Tech Stack
* **Language:** Python 3.9 - 3.11
* **LLM Engine:** Google Gemini (`google-genai`)
* **Vector Database:** ChromaDB
* **UI Framework:** Streamlit

---

## 📂 Project Directory Structure

```plaintext
sports-quiz-agent/
├── data/
│   └── sports_facts.json     # Baseline historical truth knowledge base
├── src/
│   ├── config.py             # Environment & credential configuration
│   ├── database.py           # ChromaDB initialization & querying
│   ├── generator.py          # Gemini content generation pipeline
│   └── search.py             # Live web search context retrieval
├── app.py                    # Streamlit application main entry point
├── .env                      # Local secret API keys (Hidden via .gitignore)
└── .gitignore                # Git untracked files configuration
```

**Installation & Setup**
1. Clone the Repository
```PowerShell
git clone [https://github.com/YOUR-USERNAME/sports-quiz-agent.git](https://github.com/YOUR-USERNAME/sports-quiz-agent.git)
cd sports-quiz-agent
```
2. Set Up a Virtual Environment
```PowerShell
python -m venv venv
.\venv\Scripts\activate
```
3. Install Dependencies
```PowerShell
pip install streamlit google-genai chromadb python-dotenv
```
4. Configure Environment Variables
Create a .env file in the root directory and add your credentials:

GEMINI_API_KEY=YOURGEMINIKEYHERE
🏃 How to Run the Application
Execute the entry file using your active virtual environment's package launcher:

```PowerShell
python -m streamlit run app.py
```

### How to push this new file to GitHub:
Once you save the file locally, run these commands in your terminal to update your repository:

```powershell
git add README.md
git commit -m "Add comprehensive project README"
git push origin main
```
