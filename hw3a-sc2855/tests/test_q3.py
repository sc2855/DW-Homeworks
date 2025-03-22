from ipynb.fs.full.exercise_air_quality import df_cardiovascular, df_respiratory
import pandas as pd

def test_q3_cardiovascular():
    assert df_cardiovascular.shape[0] == 25
    assert len(df_cardiovascular.time_period.unique()) == 5
    assert len(df_cardiovascular['geo_place_name'].unique()) == 5

def test_q3_respiratory():
    assert df_respiratory.shape[0] == 25
    assert len(df_respiratory.time_period.unique()) == 5
    assert len(df_respiratory['geo_place_name'].unique()) == 5
    assert ~df_cardiovascular.equals(df_respiratory)

