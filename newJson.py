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

    txt = df3['MR'].iloc[i]
    cpu = "\\" + "n" + txt[txt.find("CPU"):txt.find("GPU")] + "\\" + "n"
    gpu =  cpu + txt[txt.find("GPU"):txt.find("RAM")] + "\\" + "n"
    ram = gpu + txt[txt.find("RAM"):txt.find("VRAM")] + "\\" + "n"
    vram = ram + txt[txt.find("VRAM"):] + "\\" + "n" + "\\" + "n"
    
    txt2 = df3['RR'].iloc[i]
    cpu2 = "\\" + "n" + txt2[txt2.find("CPU"):txt2.find("GPU")] + "\\" + "n"
    gpu2 =  cpu2 + txt2[txt2.find("GPU"):txt2.find("RAM")] + "\\" + "n"
    ram2 = gpu2 + txt2[txt2.find("RAM"):txt2.find("VRAM")] + "\\" + "n"
    vram2 = ram2 + txt2[txt2.find("VRAM"):]

    responsesKey = """"responses":"""
    responsesValue = "['MINIMUM" + f"{vram}" + "\\" + "n" + "\\" + "n" + "RECOMMENDED" + f"{vram2}" + "'],"
    REPONSES = responsesKey + f"{responsesValue}"


    jsonMiddleFormat = "\n\t" + TAG + "\n\t" + PATTERNS + "\n\t" + REPONSES + "\n\t" + """"context": [""]},\n\n\t"""
    fullJsonMiddleFormat = fullJsonMiddleFormat + jsonMiddleFormat

fullJsonFormat = """{"intents":[\n\t""" + fullJsonMiddleFormat[:-1] + """\n\t]}"""
# print(fullJsonFormat)

#convert json to text file
text_file = open("intents.json", "wt")
n = text_file.write(fullJsonFormat)
text_file.close()