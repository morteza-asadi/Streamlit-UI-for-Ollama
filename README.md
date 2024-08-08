# Simple Ollama Streamlit UI

A simple user-friendly interface for interacting with Ollama models using Streamlit.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup and Running (with Docker)

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-ollama-streamlit-ui.git
   cd simple-ollama-streamlit-ui
   ```

2. Start the services using Docker Compose:
   ```
   docker-compose up -d
   ```

3. Pull the Ollama model (e.g., tinydolphin):
   ```
   docker exec -i ollama-service ollama pull tinydolphin
   ```

4. Access the Streamlit UI in your web browser at:
   ```
   http://localhost:8501
   ```

## Manual Setup (without Docker)

If you prefer to run the application without Docker:

1. Install Ollama:
   - Download and install from the Ollama [Download Page](https://ollama.com/download)
   - Or, if you prefer to use Docker for Ollama only, follow the Ollama Docker [Guidelines](https://hub.docker.com/r/ollama/ollama)

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   streamlit run src/main.py
   ```

## Usage

1. Select an Ollama model from the dropdown.
2. Start chatting with the selected model!

## Troubleshooting

- If you encounter any issues with the Ollama service, you can check its logs:
  ```
  docker logs ollama-service
  ```

- To restart the services:
  ```
  docker-compose down
  docker-compose up -d
  ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).