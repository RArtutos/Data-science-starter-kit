import os
import subprocess
import shutil
import gzip
import json
import pandas as pd
import duckdb

def create_directories():
    """Create necessary directories if they don't exist."""
    directories = ['data/elasticsearch', 'data/json', 'data/parquet']
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)

def download_and_extract():
    """Download torrent and extract elasticsearch files."""
    # Download torrent file
    torrent_url = "https://annas-archive.org/dyn/small_file/torrents/other_aa/aa_derived_mirror_metadata/aa_derived_mirror_metadata_20250223.torrent"
    torrent_path = "data/elasticsearch/metadata.torrent"
    
    print("Downloading torrent file...")
    subprocess.run(['curl', '-L', '-o', torrent_path, torrent_url], check=True)
    
    print("Downloading data using webtorrent...")
    # Create a temporary directory for the download
    os.makedirs('data/temp', exist_ok=True)
    
    # Download only the elasticsearch directory from the torrent
    subprocess.run([
        'npx', 'webtorrent-cli', 'download', 
        torrent_path, 
        '--select', 'aa_derived_mirror_metadata_20250223/elasticsearch/*',
        '--out', 'data/temp'
    ], check=True)
    
    # Move elasticsearch files to the correct location
    source_dir = "data/temp/aa_derived_mirror_metadata_20250223/elasticsearch"
    dest_dir = "data/elasticsearch"
    
    print("Moving elasticsearch files to final location...")
    for file in os.listdir(source_dir):
        if file.endswith('.gz'):
            shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))
    
    # Cleanup temporary directory and torrent file
    shutil.rmtree('data/temp')
    os.remove(torrent_path)
    print("Cleanup completed")

def decompress_gz_files():
    """Decompress GZ files to JSON."""
    print("Decompressing GZ files...")
    elasticsearch_dir = 'data/elasticsearch'
    json_dir = 'data/json'
    
    for filename in os.listdir(elasticsearch_dir):
        if filename.endswith('.gz'):
            gz_path = os.path.join(elasticsearch_dir, filename)
            json_path = os.path.join(json_dir, filename[:-3])
            
            with gzip.open(gz_path, 'rt') as gz_file, open(json_path, 'w') as json_file:
                for line in gz_file:
                    json_file.write(line)
            print(f"Decompressed {filename}")

def process_json_to_parquet(chunk_size=100000):
    """Convert JSON files to Parquet format with chunking."""
    print("Converting JSON to Parquet...")
    json_dir = 'data/json'
    parquet_dir = 'data/parquet'
    
    for filename in os.listdir(json_dir):
        if not filename.endswith('.txt'):
            continue
            
        base_name = os.path.splitext(filename)[0]
        json_path = os.path.join(json_dir, filename)
        
        # Process file in chunks
        chunk_number = 0
        for chunk_df in pd.read_json(json_path, lines=True, chunksize=chunk_size):
            parquet_path = os.path.join(parquet_dir, f"{base_name}_chunk_{chunk_number}.parquet")
            chunk_df.to_parquet(parquet_path, index=False)
            chunk_number += 1
            print(f"Processed chunk {chunk_number} of {filename}")

def setup_duckdb():
    """Create DuckDB views for the Parquet files."""
    print("Setting up DuckDB views...")
    con = duckdb.connect('data/metadata.db')
    
    # Create views for each type of data
    parquet_files = [f for f in os.listdir('data/parquet') if f.endswith('.parquet')]
    
    for file in parquet_files:
        table_name = file.split('_chunk_')[0]
        parquet_path = os.path.join('data/parquet', file)
        con.execute(f"CREATE VIEW IF NOT EXISTS {table_name} AS SELECT * FROM parquet_scan('{parquet_path}')")
    
    con.close()
    print("DuckDB setup complete!")

def main():
    """Main execution function."""
    try:
        print("Starting data processing pipeline...")
        create_directories()
        download_and_extract()
        decompress_gz_files()
        process_json_to_parquet()
        setup_duckdb()
        print("Data processing complete! You can now start analyzing the data using Jupyter notebooks.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
