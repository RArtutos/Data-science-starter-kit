# DuckDB Analysis Environment for Book Metadata

A comprehensive Docker environment for analyzing book metadata using DuckDB, Jupyter notebooks, and data visualization tools.

## 🌟 Features

- **Data Processing Pipeline**
  - GZ file decompression
  - JSON to Parquet conversion
  - Chunked processing for large datasets
  - Memory-efficient operations

- **Analysis Capabilities**
  - Advanced SQL queries with DuckDB
  - Interactive data exploration
  - Rich visualizations with Matplotlib and Seaborn
  - Statistical analysis tools

- **Technical Stack**
  - DuckDB for high-performance SQL queries
  - Jupyter for interactive analysis
  - Pandas for data manipulation
  - Matplotlib & Seaborn for visualization
  - Docker for environment consistency

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Build the Docker Image**
   ```bash
   docker-compose build
   ```

3. **Start the Environment**
   ```bash
   docker-compose up
   ```

4. **Access Jupyter**
   - Open the URL shown in the console
   - Default: http://localhost:8888

## 📁 Project Structure

```
.
├── data/
│   ├── elasticsearch/    # Source GZ files
│   ├── json/            # Decompressed JSON files
│   └── parquet/         # Converted Parquet files
├── notebooks/
│   ├── SetupData.ipynb          # Data processing pipeline
│   ├── basic_queries.ipynb      # Basic analysis examples
│   ├── advanced_analysis.ipynb  # Advanced analysis
│   └── Queries_Test.ipynb      # Comprehensive query examples
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## 📊 Available Notebooks

### 1. SetupData.ipynb
- GZ file decompression
- JSON to Parquet conversion
- Chunked processing implementation

### 2. basic_queries.ipynb
- Fundamental DuckDB operations
- Basic data exploration
- Simple visualizations

### 3. advanced_analysis.ipynb
- Complex SQL queries
- Advanced visualizations
- Statistical analysis

### 4. Queries_Test.ipynb
- 20 comprehensive analysis queries
- In-depth metadata exploration
- Advanced visualization techniques

## 🔧 Configuration

### Memory Settings
- DuckDB memory limit: 28GB
- Python environment: 3.12
- Recommended system RAM: 32GB

### Docker Settings
- Port mapping: 8888:8888
- Volume mounts for data persistence
- Jupyter notebook directory mapping

## 📈 Analysis Capabilities

- Source record analysis
- File format distribution
- Publication trends
- Language analysis
- Publisher statistics
- File size patterns
- Access type distribution
- Classification analysis
- Identifier systems
- Temporal analysis

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
