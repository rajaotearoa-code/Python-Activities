# ==============================================================================
# Iris Dataset Initial Processing & Analysis
# Description: Fetches the UCI Iris dataset (ID: 53) and extracts record counts,
#              species counts, and unique flower names using OOP principles.
# ==============================================================================

from ucimlrepo import fetch_ucirepo
import pandas as pd


class IrisAnalyzer:
    """
    Class responsible for fetching, processing, and summarizing the Iris dataset.
    """

    def __init__(self, dataset_id=53):
        self.dataset_id = dataset_id
        self.dataset = None
        self.features = None
        self.targets = None

    def load_data(self):
        """Fetches the dataset from the UC Irvine repository."""
        print("[*] Fetching Iris dataset from UCI Machine Learning Repository...")
        self.dataset = fetch_ucirepo(id=self.dataset_id)
        
        # Features: sepal length, sepal width, petal length, petal width
        self.features = self.dataset.data.features
        
        # Target: flower species classification
        self.targets = self.dataset.data.targets

    def get_total_records(self):
        """Returns the total number of records/rows in the dataset."""
        return len(self.features)

    def get_flower_names(self):
        """Returns a list of unique flower species names in the dataset."""
        # Find the target column name (usually 'class')
        target_column = self.targets.columns[0]
        return self.targets[target_column].unique().tolist()

    def get_total_species_count(self):
        """Returns the count of distinct flower species."""
        return len(self.get_flower_names())

    def display_summary(self):
        """Prints the analysis required by the activity."""
        total_records = self.get_total_records()
        species_names = self.get_flower_names()
        species_count = self.get_total_species_count()

        print("\n" + "=" * 55)
        print("          IRIS DATASET INITIAL ANALYSIS RESULTS         ")
        print("=" * 55)
        print(f"1. Total number of records (rows) : {total_records}")
        print(f"2. Total number of flower species : {species_count}")
        print(f"3. Names of flower species        :")
        for index, name in enumerate(species_names, start=1):
            print(f"   - Species {index}: {name}")
        print("=" * 55)


def main():
    analyzer = IrisAnalyzer(dataset_id=53)
    analyzer.load_data()
    analyzer.display_summary()


if __name__ == "__main__":
    main()