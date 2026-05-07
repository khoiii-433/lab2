import Lab2

def test_find_min_max():
    expected_result = (1, 6)
    test_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = Lab2.calc_min_max_temperature(test_list)
    assert (result == expected_result)
def test_calc_average():
    expected_result = 3.5
    test_list = [1, 2, 3, 4, 5, 6]
    result = Lab2.calc_average_temperature(test_list)
    assert (result == expected_result)
def test_calc_median():
    expected_result = 3.5
    test_list = [1, 2, 3, 4, 5, 6]
    result = Lab2.calc_median_temperature(test_list)
    assert (result == expected_result)

    