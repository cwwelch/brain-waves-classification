import os
import pyarrow.parquet as pq

def merge_parquet_files(folder_path, output_file):
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".parquet")]
    
    if not files:
        print("No Parquet files found in the directory.")
        return
    
    schema = pq.ParquetFile(files[0]).schema_arrow
    
    with pq.ParquetWriter(output_file, schema=schema) as writer:
        for file in files:
            table = pq.read_table(file, schema=schema)
            writer.write_table(table)
    
    print(f"Merged parquet file saved to {output_file}")