
# coding: utf-8

# In[1]:


import nipype

from nipype.interfaces import fsl
from nipype.interfaces import ants
from nipype.interfaces import freesurfer
import os


# In[2]:


base_dir=os.path.abspath('examples/')
subject_list =sorted(next(os.walk(base_dir))[1])


# In[3]:


CORES=4
TASKS=2


# In[4]:


grabber = nipype.Node(interface=nipype.DataGrabber(infields=['arg'],outfields=['out_file']), name='grabber')      
grabber.inputs.base_directory = base_dir
grabber.inputs.sort_filelist = True
grabber.inputs.template = '*/%s.nii.gz'
grabber.inputs.arg = 't1w'


# In[5]:


sink = nipype.Node(interface=nipype.DataSink(),name='sink')
sink.inputs.base_directory = base_dir
substitutions=[]
for i in range(len(subject_list)):
    substitutions+= [("_neck_remove"+str(i), subject_list[i])]
substitutions+= [("subject_id_", "")]
    
sink.inputs.substitutions =substitutions 


# In[6]:


sink2 = nipype.Node(interface=nipype.DataSink(),name='sink2')
sink2.inputs.base_directory = base_dir
substitutions=[]
for i in range(len(subject_list)):
    substitutions+= [("_N4_FC"+str(i), subject_list[i])]
substitutions+= [("subject_id_", "")]
    
sink2.inputs.substitutions =substitutions 


# In[7]:


# Neck removal by FSL robustfov
neck_remove=nipype.MapNode(interface=fsl.RobustFOV(), name='neck_remove', iterfield=['in_file'])
neck_remove.inputs.out_roi="t1w_fov.nii.gz"


# In[8]:


# Field Inhomogenity estimation (if any) and removal by ANTs N4BiasFieldCorrection
N4_FC=nipype.MapNode(interface=ants.N4BiasFieldCorrection(), name="N4_FC", iterfield=['input_image'])
N4_FC.inputs.dimension = 3
N4_FC.inputs.output_image="t1w_fov_N4.nii.gz"
N4_FC.inputs.num_threads=CORES


# In[9]:


workflow = nipype.Workflow('workflow')
workflow.connect([(grabber, neck_remove, [('out_file', 'in_file')]),
                  (neck_remove, sink, [('out_roi', '@in_file')]),
                  (neck_remove, N4_FC, [('out_roi', 'input_image')]),
                  (N4_FC, sink2, [('output_image', '@in_file')])
                 ])


# In[10]:


#workflow.run()
workflow.run('MultiProc', plugin_args={'n_procs': TASKS})


# In[ ]:




