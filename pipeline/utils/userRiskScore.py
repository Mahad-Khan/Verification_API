import pandas as import pd

countries = pd.read_csv("country_scores.csv")

def provideCountryScore(country):
    """
    :param country: country to check the risk score of - ** capitalize first initial or clean .csv
    :return: the countries risk score or NaN if the country wasn't found
    ** Do a full sweep for edge cases and clean the .csv **
    [ex] edge cases: "Republic of", native spelling, etc.
        
    """
    country_row = countries.loc[countries['Country'] == country]
    ranking = country_row['Ranking']
    return ranking

# - the "ranking" variable that is returned is what needs to be the "country_score"...
#   ... arg in the "provideUserScore" function below.

def provideUserScore(country_score, first_name_results, last_name_results, age_results, gender_results):
    """
    :param country_score: score of the user's country
    :param country_score type: int
    :param first_name_results: boolean indicated manually entered first name is matched on the provided document.
    :param last_name_results: boolean indicating manually endtered last name is matched on the provided document.
    :param age_results: boolean indicating predicted age matches accepted age within defined threshold.
    :param gender_results: boolean indicating predicted gender matches the gender on the provided document.
    
    return: a score 1-5; 1 indicating a low risk applicant, and 5 indicating a risky applicant
    """
    country_component = 1
    
    if country_score >= 50 and country_score <= 98:
        country_component = 1
    elif country_score > 98 and country_score <= 143:
        country_component = 2
    elif country_score > 143 and country_score <= 192:
        country_component = 3
    elif country_score > 192:
        country_component = 4
        
    fn_component = 0
    
    if first_name_results == False:
        fn_component = 1
    
    ln_component = 0
    
    if last_name_results == False:
        ln_component = 1
        
    age_component = 0
    
    if age_results == False:
        age_component = 1
    
    gender_component = 0
    
    if gender_results == False:
        gender_component = 1
        
    user_score = country_component + fn_component + ln_component + age_component + gender_component
    
    if user_score > 5:
        return 5
    else:
        return user_score
