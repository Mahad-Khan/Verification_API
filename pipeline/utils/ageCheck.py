def ageCheck(doc_date_of_birth, predicted_age, doc_type='passport'):
    CURRENT_YEAR = 2020
    TWENTIETH_CENTURY_BASE = '19'
    TWENTIFIRST_CENTURY_BASE = '20'
    
    doc_date_birth_year = doc_date_of_birth[0:2]
    doc_date_birth_year = int(doc_date_birth_year)
    
    if doc_date_birth_year == int('00') or doc_date_birth_year == int('01') or doc_date_birth_year == int('02'):
        birth_year = TWENTIFIRST_CENTURY_BASE+str(doc_date_birth_year)
        birth_year = int(birth_year)
    else:
        birth_year = TWENTIETH_CENTURY_BASE+str(doc_date_birth_year)
        birth_year = int(birth_year)
    age_from_doc = CURRENT_YEAR - birth_year
    predicted_age = int(predicted_age)
    # 5 year swing in either direction?
    if (age_from_doc - 5) <= predicted_age and (age_from_doc + 5) >= predicted_age:
        return True
    else:
        return False