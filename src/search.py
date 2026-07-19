from duckduckgo_search import DDGS

def get_live_news_context(sport_name):
    """
    Searches the live web for recent sport news, matches, or events.
    Returns a unified text summary of search snippets.
    """
    # Using 2026 to grab highly relevant recent content
    search_query = f"{sport_name} latest tournament results championship winners news 2026"
    retrieved_texts = []

    print(f"Executing web search for: '{search_query}'...")
    try:
        # Initializing DuckDuckGo search context
        with DDGS() as ddgs:
            # Force conversion to a list to safely evaluate results immediately
            results = list(ddgs.text(search_query, max_results=3))

            for index, r in enumerate(results, start=1):
                title = r.get("title", "No Title")
                # DuckDuckGo sometimes shifts fields between 'body' and 'snippet'
                snippet = r.get("body") or r.get("snippet") or "No Snippet Content Available"
                retrieved_texts.append(f"Web Source {index}: {title}\nSnippet: {snippet}")

    except Exception as e:
        print(f"Web Search fell back or failed: {e}")
        return "No recent search engine updates available due to system connectivity."

    # Handle case where search executes fine but returns zero hits
    if not retrieved_texts:
        return "Search completed but no matching live updates were found for 2026."

    return "\n\n".join(retrieved_texts)