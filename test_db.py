from src.search import get_live_news_context

print("Testing live web search feature...")
query = "latest winner of the cricket T20 World Cup"
live_data = get_live_news_context(query)

print(f"\nQuery: '{query}'")
print("Live Results Found:")
for idx, snippet in enumerate(live_data, 1):
    print(f"{idx}. {snippet}\n")