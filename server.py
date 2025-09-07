from fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup
import os

mcp = FastMCP("Web Extraction MCP Server")

@mcp.tool
def web_extraction(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator='\n')

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    mcp.run(transport="http", host="127.0.0.1", port=port)