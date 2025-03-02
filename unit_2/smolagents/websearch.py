from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

# Uncomment if need to login to access the huggingface_hub
# from huggingface_hub import login
# login()

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")
