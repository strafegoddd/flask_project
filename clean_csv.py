# import pandas as pd

# df = pd.read_csv('structures/imdb_2024.csv')

# columns_to_remove = [
#     'Home_Page', 'Overview', 'Storyline', 'Production_Company', 
#     'Release_Date', 'Tagline', 'Vote_Count', 'Revenue_$', 
#     'Run_Time_Minutes', 'Release_Country'
# ]
# df.drop(columns=columns_to_remove, inplace=True)

# df['Genres'] = df['Genres'].apply(lambda x: eval(x) if isinstance(x, str) else [])
# df['Cast'] = df['Cast'].apply(lambda x: eval(x) if isinstance(x, str) else [])
# df['Original_Language'] = df['Original_Language'].apply(lambda x: eval(x) if isinstance(x, str) else [])

# df.to_csv('cleaned_movies.csv', index=False)

# print("Файл успешно очищен и сохранён как cleaned_movies.csv")
