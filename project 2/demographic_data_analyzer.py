import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('project 2/adult.data.csv')#,sep=',',decimal=',')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series()
    race_count = df['race'].value_counts()
    

    # What is the average age of men?
    df2 = df[(df['sex'] == 'Male')]
    average_age_men = round(df2['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    df3 = df[(df['education'] == 'Bachelors')]
    percentage_bachelors = round((df3['education'].count() / df['education'].count()) * 100,1)
    
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    df_with_education = df[df['education'].isin(advanced_education)] #filtramos el dataframe con la educacion avanzada. 
    df_without_education = df[~df['education'].isin(advanced_education)] #filtramos el dataframe por los que no tienen eduacion avanzada. 

    higher_education = (df_with_education['education'].count() / df['education'].count()) * 100 #porcentaje de la educacion avanzada SOLAMENTE!
    lower_education = (df_without_education['education'].count() / df['education'].count()) * 100 #calculo del porcentaje de personas con educacion no avanzada. 

    df_with_education_more50k = df_with_education[df_with_education['salary'] == '>50K']
    #en un nuevo dataframe (ya filtrada la educacion), filtramos el salario (>50K)
    df_without_education_more50k = df_without_education[df_without_education['salary'] == '>50K'] 
    #filtramos nuevamente el dataframe(ya filtrado por la educacion) por el salario >50K

    # percentage with salary >50K
    higher_education_rich = round(((df_with_education_more50k['education'].count() / df_with_education['education'].count() ) * 100),1)
    #calculo del porcentaje de personas con educacion avanzada con el salario >50K
    
    lower_education_rich = round(((df_without_education_more50k['education'].count() / df_without_education['education'].count()) * 100),1)
    #calculo del porcentaje de personas con educacion no avanzada con el salario >50k.

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_number = df[(df['hours-per-week'] == 1)] #filtramos el dataframe por las horas minimas de trabajo. 
    df_min_number_salary = df_min_number[(df_min_number['salary'] == '>50K')] #en otro dataframe(ya filtrado por las horas de trabajo), filtramos el salario. 
    
    num_min_workers = df_min_number['age'].count()

    rich_percentage = (num_min_workers / df_min_number_salary['age'].count()) 

    # What country has the highest percentage of people that earn >50K?
    high_salary = df[df.salary == '>50K']
    countries=df['native-country'].value_counts()
    countries_hs=high_salary['native-country'].value_counts()
    max_percentage=0

    for i in range(countries_hs.shape[0]):
        percentage_per_country=round((countries_hs[i]/countries[countries_hs.index[i]])*100,1)
        if percentage_per_country>=max_percentage:
            max_percentage=percentage_per_country
            name_of_country=countries_hs.index[i]
            
    highest_earning_country = name_of_country
    highest_earning_country_percentage = max_percentage

    # Identify the most popular occupation for those who earn >50K in India.
    high_salary_India = high_salary[high_salary['native-country'] == 'India']
    #filtramos el dataframe (ya filtrado por el salario), por el pais India
    
    occupation = high_salary_India['occupation'].value_counts() #vemos lo valores unicos de esta columna

    top_IN_occupation = occupation.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
