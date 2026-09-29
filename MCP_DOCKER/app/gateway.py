from fastmcp import FastMCP
from fastmcp.server import create_proxy
from starlette.responses import JSONResponse
import os

mcp = FastMCP()


@mcp.tool()
async def fetch():
    '''Use this tool to fetch data from a source.'''

    # Simulate fetching data from a source
    ''' You can make some API calls here or fetch data from a database '''
    return {"data": "Hello, MCP!"}

@mcp.tool()
async def process(path:str):
    '''Use this tool to process the fetched data.'''

    # Simulate processing the fetched data
    ''' You can perform some data transformations here '''
    return {"processed_data": "Data has been processed! at path: " + path}


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    return JSONResponse({"status": "ok", "service": "MCP gateway"})


# Mount the tools to the MCP instance
mcp.mount(
    create_proxy({
        "mcpServers" : {
            "ddg_mcp": {"command":"uvx", "args": ["duckduckgo-mcp-server"]}        }
    }
    ),
    namespace="ddg",
)

mcp.mount(
    create_proxy({
        "mcpServers" : {
            "agentic_terminal": {"command":"uvx", "args": ["agentic_terminal"]}        }
    }
    ),
    namespace="terminal",
)

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8050")),
    )