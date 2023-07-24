from app.project.smartcalc.services import services
from unittest import mock


def test_read_history():
    mock_history_read_file = mock.Mock(return_value=["123-9=114.0; x=1.0", "123*6=738.0; x=1.0", "8745-9=8736.0; x=1.0"])
    services.history.read_file = mock_history_read_file
    result = services.read_history()
    assert result == ["123-9=114.0; x=1.0", "123*6=738.0; x=1.0", "8745-9=8736.0; x=1.0"]
    mock_history_read_file.assert_called_once()


def test_write_history():
    mock_history_write = mock.Mock(return_value=["123-9=114.0; x=1.0", "123*6=738.0; x=1.0", "8745-9=8736.0; x=1.0"])
    services.history.write = mock_history_write
    result = services.write_history("sin(x)*6/247=0.020440590724078455; x=1.0")
    assert result == ["123-9=114.0; x=1.0", "123*6=738.0; x=1.0", "8745-9=8736.0; x=1.0"]
    mock_history_write.assert_called_once_with("sin(x)*6/247=0.020440590724078455; x=1.0")


def test_clean_history():
    mock_history_clean = mock.Mock()
    services.history.clean = mock_history_clean
    result = services.clean_history()
    assert result is None
    mock_history_clean.assert_called_once()


def test_get_expression_result_valid_expression():
    mock_calculate = mock.Mock(return_value="10.0")
    services.calculator.calculate = mock_calculate
    result = services.get_expression_result("2*x", "5.0")
    assert result == "10.0"
    mock_calculate.assert_called_once_with("2*5.0")


def test_get_expression_result_invalid_expression():
    mock_calculate = mock.Mock(return_value=None)
    services.calculator.calculate = mock_calculate
    result = services.get_expression_result("(((eee", "1.0")
    assert result == "Error in expression"
    mock_calculate.assert_called_once_with("(((eee")


def test_calculate_graph_expression_result_valid_expression():
    # Mock calculator.graph_calculate()
    mock_graph_calculate = mock.Mock(return_value=[0, 2, 4, 6, 8])
    
    # Replace the actual function with the mock
    services.calculator.graph_calculate = mock_graph_calculate
    
    # Test the calculate_graph_expression_result function with a valid expression
    result = services.calculate_graph_expression_result("x*2", "-5.0", "5.0")
    
    # Assertions
    assert result == [0, 2, 4, 6, 8]
    mock_graph_calculate.assert_called_once_with("x*2", "-5.0", "5.0")


# def test_calculate_graph_expression_result_invalid_expression():
#     # Mock calculator.graph_calculate() to return None for an invalid expression
#     mock_graph_calculate = mock.Mock(return_value=None)
    
#     # Replace the actual function with the mock
#     services.calculator.graph_calculate = mock_graph_calculate
    
#     # Test the calculate_graph_expression_result function with an invalid expression
#     result = services.calculate_graph_expression_result("x / 0", "-5", "5")
    
#     # Assertions
#     assert result is None
#     mock_graph_calculate.assert_called_once_with("x / 0", "-5", "5")


# def test_read_config():
#     # Mock configs.read_config()
#     mock_read_config = mock.Mock(return_value={"background": "white", "main_color": "blue", "font_size": "12"})
    
#     # Replace the actual function with the mock
#     services.configs.read_config = mock_read_config
    
#     # Test the read_config function
#     result = services.read_config()
    
#     # Assertions
#     assert result == {"background": "white", "main_color": "blue", "font_size": "12"}
#     mock_read_config.assert_called_once()


# def test_update_config_valid_key():
#     # Mock configs.update_config() to return True for a valid key
#     mock_update_config = mock.Mock(return_value=True)
    
#     # Replace the actual function with the mock
#     services.configs.update_config = mock_update_config
    
#     # Test the update_config function with a valid key
#     result = services.update_config("background", "gray")
    
#     # Assertions
#     assert result is True
#     mock_update_config.assert_called_once_with("background", "gray")


# def test_update_config_invalid_key():
#     # Mock configs.update_config() to return False for an invalid key
#     mock_update_config = mock.Mock(return_value=False)
    
#     # Replace the actual function with the mock
#     services.configs.update_config = mock_update_config
    
#     # Test the update_config function with an invalid key
#     result = services.update_config("invalid_key", "value")
    
#     # Assertions
#     assert result is False
#     mock_update_config.assert_called_once_with("invalid_key", "value")
