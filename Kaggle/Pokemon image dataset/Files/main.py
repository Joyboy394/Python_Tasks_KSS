import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the specific file inside the Kaggle dataset
file_path = "pokemon.csv" 

# Use dataset_load instead of the deprecated load_dataset
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "vishalsubbiah/pokemon-images-and-types",
  file_path,
)

print("First 5 records:\n", df.head())
