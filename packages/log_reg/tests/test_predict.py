from log_reg.processing.data_management import load_data
from log_reg.predict  import make_prediction
import numpy as np

def test_make_single_prediction():
    test_data = load_data(file_name='test_data.csv')
    subject = make_prediction(input_data=test_data)


    assert subject is not None
    assert isinstance(subject.get('predictions')[0], np.ndarray)
