# LinkedIn Post Draft

## Building My First MCP Server

I recently completed a hands-on learning project to understand the Model Context Protocol (MCP) from the ground up.

What started as a question about how AI applications can interact with external tools became a practical journey through MCP servers, clients, transports, gateways, packaging, and Docker deployment.

## What I Learned

- Why MCP is useful for creating a standard interface between AI applications and tools.
- How MCP hosts, clients, and servers communicate.
- The difference between stdio and Streamable HTTP transports.
- How to create an MCP server in Python with FastMCP.
- How to build a Python MCP client with the MCP SDK.
- How to discover and call tools through a client session.
- How to integrate MCP with LangChain.
- How MCP Inspector helps test and debug servers.
- How to use community-built and hosted MCP servers.
- How to package an MCP server for reuse.
- How to bring multiple MCP services together through an MCP gateway.
- How to containerize the gateway and deploy it with Docker.

## What I Built

During the project, I created:

- A local stdio MCP server with callable tools.
- A Python client that initializes a session, lists tools, and invokes a tool.
- A Streamable HTTP MCP server.
- A gateway that mounts multiple MCP services with namespaces.
- A Dockerized MCP gateway with a health endpoint.

This project helped me connect the concepts in the MCP walkthrough with working Python code and a deployable container.

## My Biggest Takeaways

1. MCP separates tool capabilities from the AI application that uses them.
2. Transport choice depends on the environment: stdio is useful for local processes, while Streamable HTTP is useful for remote services.
3. A gateway can provide one entry point for multiple MCP servers.
4. Docker makes the deployment process repeatable and easier to share.
5. A working prototype is only the beginning. Authentication, authorization, sandboxing, testing, observability, and secret management are essential before exposing powerful tools publicly.

This is a learning and demonstration project, not a production-ready platform. Building it gave me a much clearer understanding of how MCP-based systems are structured and deployed.

I am continuing to explore how MCP can make AI applications more capable, modular, and easier to integrate with real-world tools.


Explore the Dockerized MCP gateway:
https://github.com/krishna0tak/MCP/tree/main/MCP_DOCKER

#ModelContextProtocol #MCP #Python #FastMCP #LangChain #Docker #AIEngineering #LearningInPublic
