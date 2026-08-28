import os
import pandas as pd

data={
    "name": [],
    "age": [],
    "city":[]
}

df=pd.DataFrame(data)

data_dir="data" #by name data a folder will be created
os.makedirs(data_dir,exist_ok=True)#exist_ok=True => if a folder name data already their then it will create it again

file_path=os.path.join(data_dir,"sample_data.csv") # a path defined inside data folder

#save the dataframe to csv file at this file path
df.to_csv(file_path,index=False)

print(f"csv file saved {file_path}")

