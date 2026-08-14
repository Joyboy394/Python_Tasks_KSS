import time
import numpy as np
import pandas as pd
from functools import wraps


# 1. Decorator to measure execution time
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"⏱️ [{func.__name__}] Executed in {elapsed:.4f} seconds.")
        return result
    return wrapper


# 2. Generator to stream lines with Exception Handling for bad data
def stream_valid_numbers(file_path):
    """Yields valid numbers one by one, skipping corrupted rows gracefully."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, start=1):
            cleaned = line.strip()
            if not cleaned:
                continue  # Skip empty lines
            
            try:
                # Attempt conversion to float
                yield float(cleaned)
            except ValueError:
                # Exception handling: Catch and report invalid numeric data without crashing
                print(f"⚠️ Warning: Skipped invalid data at line {line_num}: {cleaned!r}")


# 3. Processing Pipeline decorated with execution timing
@measure_time
def process_data_pipeline(file_path, batch_size=1000):
    """Streams numbers, calculates batch stats with NumPy, and returns a Pandas DataFrame."""
    batch = []
    records = []
    batch_index = 1

    # Consume the generator stream
    for number in stream_valid_numbers(file_path):
        batch.append(number)

        # Process in batches once full
        if len(batch) == batch_size:
            records.append(_compute_batch_stats(batch_index, batch))
            batch.clear()
            batch_index += 1

    # Process remaining items if batch wasn't full at EOF
    if batch:
        records.append(_compute_batch_stats(batch_index, batch))

    # 4. Convert aggregated results to a Pandas DataFrame
    df = pd.DataFrame(records)
    return df


def _compute_batch_stats(batch_id, numbers_list):
    """Helper function using NumPy for numerical calculations."""
    # Convert list segment to NumPy array
    arr = np.array(numbers_list)

    # Calculate statistics using NumPy
    return {
        "batch_id": batch_id,
        "count": len(arr),
        "mean": float(np.mean(arr)),
        "std_dev": float(np.std(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr))
    }


# --- Demonstration ---
if __name__ == "__main__":
    # Create a mock file with both valid numbers and dirty/corrupted data
    mock_file = "numbers_data.txt"
    sample_content = """10.5
20.2
INVALID_VAL
30.8
40.0
50.1
corrupted_entry
60.4
70.3
"""
    with open(mock_file, "w", encoding="utf-8") as f:
        f.write(sample_content)

    print("--- Starting Pipeline Processing ---\n")
    
    # Run the processing pipeline (batches of 3 for demonstration)
    results_df = process_data_pipeline(mock_file, batch_size=3)

    print("\n--- Final Summary DataFrame ---")
    print(results_df)
    