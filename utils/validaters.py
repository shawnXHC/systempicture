import re
# 这里面写一些验证器


# 验证手机号
def validate_phone(num):
    if isinstance(num, str):
        ret = re.match(r"^1[35678]\d{9}$", num)
    else:
        num = str(num)
        ret = re.match(r"^1[35678]\d{9}$", num)
    return bool(ret)


# 验证邮箱
def validate_email(email):
    # 邮箱格式后缀只能是.com|.gov|.net。
    verify_email = re.compile(r'^[\w][a-zA-Z1-9.]{4,19}@[a-zA-Z0-9]{2,3}.[com|gov|net]')
    result = verify_email.match(email)
    return bool(result)

