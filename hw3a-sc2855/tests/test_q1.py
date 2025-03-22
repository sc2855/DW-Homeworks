from ipynb.fs.full.exercise_air_quality import df

def test_q1_columns():
    assert 'unique_id' in df.columns
    assert 'indicator_id' in df.columns
    assert 'name' in df.columns
    assert 'measure' in df.columns
    assert 'measure_info' in df.columns
    assert 'geo_type_name' in df.columns
    assert 'geo_join_id' in df.columns
    assert 'geo_place_name' in df.columns
    assert 'time_period' in df.columns
    assert 'start_date' in df.columns
    assert 'data_value' in df.columns
    
def test_q1_dtypes():
    assert df['data_value'].dtype == 'float64'

def test_q1_length():
    assert df.shape[0] == 18025