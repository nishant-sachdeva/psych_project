import pandas as pd
import numpy as np

scoreDict = {
    'Not At All' : 1,
    'Several Days' : 2,
    'More than Half the days' : 3,
    'Nearly Everyday' : 4
}
def scoreData(x):
    return x.apply(lambda x: scoreDict[x])

def get_correlations(stressScores, avgStepCount):
    pass

def get_stress_score(stressColmns):
    pass

def get_step_count(stepColmns):
    pass

def generate_scores(fileName):
    # read the file
    filePath = "../data/" + fileName
    df = pd.read_csv(filePath)
    df = df.dropna()
    # get the required colmns
    stressScores = df[list(df)[9:]].apply(scoreData)
    avgStepCount = df[list(df)[1:8]]

    for stressRow, stepRow in zip(stressScores.iterrows(), avgStepCount.iterrows()):
        stressScores.append(get_stress_score(stressRow))
        avgStepCount.append(get_step_count(stepRow))
    
    return stressScores, avgStepCount



if __name__ == "__main__":
    # fileName = input("Please enter the file name > ")
    fileName = "psych_responses.csv"
    stressScores, avgStepCount = generate_scores(fileName)
    get_correlations(stressScores, avgStepCount)