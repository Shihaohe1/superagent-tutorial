def c_to_f(celsius):
    """摄氏度转华氏度。0°C 应该是 32°F。"""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    """华氏度转摄氏度。"""
    return (fahrenheit - 32) * 5 / 9
