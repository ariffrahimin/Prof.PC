import pandas as pd
from pathlib import Path

datasets_path = Path.joinpath(Path.cwd(),'dataset')
df3 = pd.read_excel(Path.joinpath(datasets_path,'game_data.xlsx'))

fullJsonMiddleFormat = ""
for i in range(len(df3)):
    # print(df3['GAMES'].iloc[i])
    tagKey = """{"tag":"""
    tagValue = "'" + str(f"{df3['GAMES'].iloc[i]}") + "',"
    TAG = tagKey + tagValue

    patternsKey = """"patterns":"""
    patternsValue = "'" + f"{df3['GAMES'].iloc[i]} requirements" + "'" + "," + "'" + f"{df3['GAMES'].iloc[i]}" + "'"
    PATTERNS = patternsKey + f"[{patternsValue}]," 




    responsesKey = """"responses":"""
    responsesValue = "['MINIMUM" + f"{df3['MR'].iloc[i]}" + "RECOMMENDED" + f"{df3['RR'].iloc[i]}" + "'],"
    REPONSES = responsesKey + f"{responsesValue}" 


    jsonMiddleFormat = "\n\t" + TAG + "\n\t" + PATTERNS + "\n\t" + REPONSES + "\n\t" + """"context": [""]},\n\n\t"""
    fullJsonMiddleFormat = fullJsonMiddleFormat + jsonMiddleFormat

fullJsonFormat = """{"intents":[\n\t""" + fullJsonMiddleFormat[:-1] + """\n\t]}"""
# print(fullJsonFormat)
text_file = open("JSON.txt", "wt")
n = text_file.write(fullJsonFormat)
text_file.close()