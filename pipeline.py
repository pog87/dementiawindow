
# coding: utf-8

# In[1]:


import nipype

from nipype.interfaces import fsl
from nipype.interfaces import ants
from nipype.interfaces import freesurfer
from os.path import abspath


# In[2]:


base_dir=abspath('examples/')


# In[3]:


CORES=4
TASKS=2


# In[4]:


grabber = nipype.Node(interface=nipype.DataGrabber(infields=['arg'],outfields=['out_file']), name='grabber')      
grabber.inputs.base_directory = base_dir
grabber.inputs.sort_filelist = False
grabber.inputs.template = '*/%s.nii.gz'
grabber.inputs.arg = 't1w'


# In[5]:


#a=grabber.run()
#a.outputs


# In[6]:


sink = nipype.Node(interface=nipype.DataSink(),name='sink')
sink.inputs.base_directory = base_dir
# this is to force sink to use the inputs dirs 
# credits: https://gist.github.com/lebedov/9294b8b37640db911bfc987aca49f239
#sink.inputs.regexp_substitutions = [('_\w+\d+', '')]

print sink.interface.inputs
a=sink.run()
# In[7]:


# Neck removal by FSL robustfov
neck_remove=nipype.MapNode(interface=fsl.RobustFOV(), name='neck_remove', iterfield=['in_file'])
neck_remove.inputs.out_roi="t1w_fov.nii.gz"


# In[37]:


# Field Inhomogenity estimation (if any) and removal by ANTs N4BiasFieldCorrection
N4_FC=nipype.MapNode(interface=ants.N4BiasFieldCorrection(), name="N4_FC", iterfield=['input_image'])
N4_FC.inputs.dimension = 3
N4_FC.inputs.output_image="t1w_fov_N4.nii.gz"
N4_FC.inputs.num_threads=CORES


# In[10]:


workflow = nipype.Workflow('workflow')
#workflow.connect([(grabber, neck_remove, [('out_file', 'in_file')]),
#                  (neck_remove, N4_FC, [('out_roi', 'input_image')]),
#                  (N4_FC, sink, [('output_image', 'preproc.@in_file')]),
#                 ])
workflow.connect([(grabber, neck_remove, [('out_file', 'in_file')]),
                  (neck_remove, sink, [('out_roi', '@in_file')]),
                 ])


# In[11]:


#workflow.run()
workflow.run('MultiProc', plugin_args={'n_procs': TASKS})


# In[ ]:




grabber = nipype.Node(interface=nipype.DataGrabber( outfields=['out_file']), name='grabber')                      
grabber.inputs.base_directory = base_dir
grabber.inputs.sort_filelist = True
grabber.inputs.template = '*/t1w.nii.gz' #all folders, all files named t1w.nii.gz# DataGrabber asks you how to take input files,
# DataSink where/how to save final output file
#  everything else is saved in a temp directory.

grabber = nipype.Node(interface=nipype.DataGrabber( outfields=['out_file']), name='grabber')                      
grabber.inputs.base_directory = base_dir
grabber.inputs.sort_filelist = True
grabber.inputs.template = '*/t1w.nii.gz' #all folders, all files named t1w.nii.gz