import pandas as pd
import numpy as np
from correlation import pearson, spearman, kendall

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
    df = pd.read_csv(filePath)
    df = df.dropna()

    stressScores = df[list(df)[9:]].apply(scoreData)
    avgStepCount = df[list(df)[1:7]]

    stressScores = stressScores.sum(axis=1)
    avgStepCount = avgStepCount.sum(axis=1)

    return stressScores, avgStepCount



if __name__ == "__main__":
    # fileName = input("Please enter the file name > ")
    fileName = "psych_responses.csv"
    stressScores, avgStepCount = generate_scores(fileName)
    pearson, spearman, kendall = get_correlations(stressScores, avgStepCount)
    print(pearson, spearman, kendall)