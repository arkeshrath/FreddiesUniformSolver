# Freddie's missing uniform service

Freddie's missing uniform service is a simple flask-based web service for deciphering clues based on an uploaded clues file.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- virtualenv

### Installation

1. Unzip the file / Clone the repository:
    ```sh
    git clone https://github.com/arkeshrath/FreddiesUniformSolver.git
    ```

### Running the Application

1. Start the Flask app with provided shell script:
    ```sh
   chmod +x run.sh
    ./run.sh
    ```

    To run the same alongside an external cache server please run,
    ```sh
   chmod +x run_with_cache.sh
    ./run_with_cache.sh
    ```

2. The service will be available at `http://localhost:8000/process-file`.

### Usage

#### Uploading and processing a File

To upload and process a file with grid coordinates and fold instructions, use the following CURL command:

```sh
curl -X POST http://localhost:8000/process-file \
-H "Content-Type: application/json" \
-d '{"filename": "secret-message.0.txt"}'
```

To use the demo UI, please open your web browser and go to `http://localhost:8000/ui/v1/uniform-finder`.




### Logging
Logs are maintained for various operations, including grid creation, folding, and error handling. Logs will display the time taken for folding operations and any errors encountered.

### Caching
An in-memory cache has been implemented to speed up operations on the same file. For scaling this in production, we would need to implement a distributed cache like redis.

An implementation has also been provided with a simple external cache service.

### Unit Tests

Unit tests are provided for the grid folding logic and file parsing. To run the tests, use:
```sh
python -m unittest discover -s tests
```


### Considerations and tradeoffs

In-Memory Caching: An in-memory cache (TTLCache) is used for caching grid data with a TTL of 1 hour. This choice avoids the complexity of integrating a full-fledged caching solution like Redis but limits scalability.

File Uploads: Files are read from a local directory for simplicity. In a production environment, a more robust file storage solution (like AWS S3) would be preferred.

Error Handling: Basic error handling is implemented. For a production-grade service, more comprehensive error handling and validation would be necessary.

Folding Logic: The folding logic checks for the presence of black cells along the fold line and raises errors if present. This ensures that folds are valid but may need further optimization for large grids.

Scalability : Currently the web service is running with 1 worker thread, this is in order to show the caching implementation of the project. For productioninizing, we will be using multiple worker threads and fine tune this number depending on our compute layer.

