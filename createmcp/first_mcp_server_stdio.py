from fastmcp import FastMCP


mcp = FastMCP()
@mcp.tool()
def fetch():
    '''Use this tool to fetch data from the server'''
    return {"data": "heello world"}


@mcp.tool()
def process():
    '''Use this tool to process data from the server'''
    return {"processed_data": "processed data"}


if __name__ == "__main__":
    mcp.run(transport="stdio")
