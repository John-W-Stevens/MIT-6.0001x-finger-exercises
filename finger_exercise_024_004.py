# Figure 24.15 code:

def applyModel(model, testSet, label, prob = 0.5):
    # Create vector containing feature vectors for all test examples
    testFeatureVectors = [e.getFeatures() for e in testSet]
    probs = model.predict_proba(testFeatureVectors)
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][i] > prob:
            if testSet[i].getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else:
            if testSet[i].getLabel() == label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

examples = buildMarathonExamples('bm_results2012.txt')
training, test = divide80_20(examples)

featureVecs, labels = [], []
for e in training:
    featureVecs.append([e.getAge(), e.getTime()])
    labels.append(e.getLabel())

model = sklearn.linear_model.LogisticRegression(),fit(featureVecs, labels)

print('Feature weights for label M:',
      'age = ', str(round(model.coef_[0][0], 3)) + ',',
      'time = ', round(model.coef[0][1], 3))

truePos, falsePos, trueNeg, falseNeg = applyModel(model, text, 'M', 0.5)

getStats(truePos, falsePos, trueNeg, falseNeg)

# Write code to plot the ROC curve and compute the AUROC when the model built in Figure 24.15 is tested
# on 200 randomly chosen competitors. Use that code to investiage the impact of the number of training
# examples (try varying it from 10 to 1010 in increments of 50) on the AUROC.
