from langchain_mcp_adapters.client  import MultiServerMCPClient
import asyncio
import os

#path
mcp_server_script = os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),"createmcp","first_mcp_server_stdio.py") 
venv_path = os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),".venv")
async def main():
    #instance of the MUltiservermcpclient
    client = MultiServerMCPClient(
    #MCP Server config
    {
        "data_fetch_mcp_stdio":{
            "transport": "stdio",
            "command": os.path.join(venv_path, "Scripts", "python.exe"),
            "args": [str(mcp_server_script)]
        },
        "data_fetch_mcp_http":{
            "transport": "streamable-http",
            "url": "http://localhost:8050/mcp"
        }

    }
    )
    #list tools
    tools = await client.get_tools()
    print("Available tools:", tools)
if __name__ == "__main__":
    asyncio.run(main())