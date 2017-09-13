# Description
We'll be analyzing cortical thickness values of normal, pre-clinical and clinical populations in pre-determined fronto-parietal ROIs as a function of age, beta amyloid values(for the HBA) and behavioral measures (for the datasets that have made them available).

As most of the literature focuses on memory decline in healthy older individuals and Alzheimer's patients, we aim at extending the current knowledge of cognitive decline to the executive functions' field, by correlating cortical thickness measures with behavioral performance on executive functions' tasks that are similar across the datasets.

We'll be using the DLBS dataset as a training set and the ADNI healthy control subsample as a replication set. The HAB dataset will be considered as an explorative pre-clinical set before actually testing the distance of MCI and AD patients from the normal curve.

In this way, by performing this analysis on the full spectrum, we will be able to trace a continuous trajectory between the normal, pre-clinical and clinical population as far as cognitive control decline is concerned.

# Theoretical Motivation
# Research Design

1. Run the Freesurfer pipelines for the NKI dataset just for those 341 subjects. I can share with you the scripts we use in our lab.
2. Extract the thickness measures of the Region of Interest we decide from the NKI
3. Request access to the Harvard dataset and extract those measures for this one too.
4. Run the Freesurfer pipeline for the ADNI as well, well for the subsamples that have not been run yet. In this case having to go back and manually edit each single brain might be really time consuming. I suggest to just look for major issues (the same goes for the NKI dataset).
5. Extract the thickness values of our ROIs for the ADNI too.
6. Perform basic correlations: 
a. Thickness in those ROIS-age
b. Behavior in the tasks we pick-age
c. Thickness in those ROIs-Behavior in those tasks we pick
7. END!!!


# Statistical Analysis
# Code Development 
