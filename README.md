## DuckDB Jupyter Analysis Environment

This project provides a Docker environment for analyzing data using DuckDB and Jupyter notebooks.

### Features
- DuckDB for fast SQL queries on JSON files
- Jupyter notebooks for interactive analysis
- Pandas and Matplotlib for data manipulation and visualization
- Docker container for consistent environment

### Setup
1. Build the Docker image:
```bash
docker-compose build
```

2. Start the Jupyter server:
```bash
docker-compose up
```

3. Open the Jupyter interface in your browser using the URL shown in the console

### Project Structure
- `/notebooks`: Jupyter notebooks with analysis examples
- `/data`: Directory for data files (mount your data here)

### Example Notebooks
- `basic_queries.ipynb`: Basic DuckDB query examples
- `advanced_analysis.ipynb`: Advanced analysis with visualizations
