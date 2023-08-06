# # test_history.py

# from unittest import mock
# from django.conf import settings
# from pathlib import Path
# import history

# def test_read_file_empty():
#     # Mock Path.touch() to create an empty file
#     mock_touch = mock.Mock()
#     Path.touch = mock_touch
    
#     # Mock open() to return an empty list for file.readlines()
#     mock_file = mock.mock_open(read_data="")
#     with mock.patch("history.open", mock_file):
#         result = history.read_file()
    
#     # Assertions
#     assert result == []
#     mock_touch.assert_called_once_with(settings.DATA_FILE_PATH)
#     mock_file.assert_called_once_with(settings.DATA_FILE_PATH, 'r', encoding='utf-8')


# def test_read_file_non_empty():
#     # Mock Path.touch() to create a file
#     mock_touch = mock.Mock()
#     Path.touch = mock_touch
    
#     # Mock open() to return a list of lines for file.readlines()
#     mock_file = mock.mock_open(read_data="expr1\nexpr2\nexpr3\n")
#     with mock.patch("history.open", mock_file):
#         result = history.read_file()
    
#     # Assertions
#     assert result == ["expr1\n", "expr2\n", "expr3\n"]
#     mock_touch.assert_called_once_with(settings.DATA_FILE_PATH)
#     mock_file.assert_called_once_with(settings.DATA_FILE_PATH, 'r', encoding='utf-8')


# def test_clean():
#     # Mock Path.touch() to create a file
#     mock_touch = mock.Mock()
#     Path.touch = mock_touch
    
#     # Mock open() and file.truncate() to clear the file
#     mock_file = mock.mock_open()
#     with mock.patch("history.open", mock_file):
#         history.clean()
    
#     # Assertions
#     mock_touch.assert_called_once_with(settings.DATA_FILE_PATH)
#     mock_file.assert_called_once_with(settings.DATA_FILE_PATH, 'r+', encoding='utf-8')
#     mock_file.return_value.truncate.assert_called_once_with(0)


# def test_write():
#     # Mock Path.touch() to create a file
#     mock_touch = mock.Mock()
#     Path.touch = mock_touch
    
#     # Mock open() and file.readlines() to return a list of lines
#     mock_file = mock.mock_open(read_data="expr1\nexpr2\nexpr3\n")
#     with mock.patch("history.open", mock_file):
#         result = history.write("new_expression\n")
    
#     # Assertions
#     assert result == ["new_expression\n", "expr1\n", "expr2\n", "expr3\n"]
#     mock_touch.assert_called_once_with(settings.DATA_FILE_PATH)
#     mock_file.assert_called_once_with(settings.DATA_FILE_PATH, 'r', encoding='utf-8')
#     mock_file.return_value.readlines.assert_called_once()
#     mock_file.return_value.truncate.assert_not_called()
#     mock_file.return_value.write.assert_called_once_with("new_expression\n")
