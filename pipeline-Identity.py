
# coding: utf-8

# In[1]:


import nipype

from nipype.interfaces import fsl
from nipype.interfaces import ants
from nipype.interfaces import freesurfer
import os


# In[2]:


def pathfinder(subject, foldername, filename):
    from os.path import join as opj
    struct_path = opj(foldername, subject, filename)
    return struct_path


# In[3]:


data_dir = os.path.abspath('examples/')
subject_list =sorted(next(os.walk(data_dir))[1])
T1_identifier = 't1w.nii.gz'


# In[4]:


subject_list


# In[5]:


CORES=4
TASKS=2


# In[6]:


infosource = nipype.Node(nipype.IdentityInterface(fields=['subject_id']),name="infosource")
infosource.iterables = ('subject_id', subject_list)


# In[7]:


sink = nipype.Node(interface=nipype.DataSink(),name='sink')
sink.inputs.base_directory = data_dir

substitutions=[]
for i in range(len(subject_list)):
    substitutions+= [("_neck_remove"+str(i),"")]
substitutions+= [("_subject_id_", "")]
sink.inputs.substitutions =substitutions 


# In[8]:


sink2 = nipype.Node(interface=nipype.DataSink(),name='sink2')
sink.inputs.base_directory = data_dir

substitutions=[]
for i in range(len(subject_list)):
    substitutions+= [("_N4_FC"+str(i), "")]
substitutions+= [("_subject_id_", "")]
sink.inputs.substitutions =substitutions 


# In[9]:


# Neck removal by FSL robustfov
neck_remove=nipype.MapNode(interface=fsl.RobustFOV(), name='neck_remove', iterfield=['in_file'])
neck_remove.inputs.out_roi="t1w_fov.nii.gz"


# In[10]:


# Field Inhomogenity estimation (if any) and removal by ANTs N4BiasFieldCorrection
N4_FC=nipype.MapNode(interface=ants.N4BiasFieldCorrection(), name="N4_FC", iterfield=['input_image'])
N4_FC.inputs.dimension = 3
N4_FC.inputs.output_image="t1w_fov_N4.nii.gz"
N4_FC.inputs.num_threads=CORES


# In[11]:


workflow = nipype.Workflow('workflow')
workflow.connect([(infosource, neck_remove, [(('subject_id', pathfinder,data_dir, T1_identifier), 'in_file')]),
                  (neck_remove, sink, [('out_roi', '@in_file')]),
                  (neck_remove, N4_FC, [('out_roi', 'input_image')]),
                  (N4_FC, sink2, [('output_image', '@in_file')])
                 ])


# In[12]:


#workflow.run()
workflow.run('MultiProc', plugin_args={'n_procs': TASKS})


# In[ ]:




