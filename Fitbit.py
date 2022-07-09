import pandas as pd
import os
import json
import datetime as dt

def sleep_data():
    path = r'/Users/ericcollins/Documents/Python/Fitbit_Project/MyFitbitData/EricCollins/Sleep/'
    df = pd.DataFrame()
    for file in os.listdir(path):
        filepath = (path+'/'+file)
        if file.startswith('sleep') == True & file.endswith('.json') == True:
            # load data using Python JSON module
            with open(filepath,'r') as f:
                data = json.loads(f.read())
            # Flatten data
                df_nested_list = pd.json_normalize(data)
                df = pd.concat([df,df_nested_list])

    df = df[['dateOfSleep','startTime','endTime','duration','minutesAsleep','minutesAwake','timeInBed','levels.summary.restless.minutes','levels.summary.deep.minutes','levels.summary.light.minutes','levels.summary.rem.minutes']]
    df=df.rename(columns={'levels.summary.restless.minutes':'restlessMinutes','levels.summary.deep.minutes':'minutesDeep',
                            'levels.summary.light.minutes':'minutesLight','levels.summary.rem.minutes':'minutesREM'})
    df['dateOfSleep']=pd.to_datetime(df['dateOfSleep'])

    return df

def zone_minutes():
    path = r'/Users/ericcollins/Documents/Python/Fitbit_Project/MyFitbitData/EricCollins/Physical Activity/'
    df = pd.DataFrame()
    for file in os.listdir(path):
        filepath = (path+'/'+file)
        if file.startswith('Active Zone Minutes') & file.endswith('.csv'):
            data = pd.read_csv(filepath)
            df = pd.concat([df,data])
    df = df.sort_values(by='date_time')


    df['date_time']=pd.to_datetime(df['date_time'])
    df['date'] = df['date_time'].dt.date
    df['time'] = df['date_time'].dt.time

    df.groupby('date').sum()

    return df


def distance():
    path = r'/Users/ericcollins/Documents/Python/Fitbit_Project/MyFitbitData/EricCollins/Physical Activity/'
    df = pd.DataFrame()
    for file in os.listdir(path):
        filepath = (path+'/'+file)
    if file.startswith('distance-') & file.endswith('.json'):
        data = pd.read_json(filepath)
        df = pd.concat([df,data])
    df = df.sort_values(by='dateTime')

    import datetime as dt
    df['dateTime']=pd.to_datetime(df['dateTime'])
    df['date'] = df['dateTime'].dt.date
    df['time'] = df['dateTime'].dt.time

    df.groupby('date').sum()

    return df

def calories():
    path = r'/Users/ericcollins/Documents/Python/Fitbit_Project/MyFitbitData/EricCollins/Physical Activity/'
    df = pd.DataFrame()
    for file in os.listdir(path):
        filepath = (path+'/'+file)
    if file.startswith('calories-') & file.endswith('.json'):
        data = pd.read_json(filepath)
        df = pd.concat([df,data])
    df = df.sort_values(by='dateTime')

    import datetime as dt
    df['dateTime']=pd.to_datetime(df['dateTime'])
    df['date'] = df['dateTime'].dt.date
    df['time'] = df['dateTime'].dt.time

    df.groupby('date').sum()

    return df

def sedentary_minutes():
    path = r'/Users/ericcollins/Documents/Python/Fitbit_Project/MyFitbitData/EricCollins/Physical Activity/'
    df = pd.DataFrame()
    for file in os.listdir(path):
        filepath = (path+'/'+file)
    if file.startswith('sedentary_') & file.endswith('.json'):
        data = pd.read_json(filepath)
        df = pd.concat([df,data])
    df = df.sort_values(by='dateTime')

    import datetime as dt
    df['dateTime']=pd.to_datetime(df['dateTime'])
    df['date'] = df['dateTime'].dt.date
    df['time'] = df['dateTime'].dt.time

    df.groupby('date').sum()

    return df