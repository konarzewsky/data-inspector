def get_margins(value, unit):
    assert unit in ["v", "px"]
    margins = {}
    if unit == "v":
        margins["margin-top"] = f"{value}vh"
        margins["margin-bottom"] = f"{value}vh"
        margins["margin-left"] = f"{value}vw"
        margins["margin-right"] = f"{value}vw"
    else:
        margins["margin-top"] = f"{value}px"
        margins["margin-bottom"] = f"{value}px"
        margins["margin-left"] = f"{value}px"
        margins["margin-right"] = f"{value}px"
    return margins
