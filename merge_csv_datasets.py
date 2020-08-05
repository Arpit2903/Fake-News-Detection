import pandas as pd
import os


def mergeCSVDatasets(filePath, files):
    dfs = []
    for filename in files:
        if files[filename]['default_label'] is None:
            df = pd.read_csv(filePath + filename, usecols=['title', 'text', 'label'])
            if files[filename]["label_mapping"] is not None:
                # map the label 'FAKE': 1 and 'REAL': 0
                df["label"].replace(files[filename]['label_mapping'], inplace=True)
        else:
            # If the CSV file does not have the label then add the label column with the supplied default value
            df = pd.read_csv(filePath + filename, usecols=['title', 'text'])
            df['label'] = files[filename]['default_label']
        print("Imported {} with {} rows".format(filename, df.shape[0]))
        dfs.append(df)

    merged_df = pd.concat(dfs, axis=0)    # Vertical stacking each dataframe on another to create a merged dataframe

    merged_df.drop_duplicates(inplace=True, keep="first")  # Remove any duplicate rows if exists

    merged_df.dropna(axis=0, inplace=True)   # Remove rows with null values in any column

    print("Merged dataset with {} rows".format(merged_df.shape[0]))
    if os.path.exists(filePath + 'merged.csv'):
        os.remove(filePath + 'merged.csv')

    merged_df.to_csv(filePath + 'merged.csv', index=False, mode='a')


