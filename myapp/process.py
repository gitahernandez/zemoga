
import pandas as pd
import numpy as np
import zipfile

def create_data_frame(kind, files, separator):
    filtered_files = [file for file in files if file.kind == kind]
    frames = []
    for file in filtered_files:
        df = pd.read_csv(file.docfile.path, sep=separator, header=None,error_bad_lines=False)

        frames.append(df)
    
    df = pd.concat(frames)
    df.columns =[f'{kind}_Column_{column}' for column in range(1, len(df.columns)+1)]
    df['file_name'] = file.file_name

    return df


def link_data_frames(database_df, schema_df, data_df):

    database_df = database_df.dropna(subset=["DATABASE_Column_1"])
    schema_df = schema_df.dropna(subset=["SCHEMA_Column_1"])
   
    data_df['row_num'] = np.arange(1, len(data_df)+1)

    data_df_blank_id = data_df[data_df['DATA_Column_1'].isna()]
    data_df_blank_id = data_df_blank_id[["file_name", "row_num"]]
    data_df_blank_id["error"] = "Id Empty"

    data_df = data_df.dropna(subset=["DATA_Column_1"])

    data_df_wrong_separator = data_df[data_df['DATA_Column_9'].str.contains(";")]
    data_df_wrong_separator = data_df_wrong_separator[["file_name", "row_num"]]
    data_df_wrong_separator["error"] = "Semicolon is not an allowed separator"

    errors = pd.concat([data_df_blank_id, data_df_wrong_separator])
    errors.to_csv('media/errors.csv', index = False)

    data_df = data_df[~data_df["DATA_Column_9"].str.contains(";")]

    database_schema_df = pd.merge(schema_df, database_df, left_on="SCHEMA_Column_1", right_on="DATABASE_Column_1")
    database_schema_data_df = pd.merge(database_schema_df, data_df, left_on="SCHEMA_Column_5", right_on="DATA_Column_1")

    database_schema_data_df.to_csv('media/linked_data.csv', index = False)

    zip_file = zipfile.ZipFile('media/rezult.zip', 'w')
    zip_file.write('media/errors.csv', compress_type=zipfile.ZIP_DEFLATED)
    zip_file.write('media/linked_data.csv', compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()

