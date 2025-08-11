# MCP Attendance Manager Server

A Model Context Protocol (MCP) server that provides attendance management functionality through Claude Desktop.

## Features

- Hello World MCP server with attendance management capabilities
- Cross-platform support (Windows, macOS, Linux)
- Easy setup and configuration
- Integration with Claude Desktop

## Prerequisites

### Python Version
- **Python 3.11 or higher** is required
- Download from: https://www.python.org/downloads/

### UV Package Manager
UV is a fast Python package installer and resolver.

#### Windows
```powershell
# Using PowerShell
irm https://astral.sh/uv/install.ps1 | iex

# Or using pip
pip install uv
```

#### macOS
```bash
# Using curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using Homebrew
brew install uv
```

#### Linux
```bash
# Using curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pip
pip install uv
```

### Claude Desktop
1. Download Claude Desktop from: https://claude.ai/download
2. Install for your operating system:
   - **Windows**: Download .exe installer
   - **macOS**: Download .dmg file
   - **Linux**: Download .AppImage or .deb package

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Theubaa/MCP-Attendance-manager.git
cd MCP-Attendance-manager
```

### 2. Create Virtual Environment
```bash
# Using UV (recommended)
uv venv

# Activate virtual environment
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
# Using UV
uv pip install -e .

# Or using pip
pip install -e .
```

## Configuration

### 1. Claude Desktop Setup
1. Open Claude Desktop
2. Go to **Settings** → **Model Context Protocol**
3. Click **Add Server**
4. Enter the following details:
   - **Name**: Attendance Manager
   - **Command**: `python main.py`
   - **Working Directory**: Path to your project folder
   - **Environment Variables**: Leave empty for now

### 2. Server Configuration
The server is pre-configured with basic MCP functionality. You can modify `main.py` to add custom tools and functions.

## Usage

### Starting the Server
```bash
# Make sure virtual environment is activated
python main.py
```

### Testing the Server
1. In Claude Desktop, ask: "What tools do you have available?"
2. The server should respond with available MCP tools
3. Test attendance management functions

## Project Structure

```
MCP-Attendance-manager/
├── main.py              # Main MCP server file
├── pyproject.toml       # Project configuration
├── README.md            # This file
├── .python-version      # Python version specification
├── .gitignore           # Git ignore rules
└── .venv/               # Virtual environment (created after setup)
```

## Troubleshooting

### Common Issues

#### Python Version Error
```bash
# Check Python version
python --version

# If version is below 3.11, upgrade Python
```

#### UV Installation Issues
```bash
# Verify UV installation
uv --version

# If not found, reinstall using the commands above
```

#### Virtual Environment Issues
```bash
# Remove and recreate virtual environment
rm -rf .venv
uv venv
```

#### Claude Desktop Connection Issues
1. Ensure the server is running (`python main.py`)
2. Check the working directory path in Claude Desktop settings
3. Verify Python path in Claude Desktop settings

### Getting Help
- Check the [MCP Documentation](https://modelcontextprotocol.io/)
- Review [Claude Desktop Documentation](https://docs.anthropic.com/claude/docs/claude-desktop)
- Open an issue on this repository

## Development

### Adding New Tools
1. Modify `main.py`
2. Add new tool functions
3. Register them with the MCP server
4. Test with Claude Desktop

### Building and Testing
```bash
# Install development dependencies
uv pip install -e ".[dev]"

# Run tests (if available)
python -m pytest
```

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For support and questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review MCP and Claude Desktop documentation

---

**Note**: This server is designed to work with Claude Desktop and follows the Model Context Protocol specification. Make sure you have the latest versions of all dependencies for the best experience.
