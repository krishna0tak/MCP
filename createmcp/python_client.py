import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters , StdioServerParameters , client

#path
mcp_server_script = os.path.join((os.path.dirname(os.path.abspath(__file__))),"first_mcp_server_stdio.py")
print(f"mcp_server_script: {mcp_server_script}")
#create server para
server_params = StdioServerParameters(
     command="python",
        args=[mcp_server_script],
        env={}
)
#client session

