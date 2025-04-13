from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_API_KEY"))

def export_summary_to_notion(title: str, summary: str):
    # Make sure you're using the correct page ID
    # Notion page IDs can be in different formats, but the API typically expects them without dashes
    page_id = os.getenv("NOTION_PAGE_ID")
    
    # Some debugging to help identify issues
    print(f"Using page ID: {page_id}")
    
    try:
        notion.blocks.children.append(
            block_id=page_id,
            children=[
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"type": "text", "text": {"content": title}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": summary}}]
                    }
                }
            ]
        )
        print("Successfully added content to Notion page")
    except Exception as e:
        print(f"Error adding content to Notion: {e}")
        
        # Try to verify if the page exists and is accessible
        try:
            # Attempt to retrieve the page to check access
            page = notion.pages.retrieve(page_id)
            print("Page exists and is accessible, but there was an error adding content")
        except Exception as page_error:
            print(f"Could not access the page: {page_error}")
            print("Please check that:")
            print("1. The page ID is correct")
            print("2. Your integration has been added to the page")
            print("3. The integration has permission to edit content")