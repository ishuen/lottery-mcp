# Lottery MCP Server

This MCP (Model Context Protocol) server enables retrieval of Taiwan lottery data for a specified month. It currently supports four games: Super Lotto 638 (威力彩), Lotto 649 (大樂透), Daily Cash 539 (今彩539), and Lotto 4D (4星彩).

## Requirements

- Python 3.9+
- uv (Python package manager)

## Usage

Install uv if you don't have it:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Start the server:
```bash
uv run main.py
```

## Running Locally with Claude App

To use this MCP server with Claude App, follow these steps:

1. Open `Settings > Developer` in Claude App.
2. Add or update your configuration as shown below, replacing `<absolute_path_to_the_folder>` with the full path to your project directory:

    ```json
    {
      "mcpServers": {
        "lottery": {
          "command": "uv",
          "args": [
            "--directory",
            "<absolute_path_to_the_folder>",
            "run",
            "main.py"
          ]
        }
      }
    }
    ```

3. After connecting, a blue `running` tag will appear next to your server name in the Local MCP servers list.
4. Access the server's tools by clicking the `Search and tools` button in the chat interface.

This confirms the MCP server is running and integrated with Claude App.

## Troubleshoot

- Unable to connect MCP server locally
    - If uv is already installed, it may mean that Claude cannot find it. Turn on the terminal and set a symlink:
    
    ```
        sudo ln -s ~/.local/bin/uv /usr/local/bin/uv
    ```

    - Reference: https://gist.github.com/gregelin/b90edaef851f86252c88ecc066c93719