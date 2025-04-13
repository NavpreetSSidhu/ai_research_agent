🧠 AI Research Agent
The AI Research Agent is an autonomous tool powered by OpenAI and LangChain that performs research on any given topic, analyzes the information, generates a concise report, and automatically populates it into your Notion workspace.

✨ Features
🔍 Performs deep research using web search

📊 Analyzes and summarizes relevant information

📝 Generates well-structured reports

🧾 Automatically updates your Notion page

⚙️ Built with Python, OpenAI, LangChain, and Notion API

🚀 Getting Started
1. Clone the Repository

git clone https://github.com/NavpreetSSidhu/ai_research_agent
cd ai-research-agent

2. Install Dependencies

Make sure you have Python 3.8+ installed, then run:
pip install -r requirements.txt

4. Setup Environment Variables

Create a .env file in the root directory and add the following keys:

OPENAI_API_KEY=your_openai_api_key
NOTION_API_KEY=your_notion_api_key
NOTION_PAGE_ID=your_notion_page_id

💡 You can get your Notion integration token and page ID from Notion Developers.

4. Run the Agent

Once everything is set up, run:
python main.py

The agent will ask for your research topic, perform analysis, generate a report, and push the results to your specified Notion page.

🛠 Tech Stack

Python

OpenAI GPT models

LangChain

Notion API

📌 TODO / Future Improvements

Add support for multiple report templates

Schedule recurring research reports

Enable multi-page Notion updates

Integrate with Slack or Email for delivery

🧑‍💻 Author
Navpreet Singh Sidhu
Feel free to reach out for collaboration or feedback!
