import pandas as pd

file_path=r"CTA_-_Ridership_-_Daily_Boarding_Totals_20250807.csv"
df=pd.read_csv(file_path)


df['bus']=df['bus'].str.replace(',', '',regex=False)


df['bus']=df['bus'].astype(int)

df['rail_boardings']=df['rail_boardings'].str.replace(',','', regex=False)
df['rail_boardings']=df['rail_boardings'].astype(int)
df['total_rides']=df['total_rides'].str.replace(',','',regex=False)
df['total_rides']=df['total_rides'].astype(int)


print("Data Type Conversion Completed")


print(df.info())