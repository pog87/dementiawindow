# Description
We'll be analyzing cortical thickness values of normal, pre-clinical and clinical populations in pre-determined fronto-parietal ROIs as a function of age, beta amyloid values(for the HBA) and behavioral measures (for the datasets that have made them available).

As most of the literature focuses on memory decline in healthy older individuals and Alzheimer's patients, we aim at extending the current knowledge of cognitive decline to the executive functions' field, by correlating cortical thickness measures with behavioral performance on executive functions' tasks that are similar across the datasets.

We'll be using the DLBS dataset as a training set and the ADNI healthy control subsample as a replication set. The HAB dataset will be considered as an explorative pre-clinical set before actually testing the distance of MCI and AD patients from the normal curve.

In this way, by performing this analysis on the full spectrum, we will be able to trace a continuous trajectory between the normal, pre-clinical and clinical population as far as cognitive control decline is concerned.

# Theoretical Motivation
# Research Design
TRAINING SET
Dallas Lifespan Brain Study(n=315 NORMAL CONTROLS age: 20-89 y/o):
1. Run the Freesurfer pipelines
2. Freesurfer Qc --> manual assessment with tkmedit for biggest issues: adding control points, white matter filling, editing the pial 
3. Extract cortical thickness measures of fronto-parietal ROIs (to be defined: dLPC, ACC, IPL, IFG?)
4. Correlation 1: Cortical Thickness ROIs x Age
5. Correlation 2: Behavioral Performance in the Cambridge Neuropsychological Test Automated Battery x Age
4. Brain-Behavior correlation: Interaction between age x cortical thickness ROIs x performance in the Cambridge Neuropsychological Test Automated Battery

REPLICATION SET
Alzheimer's Disease Neuroimaging Initiative(n=150 RANDOMLY CHOSEN HEALTHY CONTROLS age:   ):
1. Run the Freesurfer pipelines
2. Freesurfer Qc --> manual assessment with tkmedit for biggest issues: adding control points, white matter filling, editing the pial 
3. Extract cortical thickness measures of fronto-parietal ROIs
4. Correlation 1: Cortical Thickness ROIs x Age
5. Correlation 2: Behavioral Performance in the Trail Making Test x Age
6. Brain-Behavior correlation: Interaction age x thickness ROIs x performance TMT

PRE-CLINICAL SET
Harvard Brain Aging (n=284 COGNITIVELY NORMAL age: 60-90 y/o):
1. Correlation 1: Cortical Thickness ROIs x Age
2. Correlation 2: beta amyloid x Age --> high beta amyloid subjects vs low beta amyloid subjects
3. Beta amyloid values x thickness ROIs x age
4. Behavioral Performance in Trail Making Test x age 
5. Behavioral Performance in TMT x cortical thickness
6. Subj with high/low beta amyloid: cortical thickness x Behavioral Perfomance in Trail Making Test x age

TEST SET
Alzheimer's Disease Neuroimaging Initiative (n=300 evenly distributed between EMCI,MCI,LMCI and AD):
1. Run the Freesurfer pipelines
2. Freesurfer Qc --> manual assessment with tkmedit for biggest issues: adding control points, white matter filling, editing the pial 
3. Extract cortical thickness measures of ROIs
4. Histogram 1: Cortical Thickness ROIs in each group
5. Histogram 2: Behavioral Performance in the Trail Making Test x each group
6. Correlation: Thickness ROIs x Performance in each Group

FINAL STEP:
Overlapping curves and computing distances:
1. Are DLBS and ADNI normal controls overlapping?
2. Are the normal curves and the HAB curve any different? Can we use it to predict later cognitive impairment?
3. Can we predict the degree of cognitive impairment(pre-clinical, EMCI, MCI, LMCI, AD) based on the distance of the subjects from the normal curve? 


# Statistical Analysis
# Code Development 
