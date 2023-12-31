import string

def length_check(credentials: str) -> dict:
    if len(credentials) > 6:
        res = True
        return {"msg":"success","status":True}
    else:
        msg= "Lenght should be > 6"
        return {"status":False, "msg":msg}


def upper_case_check(credentials: str) -> dict:
    res = any( i.isupper() for i in credentials )
    return {"status": res, "msg": "success"} if res else {"status":res, "msg": "Credentials should contain upper character"}

def lower_case_check(credentials: str) -> dict:
    res = any(i.islower for i in credentials)
    return {"status": res, "msg": "success"} if res else {"status":res, "msg": "Credentials should contain lower character"}

def digit_check(credentials: str) -> dict:
    res = any(i.isdigit() for i in credentials)
    return {"status": res, "msg": "success"} if res else {"status":res, "msg": "Credentials should contain digit"}

def punctuation_check(credentials: str) -> dict:
    res = any(i in string.punctuation for i in credentials)
    return {"status": res, "msg": "success"} if res else {"status":res, "msg": "Credentials should contain special characters"}


def checks(credentials: str) -> dict:
    length_validation = length_check(credentials)
    if not length_validation.get("status"):
        return {"msg":"Length is less than 6", "status": length_validation.get("status")}
    
    
    upper_case_validation = upper_case_check(credentials)
    if not upper_case_validation.get("status"):
        return {"msg":"Doesn't contain upper case", "status": upper_case_validation.get("status")}
    
    lower_case_validation = lower_case_check(credentials)
    if not lower_case_validation.get("status"):
        return {"msg":"Doesn't contain lower case", "status": lower_case_validation.get("status")}
    
    digit_validation = digit_check(credentials)
    if not digit_validation.get("status"):
        return {"msg":"Doesn't contain digit", "status": digit_validation.get("status")}
    
    special_chars_validation = punctuation_check(credentials)
    if not special_chars_validation.get("status"):
        return {"msg":"Doesn't contain special chars", "status": special_chars_validation.get("status")}
        
    return {"msg": "Success", "status": True}
