 # Model Context Protocol Learning Lab

 

 A hands-on Python project for learning how to build, connect, package, gateway, and containerize Model Context Protocol (MCP) servers.

 This repository follows a practical learning path from a small stdio server to a Streamable HTTP server, MCP clients, LangChain integration, community tools, a gateway, and a Dockerized deployment.

 ## What I Learned

 - Why MCP provides a standard way for AI applications to discover and use tools.
 - How MCP hosts, clients, servers, tools, and transports fit together.
 - The difference between local stdio communication and Streamable HTTP.
 - How to create an MCP server with Python and FastMCP.
 - How to connect to an MCP server with the Python SDK.
 - How MCP tools can be used with LangChain.
 - How to inspect and debug servers with MCP Inspector.
 - How to connect community and hosted MCP servers.
 - How to package an MCP server for reuse.
 - How to combine multiple MCP servers behind a gateway.
 - How to containerize and deploy an MCP gateway with Docker.

 ## Project Flow

 ```text
 MCP server -> MCP client -> LangChain -> HTTP transport -> Gateway -> Docker
 ```

 ## Repository Map

 | Directory | Purpose |
 | --- | --- |
 | `createmcp/` | First stdio server and Python client experiments |
 | `HTTP_MCP/` | Streamable HTTP server examples |
 | `3rd_party_mcp/` | Community and hosted MCP experiments |
 | `MCP_GATEWAY/` | Gateway experiments and mounted MCP services |
 | `MCP_DOCKER/` | Dockerized MCP gateway deployment |
 | `MCP_PYPI/` | MCP terminal-tool packaging experiments |
 | `.vscode/mcp.json` | MCP server configuration used by VS Code |

 ## Prerequisites

 - Python 3.13 or newer
 - `uv` or `pip`
 - Docker Desktop, for the containerized gateway
 - Optional: LangChain-compatible credentials for the client examples

 Install the main project dependencies with:

 ```powershell
 uv sync
 ```

 ## Run the Examples

 ### Start the stdio server

 ```powershell
 python createmcp/first_mcp_server_stdio.py
 ```

 The stdio server is normally started by an MCP client. Run the example client in a separate terminal to initialize a session, list tools, and call `process`:

 ```powershell
 python createmcp/python_client.py
 ```

 ### Start the Streamable HTTP server

 ```powershell
 python HTTP_MCP/http_mcp.py
 ```

 The server listens on port `8050` by default.

 ## Docker Deployment

 The Docker implementation is the primary deployment example in this repository. It runs the gateway and mounts example services for DuckDuckGo and terminal capabilities.

 ```powershell
 cd MCP_DOCKER
 docker build -t mcp-gateway .
 docker run --rm -p 8050:8050 mcp-gateway
 ```

 The gateway exposes a health endpoint:

 ```text
 http://localhost:8050/health
 ```

 Expected response:

 ```json
 {"status":"ok","service":"MCP gateway"}
 ```

 The deployed MCP endpoint is configured as:

 ```text
 https://mcp-1-hrtq.onrender.com/mcp
 ```

 ## Security Note

 This is a learning and demonstration project. Some examples expose terminal execution, Python execution, file writes, and folder deletion. Use them only in a trusted local environment until authentication, authorization, sandboxing, input validation, and audit logging have been added.

 Do not commit real API keys. Keep local secrets in `.env` and use placeholder values in documentation or `.env.example` files.



 ## Docker Source

 [Open the MCP Docker implementation on GitHub](https://github.com/krishna0tak/MCP/tree/main/MCP_DOCKER)

 ## LinkedIn Post


