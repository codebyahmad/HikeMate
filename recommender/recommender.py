# %%
import pandas as pd
import os
from ast import literal_eval
import numpy as np

from sklearn.preprocessing import MinMaxScaler



# %%
mydir = os.getcwd()

# %%
alltrails = pd.read_csv('../data/alltrails-data.csv')



 #   Column            Non-Null Count  Dtype        Notes
# ---  ------            --------------  -----  
#  0   trail_id          7883 non-null   int64   
#  1   name              7881 non-null   object 
#  2   city              7883 non-null   object 
#  3   region_name       7883 non-null   object 
#  4   country_name      7883 non-null   object 
#  5   _geoloc           7883 non-null   object 
#  6   popularity        7838 non-null   float64    the larger the value, the more popular the trail? 1-100
#  7   length            7883 non-null   float64    
#  8   elevation_start   7883 non-null   float64
#  9   elevation_gain    7883 non-null   float64
#  10  elevation_max     7883 non-null   float64
#  11  unit              7883 non-null   object 
#  12  duration_minutes  7883 non-null   float64
#  13  avg_rating        7883 non-null   float64
#  14  difficulty        7883 non-null   int64      1-7
#  15  visitor_usage     7883 non-null   float64    meaning?
#  16  season            7883 non-null   object 
#  17  route_type        7883 non-null   object 
#  18  review_count      7883 non-null   int64      meaning?-> num of reviews
#  19  photo_count       7883 non-null   int64      meaning?-> num of photos-> irrelevant
#  20  track_count       7883 non-null   int64      meaning?-> subtracks of this trail -> irrelevant
#  21  completed_count   7883 non-null   int64      meaning?-> how many users have completed this trail.
#  22  activities        7883 non-null   object 
#  23  features          7883 non-null   object 
#  24  obstacles         7883 non-null   object 
#  25  slug              7883 non-null   object     meaning?
#  26  overview          7883 non-null   object

# %%
def print_full_df(df):
    '''
    print full content of a df
    '''
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
        print(df)


def count_num_of_values(df, col, bar):
    '''
    get an overview of the value number in a certain column

    code cf. https://github.com/tweichle/California-Trail-Finder/blob/main/(4)%20Trail%20Info%20EDA%20and%20Create%20Pandas%20DataFrame.ipynb
    '''
    value_num = df[col].value_counts()
    overview = value_num.rename_axis(col).reset_index(name='counts')
    overview['pct'] = round(overview['counts'] / sum(overview['counts']), 4)


    # if bar:
    #     ax = df[col].value_counts(normalize=True).plot(kind='bar')
    #     ax.set_ylabel('pct')

    return overview

def convert_tag_col_to_dummies(df, col_list):
    '''
    convert the columns containing tag text to dummy varible,
    use literal_eval to parse the json format data to python format
    '''
    tag_dummy_list = []

    for col in col_list:
        tag_dummy = df[col].apply(literal_eval).str.join(sep='|').str.get_dummies()
        tag_dummy_list.append(tag_dummy)
    
    tag_dummy_df = pd.concat(tag_dummy_list, axis=1)
    df_with_dummies = pd.concat([df, tag_dummy_df], axis=1)
    return df_with_dummies

def convert_categorical_variable_to_dummy(df, col, dummy_col_prefix):
    '''
    convert categorical column difficulty_level and route_type_coded
    into dummy variables
    
    '''
    df = df.join(pd.get_dummies(df[col], prefix=dummy_col_prefix, drop_first=False))
    return df
   
# %%
# eda

# null values

alltrails.isnull().sum()

# %%
# drop 2 trails with no trail name
# of course possbile to search online and add name 
# yet it should be fine just drop 2 trails

alltrails_drop_no_names = alltrails[~alltrails['name'].isnull()].reset_index(drop=True)

# %%
value_num_cantons = count_num_of_values(alltrails_drop_no_names, 'region_name', bar = True)
# %%
value_num_cantons['region_name'].sort_values(ascending=True)
# %%
count_num_of_values(alltrails_drop_no_names, 'difficulty', bar = True)
# %%
# convert difficulty level to common text

pd.set_option('mode.chained_assignment', None)
alltrails_drop_no_names.loc[:, 'difficulty_level'] = list(alltrails_drop_no_names['difficulty'].map({1: 'Easy', 3: 'Moderate', 5: 'Hard', 7: 'Hard'}))
# %%
# convert length from m to km

alltrails_drop_no_names.loc[:, 'length_km'] = alltrails_drop_no_names['length'].apply(lambda x: round(x/1000, 1))
# %%
# convert elevation to int

alltrails_drop_no_names.loc[:, 'elevation_start_m'] = alltrails_drop_no_names['elevation_start'].apply(lambda x: int(round(x, 0)))
alltrails_drop_no_names.loc[:, 'elevation_gain_m'] = alltrails_drop_no_names['elevation_gain'].apply(lambda x: int(round(x, 0)))
alltrails_drop_no_names.loc[:, 'elevation_max_m'] = alltrails_drop_no_names['elevation_max'].apply(lambda x: int(round(x, 0)))
# %%
# convert 'activities', 'features', 'obstacles' to dummy variables

# values info

#alltrails_drop_no_names['activities'].apply(literal_eval).explode().unique()
#alltrails_drop_no_names['features'].apply(literal_eval).explode().unique()
#alltrails_drop_no_names['obstacles'].apply(literal_eval).explode().unique()
#alltrails_drop_no_names['season'].unique()
#alltrails_drop_no_names['route_type'].unique()

# %%
# coding season

alltrails_drop_no_names['season'] = alltrails_drop_no_names['season'].apply(literal_eval)
alltrails_drop_no_names.insert(len(alltrails_drop_no_names.columns), 'season_coded', '')


# winter season: Nov to April (11 to 4)
# summer season: Juni to Sep (6 to 9)
# all year

ws_start = [9, 10, 11, 12, 1]
#ws_end = [11, 12, 1, 2, 3, 4, 5]
ss_start = [2, 3, 4, 5, 6, 7, 8]
#ss_end = [7, 8, 9, 10]

for i in range(0, len(alltrails_drop_no_names)):
   
    if (alltrails_drop_no_names['season'].iloc[i]['start'] != None) & (alltrails_drop_no_names['season'].iloc[i]['end'] != None):
        
        if abs(alltrails_drop_no_names['season'].iloc[i]['start']) == abs(alltrails_drop_no_names['season'].iloc[i]['end']):
            alltrails_drop_no_names.loc[i, 'season_coded'] = 'Summer, Winter, All year'

        elif abs(alltrails_drop_no_names['season'].iloc[i]['end']) - abs(alltrails_drop_no_names['season'].iloc[i]['start']) == 11:
            alltrails_drop_no_names.loc[i, 'season_coded'] = 'Summer, Winter, All year'

        elif (abs(alltrails_drop_no_names['season'].iloc[i]['start']) in ws_start) & (alltrails_drop_no_names.loc[i, 'season_coded'] != 'Summer, Winter, All year'):
            if (alltrails_drop_no_names.loc[i, 'season_coded'] != 'Summer'):
                alltrails_drop_no_names.loc[i, 'season_coded'] = 'Winter'

            elif (alltrails_drop_no_names.loc[i, 'season_coded'] == 'Summer'):
                alltrails_drop_no_names.loc[i, 'season_coded'] = 'Summer, Winter'

            else:
                alltrails_drop_no_names.loc[i, 'season_coded'] = 'unavailable'
        
        elif (abs(alltrails_drop_no_names['season'].iloc[i]['start']) in ss_start) & (alltrails_drop_no_names.loc[i, 'season_coded'] != 'Summer, Winter, All year'):
            if (alltrails_drop_no_names.loc[i, 'season_coded'] != 'Winter'):
                alltrails_drop_no_names.loc[i, 'season_coded'] = 'Summer'

            elif (alltrails_drop_no_names.loc[i, 'season_coded'] == 'Winter'):
                alltrails_drop_no_names.loc[i, 'season_coded'] = 'Summer, Winter'

            else:
                alltrails_drop_no_names.loc[i, 'season_coded'] = 'unavailable'

        else:
            alltrails_drop_no_names.loc[i, 'season_coded'] = 'unavailable'
     

# %%
alltrails_drop_no_seasons = alltrails_drop_no_names[~alltrails_drop_no_names['season_coded'].isnull()].reset_index(drop=True)

# %%
# coding route_type

alltrails_drop_no_seasons['route_type'] = alltrails_drop_no_seasons['route_type'].apply(literal_eval)

for i in range(0, len(alltrails_drop_no_seasons)):
    
    if alltrails_drop_no_seasons['route_type'].iloc[i]['uid'] == 'O':
        alltrails_drop_no_seasons.loc[i, 'route_type_coded'] = 'Out & Back'
    
    elif alltrails_drop_no_seasons['route_type'].iloc[i]['uid'] == 'L':
        alltrails_drop_no_seasons.loc[i, 'route_type_coded'] = 'Loop'

    else:
        alltrails_drop_no_seasons.loc[i, 'route_type_coded'] = 'Point to Point'

# %%
# set dummy for season


season_coded_dummy = alltrails_drop_no_seasons['season_coded'].str.get_dummies()
season_coded_dummy.loc[season_coded_dummy['Summer, Winter, All year'] == 1, ['Summer', 'Winter']] = 1
season_coded_dummy.rename(columns={'Summer, Winter, All year': 'All year'}, inplace=True)
alltrails_drop_no_seasons = pd.concat([alltrails_drop_no_seasons, season_coded_dummy], axis=1)


# %%
# set dummy for  ['activities', 'features', 'obstacles']

alltrails_with_dummies = convert_tag_col_to_dummies(df = alltrails_drop_no_seasons, col_list = ['activities', 'features', 'obstacles'])

# %%
# drop irrelevant cols

alltrails_contend_based_re_transformed = alltrails_with_dummies.drop(columns=['country_name', '_geoloc', 'popularity', 'length', 'elevation_start', 'elevation_gain', 'elevation_max', 'unit', 'difficulty',
       'visitor_usage', 'season', 'route_type', 'review_count', 'photo_count',
       'track_count', 'completed_count', 'activities', 'features', 'obstacles', 'slug'])

# %%
# set dummy for 'difficulty_level' and 'route_type_coded'

alltrails_contend_based_re_transformed =  convert_categorical_variable_to_dummy(alltrails_contend_based_re_transformed, ['difficulty_level'], 'difficulty_level')
alltrails_transformed_final = convert_categorical_variable_to_dummy(alltrails_contend_based_re_transformed, ['route_type_coded'], 'route_type')

print_full_df(alltrails_transformed_final.isnull().sum())

# %%
# features (columns) used for recommendation

numerical_cols = ['duration_minutes', 'length_km', 'elevation_gain_m', 'elevation_max_m']

categorical_to_dummy_cols = ['difficulty_level_Easy', 'difficulty_level_Hard',
       'difficulty_level_Moderate', 'route_type_Loop', 'route_type_Out & Back',
       'route_type_Point to Point']

season_tags = ['Summer', 'All year', 'Winter']

activities_tags = ['backpacking', 'birding', 'fishing', 'hiking', 'trail-running',
       'skiing', 'mountain-biking', 'camping', 'walking', 'snowshoeing',
       'rock-climbing', 'bike-touring', 'road-biking', 'scenic-driving',
       'via-ferrata', 'cross-country-skiing', 'paddle-sports',
       'horseback-riding', 'off-road-driving']

features_tags = ['lake', 'river', 'views', 'wild-flowers', 'wildlife', 'forest',
       'dogs-leash', 'partially-paved', 'historic-site', 'dogs',
       'waterfall', 'dogs-no', 'beach', 'cave', 'kids', 'city-walk',
       'paved', 'strollers', 'ada', 'rails-trails', 'event', 'pub-crawl',
       'hot-springs']

obstacles_tags = ['no-shade', 'rocky', 'scramble', 'snow', 'fee', 'muddy',
       'bridge-out', 'off-trail', 'bugs', 'over-grown', 'washed-out',
       'blowdown', 'private-property']

recommender_cols = numerical_cols + categorical_to_dummy_cols + season_tags + activities_tags + features_tags + obstacles_tags

recommender_df = alltrails_transformed_final[recommender_cols]

# %%
# scale all column values to [0~1]
scaler = MinMaxScaler()
scaler.fit(recommender_df)

recommender_df_scaled = pd.DataFrame(scaler.transform(recommender_df), columns=recommender_cols)

# add trail id
recommender_df_scaled.loc[:, 'trail_id'] = alltrails_transformed_final['trail_id']


# %%
# calculate cosine similarity and get recommendations

def get_cosine_similarity(x, y):

    '''
    function cf. lecture notebook
    
    '''
    numerator = np.dot(x,y)
    denominator = np.linalg.norm(x) * np.linalg.norm(y)

    # sanity check: x and y must be non-zero vectors
    if denominator > 0:
        sim = numerator / denominator
    else:
        raise Exception("The cosine similarity is not defined for vectors containing only zeros!")

    return sim

def recommender(df, query_trail_id, recommender_model_columns, n):

    '''
    recommendation function cf. lecture notebook
    "Content-Based Movie Recommendations"
    '''

    trails = df['trail_id']
    indices = pd.Series(df.index, index=df['trail_id'])

    # get the row number of the query trail
    idx = indices[query_trail_id]

    # get row cols of the query trail
    query_trail = df.iloc[idx][recommender_model_columns].to_numpy()

    # compute cs between the query trail and the rest trails
    similarities = []

    for i in range(len(df)):

        if i != idx:

            other_trail = df.iloc[i][recommender_model_columns].to_numpy()

            cs = get_cosine_similarity(query_trail, other_trail)
            similarities.append((i, cs))

    sorted_cs = sorted(similarities, key=lambda x: x[1], reverse=True)
    sorted_cs = sorted_cs[:n]
    
    # extract index of the recommended trail
    trail_indices = [pair[0] for pair in sorted_cs]

    # merge the recommended trail to  alltrails_transformed_final

    return trails.iloc[trail_indices].to_frame()

# example: query trail id 10259747
# get top 100 recommendations

recommendations = recommender(df = recommender_df_scaled, query_trail_id = 10259747, recommender_model_columns = recommender_cols, n = 100)

# %%
# show the full recommendation columns
recommendations_df = recommendations.merge(alltrails_transformed_final, on = 'trail_id', how = 'left')
print(recommendations_df)



