from langchain_mcp_adapters.client  import MultiServerMCPClient
import asyncio
import os

async def main():
    #instance of the MUltiservermcpclient
    client = MultiServerMCPClient(
    #MCP Server config
    {
       "data_fetch_mcp_stdio": {
    "transport": "stdio",
    "command": r"C:\ModelContextProtocol\.venv\Scripts\python.exe",
    "args": [
        r"C:\ModelContextProtocol\createmcp\first_mcp_server_stdio.py"
    ],
}
    }
    )
    #list tools
    tools = await client.get_tools()
    print("Available tools:", tools)
if __name__ == "__main__":
    asyncio.run(main())