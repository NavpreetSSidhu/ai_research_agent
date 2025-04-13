import os
from dotenv import load_dotenv
from agents.research_agent import build_research_agent
from exporters.notion_exporter import export_summary_to_notion

load_dotenv()

def main():
    topic = input("Enter a research topic: ")
    agent = build_research_agent()

    print(f"\n🔍 Researching: {topic}...\n")
    summary = agent.run(f"Research and summarize the topic: {topic} in 3 key sections.")
    
    print("\n✅ Summary generated:\n")
    print(summary)

    export_summary_to_notion(title=topic.title(), summary=summary)
    print("\n📤 Sent to Notion!")

if __name__ == "__main__":
    main()
