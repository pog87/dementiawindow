# 1. Description
We'll be analyzing and predicting cortical thickness values of normal, pre-clinical and clinical populations in pre-determined fronto-parietal ROIs as a function of age, beta amyloid values and behavioral measures (for the datasets that have made them available).

We'll be training and testing our classifier using data coming from the DLBS and the ADNI datasets (for replication purposes between datasets) as our healthy control subsample, from the HAB dataset as our explorative pre-clinical set and from the ADNI EMCI, MCI, LMCI, AD data as our clinical subsample. We'll be splitting each dataset into two halves: one will be used to train and one to test our classifier. Each subsample (normal-pre clinical-clinical) will have the same number of subjects that will be randomly chosen from each dataset. 

# 2.Theoretical Motivation

As most of the literature focuses on memory decline in healthy older individuals and Alzheimer's patients, we aim at extending the current knowledge of cognitive decline to the executive functions' field, by exploring the relation between thickness measures (and brain volume measures) and behavioral performance on executive functions' tasks that are similar across the datasets.

In this way, by performing this analysis on the full spectrum, we will be able to trace a continuous trajectory between the normal, pre-clinical and clinical population as far as cognitive control decline is concerned.
# 3. Research Design

## 3.1. Data sets
* **Normal Subsample**
1. Dallas Lifespan Brain Study (DLBS, n=315, healthy controls HC, age range: 20-89 y/o)
2. Randomly chosen healthy controls from Alzheimer's Disease Neuroimaging Initiative (ADNI, n=150 , HC,  age range: 55-90 y/o)
* **Pre-clinical subsample**
Harvard Brain Aging (HBA, n=284, Cognitively Normal CN age range: 60-90 y/o)
* **Clinical Subsample**
ADNI (n=300, evenly distributed between EMCI,MCI,LMCI and AD, age range: to be defined )

## 3.2. Pipeline
1. Quality control using `MRIQC` tool
2. Neck removal with FSL `robustfov` tool
3. N4 non-uniformity correction using ANTs `N4BiasFieldCorrection` tool
4. Run the Freesurfer 6.0 pipelines
5. Freesurfer Qc → manual assessment with tkmedit for biggest issues: adding control points, white matter filling, editing the pial 
6. Extract cortical thickness measures of fronto-parietal ROIs (to be defined: dLPC, ACC, IPL, IFG?)
      For cortical ROIs measures we'll be using the Desikan-Killiany atlas and subcortical ROIs (if any): Freesurfer aseg atlas
7. Extract Ventricular and total brain volume meausures
8. Fitting of the overlapping curves and computing distances 

Research questions:
1. Are DLBS and ADNI normal controls curves overlapping? 
2. Are the normal curves and the HAB curve any different? Can we use the latter to predict later cognitive impairment?
3. Can we predict the degree of cognitive impairment(pre-clinical, EMCI, MCI, LMCI, AD) based on the distance of the subjects from the normal curves? 


# 4. Statistical Analysis
## 4.1. Intra-group analysis
* **Training Set**
  1. Correlation 1: Cortical Thickness ROIs x Age
  2. Correlation 2: Behavioral Performance in the Cambridge Neuropsychological Test Automated Battery x Age
  3. Brain-Behavior correlation: Interaction between age x cortical thickness ROIs x performance in the Cambridge Neuropsychological Test Automated Battery
* **Replication Set**
  1. Correlation 1: Cortical Thickness ROIs x Age
  2. Correlation 2: Behavioral Performance in the Trail Making Test x Age
  3. Brain-Behavior correlation: Interaction age x thickness ROIs x performance TMT
* **Pre Clinical Set**
  1. Correlation 1: Cortical Thickness ROIs x Age
  2. Correlation 2: beta amyloid x Age → high beta amyloid subjects vs low beta amyloid subjects
  3. Beta amyloid values x thickness ROIs x age
  4. Behavioral Performance in Trail Making Test x age 
  5. Behavioral Performance in TMT x cortical thickness
  6. Subj with high/low beta amyloid: cortical thickness x Behavioral Perfomance in Trail Making Test x age
* **Test Set**
  1. Extract cortical thickness measures of ROIs
  2. Histogram 1: Cortical Thickness ROIs in each group
  3. Histogram 2: Behavioral Performance in the Trail Making Test x each group
  4. Correlation: Thickness ROIs x Performance in each Group
  
## 4.2. Infra-group analysis
We'll be performing t-tests between:
1. DLBS and ADNI normal controls
2. DLBS/ADNI normal controls and HAB
3. DLBS/ADNI normal controls and EMCI
4. DLBS/ADNI normal controls and MCI
5. DLBS/ADNI normal controls and LMCI
6. DLBS/ADNI normal controls and AD

We'll be performing ANOVAs between:
1. EMCI-MCI-LMCI-AD
2. normal curve (DLBS/ADNI controls) - pre-clinical curve (HAB) - clinical curve (that includes EMCI,MCI,LMCI and AD)


# 5. Code Development 
Freesurfer recon-all will be run using Python language (nipype). 
Our statistical analysis will be performed using "rpy2" package in Python.
