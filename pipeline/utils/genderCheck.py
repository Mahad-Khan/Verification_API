# [ex]: passport_reading "M" or "F" (string)
# [ex]: prediction is a "Man" or "Woman" (string)
# - Sex on driver's licenses and passporteye is formatted the same way ('M' or 'F')
def genderCheck(passport_reading, prediction, doc_type='passport'):
    if passport_reading == "M" and prediction == "Man":
        return True
    elif passport_reading == "F" and prediction == "Woman":
        return True
    else:
        return False