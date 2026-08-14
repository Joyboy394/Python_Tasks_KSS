from collections import defaultdict
def read_log_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()

def process_error_logs(file_path):
    error_counts = defaultdict(int)

    for line in read_log_file(file_path):
        if "ERROR" in line:
            parts = line.split("ERROR", 1)
            error_msg = (
                parts[1].strip(" :[]") if len(parts) > 1 else line
            )
            error_counts[error_msg] += 1

    return dict(error_counts)

if __name__ == "__main__":
    log_file = "app.log"

    results = process_error_logs(log_file)

    print("--- Error Occurrences ---")
    for error, count in results.items():
        print(f"{count}x : {error}")
        