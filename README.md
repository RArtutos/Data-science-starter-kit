# DuckDB Analysis Environment for Book Metadata

A comprehensive Docker environment for analyzing book metadata using DuckDB, Jupyter notebooks, and data visualization tools.
[Google drive folder with .parquet files](https://drive.google.com/drive/folders/1Z8gC0HPT5LTJaV-0_UtwlkBZXMNof4xM?usp=sharing)

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

## 📥 Data Setup

### Data File Locations
The project uses the following directory structure:
```
data/
├── elasticsearch/    # Original .gz files from Anna's Archive metadata
├── json/            # Decompressed JSON files
└── parquet/         # Converted Parquet files
```

### Data Processing Options

You have two options for processing the data:

#### Option 1: Using initialScript.py
Run the script to automatically handle the entire pipeline:
```bash
python initialScript.py
```

This script will:
1. Create necessary directories
2. Download the metadata torrent
3. Extract required files
4. Convert data to Parquet format
5. Set up DuckDB views

#### Option 2: Using Jupyter Notebook
1. Start the Jupyter environment:
   ```bash
   docker-compose up
   ```
2. Put the .gz of elasticsearch in the data/elasticsearch folder
3. Open `SetupData.ipynb` in Jupyter and run all cells to process the data interactively

Both options will prepare your data for analysis. Choose based on your preference for automation vs. interactive processing.

## 📊 Analysis Examples

Here are some examples of the analyses and visualizations you can create:

### Publication Year Distribution
![Publication Year Distribution](/images/Publication Year Distribution.png)
Analyze the distribution of publications across different years using advanced aggregation queries.

### Language Analysis
![Language Distribution](/images/Language Distribution.png)
Explore the diversity of languages in the dataset with interactive pie charts and bar graphs.

### Rare vs. Non-Rare Books Analysis
![Rare vs. Non-Rare](/images/Rare vs. Non-Rare.png)
Discover the distribution between rare and non-rare books in the collection, providing insights into the uniqueness of the available literature.

### Download Availability Analysis
![Download Availability](/images/Download Availability.png)
Explore the various download options available across the dataset, helping understand accessibility patterns and preferred distribution methods.

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
├── initialScript.py
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
