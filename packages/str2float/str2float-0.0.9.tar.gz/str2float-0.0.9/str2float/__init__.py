def str2float(string: str, default: float = 0.0):
    """
    str2float: convert float string (decimal point or decimal comma) to float
    :param string: string value | eg: "1,234,567.85"
    :param default: default value | eg: 0.0
    :return: float: result | eg: 1234567.85
    """
    try:
        value = 0
        string = string.replace(" ", "")
        sign = -1 if string.startswith("-") else 1
        num_dot = string.count(".")
        num_com = string.count(",")
        if num_dot == 0:
            if num_com > 1:
                value = string.replace(",", "")
            elif num_com == 1:
                value = string.replace(",", ".")
            else:
                value = string
        elif num_com == 0:
            if num_dot > 1:
                value = string.replace(".", "")
            else:
                value = string
        elif (num_dot >= 1 and num_com == 1) or (num_dot == 1 and num_com >= 1):
            index_dot = string.find(".")
            index_com = string.find(",")
            if index_dot < index_com:
                value = string.replace(".", "").replace(",", ".")
            else:
                value = string.replace(",", "")
        else:
            # num_dot > 1 and num_com > 1:
            raise ValueError(f"invalid format: {string}")
        float_value = float(value) * sign
    except:
        float_value = default
    return float_value
