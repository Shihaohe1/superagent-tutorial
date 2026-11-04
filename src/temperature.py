def c_to_f(celsius):
    """摄氏度转华氏度。0°C 应该是 32°F。"""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    """华氏度转摄氏度。"""
    return (fahrenheit - 32) * 5 / 9


def c_to_k(celsius):
    """摄氏度转开尔文。"""
    return celsius + 273.15


def k_to_c(kelvin):
    """开尔文转摄氏度。"""
    return kelvin - 273.15
