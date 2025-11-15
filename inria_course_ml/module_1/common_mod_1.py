import os

import pandas as pd
import scipy as sc

data_dir_path = os.path.abspath('../')


def dfFromArffFile(strpath):
    file_path = data_dir_path + strpath
    assert os.path.exists(file_path)
    arff_file = sc.io.arff.loadarff(file_path)
    print(print(f'Metadata =============================================\n {arff_file[1]}'))
    df = pd.DataFrame(arff_file[0])
    for column in df.select_dtypes(include='object').columns:
        df[column] = df[column].str.decode('utf-8')
    return df
