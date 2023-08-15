def get_code_main_color(color: str) -> str:
    color_map = {'pink': '#F099B1', 'green': '#85DABB'}
    return color_map.get(color, '')


def get_code_bg_color(color_mode: str) -> str:
    color_map = {'light': '#f8f8f8', 'dark': '#CCCCCC'}
    return color_map.get(color_mode, '')


def validate_float_input(new_value):
    try:
        if new_value == "" or float(new_value):
            return True
    except ValueError:
        return False
    return False
