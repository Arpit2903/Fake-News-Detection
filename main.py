from merge_csv_datasets import mergeCSVDatasets


if __name__ == "__main__":
    files = {
        "Fake.csv": {
            "default_label": 1,
            "label_mapping": None
        },
        "fake_or_real_news.csv": {
            "default_label": None,
            "label_mapping": {"FAKE": 1, "REAL": 0}
        },
        "news.csv": {
            "default_label": None,
            "label_mapping": {"FAKE": 1, "REAL": 0}
        },
        "train.csv": {
            "default_label": None,
            "label_mapping": None
        }
    }
    mergeCSVDatasets(filePath="datasets/", files=files)
