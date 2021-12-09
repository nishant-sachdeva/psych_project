import pandas as pd
import numpy as np
from correlation import pearson, spearman, kendall
import matplotlib.pyplot as plt

scoreDict = {
    'Not At All' : 1,
    'Several Days' : 2,
    'More than Half the days' : 3,
    'Nearly Everyday' : 4
}
def scoreData(x):
    return x.apply(lambda x: scoreDict[x])

def get_correlations(stressScores, avgStepCount):
    pearsonScore = pearson(stressScores.values.tolist(), avgStepCount.values.tolist())
    spearmanScore = spearman(stressScores.values.tolist(), avgStepCount.values.tolist())
    kendallScore = kendall(stressScores.values.tolist(), avgStepCount.values.tolist())
    return [pearsonScore, spearmanScore, kendallScore]

def generate_scores(fileName):
    filePath = "../data/" + fileName

    try:
        df = pd.read_csv(filePath)
        df = df.dropna()

        stressScores = df[list(df)[9:]].apply(scoreData)
        avgStepCount = df[list(df)[1:7]]

        stressScores = stressScores.sum(axis=1)
        avgStepCount = avgStepCount.mean(axis=1)

        return stressScores, avgStepCount
    except:
        print("Files could not be opened")
        return None, None



if __name__ == "__main__":
    # fileName = input("Please enter the file name > ")
    fileName = "psych_responses.csv"
    stressScores, avgStepCount = generate_scores(fileName)
    corrPlot = pd.concat([stressScores, avgStepCount], join='outer', axis=1)
    corrPlot.to_csv("../data/averageScores.csv", sep=',')
    print(list(corrPlot))



    if stressScores is not None and avgStepCount is not None:
        
        pearson, spearman, kendall = get_correlations(stressScores, avgStepCount)
        print("Pearson Correlation ", pearson)
        print("Spearman Correlation ", spearman)
        print("Kendall Correlation ", kendall)
    else:
        print("Scores could not be calculated. File opening error")