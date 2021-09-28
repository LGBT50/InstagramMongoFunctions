import pandas as pd 
  
# Read csv file  
def getNCAABBall():
    df = pd.read_csv("NCAAinstagrams.csv") 
    # Print it out if you want to...
    print(df)
    names = []
    for index, row in df.iterrows():
        name = row["names"]
        name = name.replace("https://www.instagram.com/","")
        name = name.replace("/?hl=en", "")
        name = name.replace("/", "")
        if ("p/" and "https") not in name:
            for x in name:
                if x != "p":
                    names.append(name)
                    print(name)
                break
    return names



