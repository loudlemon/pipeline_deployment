"""
This script should only be run in CI,
otherwise it will disrupt the differential logic
"""

import pandas as pd
from log_reg.predict import make_prediction
from log_reg.processing.data_management import load_data
from api import config



def capture_predictions() -> None:
    """ Save test data predictions to .csv file"""
    
    new_dict = {}
    saved_file = 'test_predictions.csv'
    test_data = load_data(file_name='test_data.csv')
    predictions = make_prediction(input_data=test_data)
    array = predictions.get('predictions')[0]
    version = predictions.get('version')
    new_dict['predictions'] = array
    new_dict['version'] = version
    preds_df = pd.DataFrame([new_dict])

    #save the file into package repo
    preds_df.to_csv(
        f'{config.PACKAGE_ROOT}/{saved_file}', index=False)



if __name__ == '__main__':
    capture_predictions()