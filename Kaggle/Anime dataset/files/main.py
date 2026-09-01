import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the specific file inside the Kaggle dataset
# Replace "anime.csv" with the exact name of the file you want to load
file_path = "anime.csv" 

# Use dataset_load instead of the deprecated load_dataset
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "udaykumar025/anime-dataset-top-10k-normalized",
  file_path,
)

print("First 5 records:\n", df.head())
