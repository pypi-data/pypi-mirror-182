# str2float

There are 3 ways to group the number ten thousand with digit group separators:
1. **Space:** the internationally recommended thousands separator.
2. **Point:** the thousands separator used in many non-English speaking countries.
3. **Comma:** the thousands separator used in most English-speaking countries.

![thousands separators](https://upload.wikimedia.org/wikipedia/commons/3/3a/Thousands_separators.gif)

---

In which, there are 2 types of decimal separators:
1. Decimal **point**
2. Decimal **comma**

![decimal separators](https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Common_decimal_separators_-_Decimal_point_and_decimal_comma.png/440px-Common_decimal_separators_-_Decimal_point_and_decimal_comma.png)

---

This package will help convert float string (decimal point or decimal comma) to float!

## Installation:
https://pypi.org/project/str2float/

    pip install str2float

## Usage:

    from str2float import str2float
    float = str2float(str_float)
        
## Example:

    from str2float import str2float


    if __name__ == "__main__":
        assert str2float("1") == 1.0
        assert str2float("1.2345") == 1.2345
        assert str2float("1.23") == 1.23
        assert str2float("1.2") == 1.2
        assert str2float("1,2345") == 1.2345
        assert str2float("1,23") == 1.23
        assert str2float("1,2") == 1.2
        assert str2float("1234,5") == 1234.5
        assert str2float("1.234,5") == 1234.5
        assert str2float("1,234.5") == 1234.5
        assert str2float("1,234,567.85") == 1234567.85
        assert str2float("1.234.567,85") == 1234567.85

---

**_From [hoangyell](https://hoangyell.com/) with love_** 😘
