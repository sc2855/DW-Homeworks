from ipynb.fs.full.exercise_air_quality import pm_annual_avg

def test_q2_pm_annual_avg():
    assert pm_annual_avg.shape[0] == 84
    assert 'New York City' in pm_annual_avg['geo_place_name'].unique()
    assert len(pm_annual_avg['geo_place_name'].unique()) == 6
    assert len(pm_annual_avg['time_period'].unique()) == 14