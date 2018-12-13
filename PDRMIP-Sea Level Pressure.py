#!/usr/bin/env python
# coding: utf-8

# Loading in PDRMIP outputs - sea level pressure, geopotential height, horizontal and vertical winde 
# Data Anaylsis stemming from these outputs.

# In[24]:


# To import both packages:

import cf, cfplot as cfp
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# you also want these lines so that the plots will open in matplotlib's viewer

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# Importing all Base Case models, that output a Sea Level Pressure Variable

# In[3]:


# To read a NetCDF with one field:
#f = cf.read_field("netCDF_filename")

# To read a NetCDF with one field:
# TEMPLATE AND NOMENCLATURE TO BE USED FOR FUTURE READING

#model_experiment_variable

#canesm2_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CanESM2**base*.nc")
#mpiesm_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*MPI-ESM**base*.nc")
#noresm1_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*NorESM1**base*.nc")
#cesm1cam4_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM4**base*.nc")
#cesm1cam5_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM5**base*.nc")
#sprintars_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*SPRINTARS**base*.nc")
#hadgem2_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM2**base*.nc")
#hadgem3_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM3**base*.nc")
#giss_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*GISS**base*.nc")
#ipsl_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*IPSL**base*.nc")
#echam_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*ECHAM**base*.nc")


# In[4]:


# To read a NetCDF with one field:
#f = cf.read_field("netCDF_filename")

# To read a NetCDF with one field:
# TEMPLATE AND NOMENCLATURE TO BE USED FOR FUTURE READING
canesm2_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CanESM2**base*.nc")
mpiesm_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*MPI-ESM**base*.nc")
noresm1_b_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*NorESM1**base*.nc")[0]
cesm1cam4_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM4**base*.nc")
cesm1cam5_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM5**base*.nc")
sprintars_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*SPRINTARS**base*.nc")
hadgem2_b_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM2**base*.nc")[0]
#hadgem3_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM3**base*.nc")
giss_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*GISS**base*.nc")
ipsl_b_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*IPSL**base*.nc")[1]
echam_b_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*ECHAM**base*.nc")

echam_b_psl.dump()


# Importing all BCx10 models, that output Sea Level Pressure Variable

# In[5]:


canesm2_bc10_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CanESM2**bcx10_*.nc")
#mpiesm_bc10_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*MPI-ESM**bcx10_*.nc")
noresm1_bc10_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*NorESM1**bcx10_*.nc")[0]
cesm1cam4_bc10_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM4**bcx10_*.nc")
cesm1cam5_bc10_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM5**bcx10_*.nc")
sprintars_bc10_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*SPRINTARS**bcx10_*.nc")
hadgem2_bc10_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM2**bcx10_*.nc")[0]
#hadgem3_bc10_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM3**bcx10_*.nc")
giss_bc10_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*GISS**bcx10_*.nc")
ipsl_bc10_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*IPSL**bcx10_*.nc")[1]
echam_bc10_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*ECHAM**bcx10_*.nc")


# Importing all sulx5 models, that output Sea Level Pressure Variable

# In[6]:


canesm2_s5_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CanESM2**sulx5*.nc")
#mpiesm_s5_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*MPI-ESM**sulx5*.nc")
noresm1_s5_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*NorESM1**sulx5*.nc")[0]
cesm1cam4_s5_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM4**sulx5*.nc")
cesm1cam5_s5_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM5**sulx5*.nc")
sprintars_s5_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*SPRINTARS**sulx5*.nc")
hadgem2_s5_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM2**sulx5*.nc")[0]
#hadgem3_s5_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM3**sulx5*.nc")
giss_s5_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*GISS**sulx5*.nc")
ipsl_s5_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*IPSL**sulx5*.nc")[1]
#echam_s5_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*ECHAM**sulx5*.nc")


# Importing all bcx10asia models, that output Sea Level Pressure Variable

# In[7]:


#canesm2_bc10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CanESM2**bcx10asia*.nc")
#mpiesm_bc10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*MPI-ESM**bcx10asia*.nc")
noresm1_bc10a_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*NorESM1**bcx10asia*.nc")[0]
#cesm1cam4_bc10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM4**bcx10asia*.nc")
cesm1cam5_bc10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM5**bcx10asia*.nc")
sprintars_bc10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*SPRINTARS**bcx10asia*.nc")
#hadgem2_bc10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM2**bcx10asia*.nc")[0]
#hadgem3_bc10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM3**bcx10asia*.nc")
giss_bc10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*GISS**bcx10asia*.nc")
ipsl_bc10a_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*IPSL**bcx10asia*.nc")[1]
#echam_bc10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*ECHAM**bcx10asia*.nc")


# Importing all sulx10asia models, that output Sea Level Pressure Variable

# In[8]:


#canesm2_s10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CanESM2**sulx10asia*.nc")
#mpiesm_s10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*MPI-ESM**sulx10asia*.nc")
noresm1_s10a_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*NorESM1**sulx10asia*.nc")[0]
cesm1cam4_s10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM4**sulx10asia*.nc")
cesm1cam5_s10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM5**sulx10asia*.nc")
sprintars_s10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*SPRINTARS**sulx10asia*.nc")
#hadgem2_s10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM2**sulx10asia*.nc")[0]
#hadgem3_s10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM3**sulx10asia*.nc")
giss_s10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*GISS**sulx10asia*.nc")
ipsl_s10a_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*IPSL**sulx10asia*.nc")[1]
#echam_s10a_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*ECHAM**sulx10asia*.nc")


# Importing all sulx10eur models, that output Sea Level Pressure Variable

# In[9]:


#canesm2_s10e_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CanESM2**sulx10eur*.nc")
#mpiesm_s10e_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*MPI-ESM**sulx10eur*.nc")
noresm1_s10e_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*NorESM1**sulx10eur*.nc")[0]
cesm1cam4_s10e_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM4**sulx10eur*.nc")
cesm1cam5_s10e_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM5**sulx10eur*.nc")
sprintars_s10e_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*SPRINTARS**sulx10eur*.nc")
#hadgem2_s10e_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM2**sulx10eur*.nc")[0]
#hadgem3_s10e_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM3**sulx10eur*.nc")
giss_s10e_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*GISS**sulx10eur*.nc")
ipsl_s10e_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*IPSL**sulx10eur*.nc")[1]
#echam_s10e_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*ECHAM**sulx10eur*.nc")


# Importing all Sulred models, that output Sea Level Pressure Variable

# In[10]:


#canesm2_sr_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CanESM2**sulred*.nc")
#mpiesm_sr_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*MPI-ESM**sulred*.nc")
#noresm1_sr_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*NorESM1**sulred*.nc")[0]
#cesm1cam4_sr_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM4**sulred*.nc")
#cesm1cam5_sr_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM5**sulred*.nc")
sprintars_sr_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*SPRINTARS**sulred*.nc")
#hadgem2_sr_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM2**sulred*.nc")[0]
#hadgem3_sr_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM3**sulred*.nc")
#giss_sr_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*GISS**sulred*.nc")
#ipsl_sr_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*IPSL**sulred*.nc")[1]
#echam_sr_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*ECHAM**sulred*.nc")


# Importing all Sulasiared models, that output Sea Level Pressure Variable

# In[11]:


#canesm2_sar_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CanESM2**sulasiared*.nc")
#mpiesm_sar_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*MPI-ESM**sulasiared*.nc")
#noresm1_sar_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*NorESM1**sulasiared*.nc")[0]
#cesm1cam4_sar_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM4**sulasiared*.nc")
#cesm1cam5_sar_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*CESM1-CAM5**sulasiared*.nc")
sprintars_sar_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*SPRINTARS**sulasiared*.nc")
#hadgem2_sar_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM2**sulasiared*.nc")[0]
#hadgem3_sar_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*HadGEM3**sulasiared*.nc")
#giss_sar_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*GISS**sulasiared*.nc")
#ipsl_sar_psl = cf.read("/nfs/annie/eewjd/PDRMIP/slp/*IPSL**sulasiared*.nc")[1]
#echam_sar_psl = cf.read_field("/nfs/annie/eewjd/PDRMIP/slp/*ECHAM**sulasiared*.nc")


# Given the run length for the coupled experiments is 100 years, we will concentrate on final 50 years.
# At the moment this is assumed to be when the model has reached equilibrium - need to test this!

# BASE CASE

# In[12]:


fin50_canesm2_b_psl = canesm2_b_psl.subspace('time'>600)
fin50_mpiesm_b_psl = mpiesm_b_psl.subspace('time'>600)
fin50_noresm1_b_psl = noresm1_b_psl.subspace('time'>600)
fin50_cesm1cam4_b_psl = cesm1cam4_b_psl.subspace('time'>600) 
fin50_cesm1cam5_b_psl = cesm1cam5_b_psl.subspace('time'>600) 
fin50_sprintars_b_psl = sprintars_b_psl.subspace('time'>600) 
fin50_hadgem2_b_psl = hadgem2_b_psl.subspace('time'>600)
#fin50_hadgem3_b_psl = fin50_hadgem3_b_psl.subspace('time'>600)
fin50_giss_b_psl = giss_b_psl.subspace('time'>600) 
fin50_ipsl_b_psl = ipsl_b_psl.subspace('time'>600) 
fin50_echam_b_psl = echam_b_psl.subspace('time'>600) 


# BCx10

# In[13]:


fin50_canesm2_bc10_psl = canesm2_bc10_psl.subspace('time'>600)
#fin50_mpiesm_bc10_psl = mpiesm_bc10_psl.subspace('time'>600)
fin50_noresm1_bc10_psl = noresm1_bc10_psl.subspace('time'>600)
fin50_cesm1cam4_bc10_psl = cesm1cam4_bc10_psl.subspace('time'>600)
fin50_cesm1cam5_bc10_psl = cesm1cam5_bc10_psl.subspace('time'>600)
fin50_sprintars_bc10_psl = sprintars_bc10_psl.subspace('time'>600)
fin50_hadgem2_bc10_psl = hadgem2_bc10_psl.subspace('time'>600)
#fin50_hadgem3_bc10_psl = hadgem3_bc10_psl.subspace('time'>600)
fin50_giss_bc10_psl = giss_bc10_psl.subspace('time'>600)
fin50_ipsl_bc10_psl = ipsl_bc10_psl.subspace('time'>600)
fin50_echam_bc10_psl = echam_bc10_psl.subspace('time'>600)


# Sulx5

# In[14]:


fin50_canesm2_s5_psl = canesm2_s5_psl.subspace('time'>600)
#fin50_mpiesm_s5_psl = mpiesm_s5_psl.subspace('time'>600)
fin50_noresm1_s5_psl = noresm1_s5_psl.subspace('time'>600)
fin50_cesm1cam4_s5_psl = cesm1cam4_s5_psl.subspace('time'>600)
fin50_cesm1cam5_s5_psl = cesm1cam5_s5_psl.subspace('time'>600)
fin50_sprintars_s5_psl = sprintars_s5_psl.subspace('time'>600)
fin50_hadgem2_s5_psl = hadgem2_s5_psl.subspace('time'>600)
#fin50_hadgem3_s5_psl = fin50_hadgem3_s5_psl.subspace('time'>600)
fin50_giss_s5_psl = giss_s5_psl.subspace('time'>600)
fin50_ipsl_s5_psl = ipsl_s5_psl.subspace('time'>600)
#fin50_echam_s5_psl = echam_s5_psl.subspace('time'>600)


# bcx10asia

# In[15]:


#fin50_canesm2_bc10a_psl = canesm2_bc10a_psl.subspace('time'>600)
#fin50_mpiesm_bc10a_psl = mpiesm_bc10a_psl.subspace('time'>600)
fin50_noresm1_bc10a_psl = noresm1_bc10a_psl.subspace('time'>600)
#fin50_cesm1cam4_bc10a_psl = cesm1cam4_bc10a_psl.subspace('time'>600)
fin50_cesm1cam5_bc10a_psl = cesm1cam5_bc10a_psl.subspace('time'>600)
fin50_sprintars_bc10a_psl = sprintars_bc10a_psl.subspace('time'>600)
#fin50_hadgem2_bc10a_psl = hadgem2_bc10a_psl.subspace('time'>600)
#fin50_hadgem3_bc10a_psl = hadgem3_bc10a_psl.subspace('time'>600)
fin50_giss_bc10a_psl = giss_bc10a_psl.subspace('time'>600)
fin50_ipsl_bc10a_psl = ipsl_bc10a_psl.subspace('time'>600)
#fin50_echam_bc10a_psl = echam_bc10a_psl.subspace('time'>600)


# sulx10asia

# In[16]:


#fin50_canesm2_s10a_psl = canesm2_s10a_psl.subspace('time'>600)
#fin50_mpiesm_s10a_psl = mpiesm_s10a_psl.subspace('time'>600)
fin50_noresm1_s10a_psl = noresm1_s10a_psl.subspace('time'>600)
fin50_cesm1cam4_s10a_psl = cesm1cam4_s10a_psl.subspace('time'>600)
fin50_cesm1cam5_s10a_psl = cesm1cam5_s10a_psl.subspace('time'>600)
fin50_sprintars_s10a_psl = sprintars_s10a_psl.subspace('time'>600)
#fin50_hadgem2_s10a_psl = hadgem2_s10a_psl.subspace('time'>600)
#fin50_hadgem3_s10a_psl = hadgem3_s10a_psl.subspace('time'>600)
fin50_giss_s10a_psl = giss_s10a_psl.subspace('time'>600)
fin50_ipsl_s10a_psl = ipsl_s10a_psl.subspace('time'>600)
#fin50_echam_s10a_psl = echam_s10a_psl.subspace('time'>600)


# sulx10eur

# In[17]:


#fin50_canesm2_s10e_psl = canesm2_s10e_psl.subspace('time'>600)
#fin50_mpiesm_s10e_psl = mpiesm_s10e_psl.subspace('time'>600)
fin50_noresm1_s10e_psl = noresm1_s10e_psl.subspace('time'>600)
fin50_cesm1cam4_s10e_psl = cesm1cam4_s10e_psl.subspace('time'>600)
fin50_cesm1cam5_s10e_psl = cesm1cam5_s10e_psl.subspace('time'>600)
fin50_sprintars_s10e_psl = sprintars_s10e_psl.subspace('time'>600)
#fin50_hadgem2_s10e_psl = hadgem2_s10e_psl.subspace('time'>600)
#fin50_hadgem3_s10e_psl = hadgem3_s10e_psl.subspace('time'>600)
fin50_giss_s10e_psl = giss_s10e_psl.subspace('time'>600)
fin50_ipsl_s10e_psl = ipsl_s10e_psl.subspace('time'>600)
#fin50_echam_s10e_psl = echam_s10e_psl.subspace('time'>600)


# sulred

# In[18]:


#fin50_canesm2_sr_psl = canesm2_sr_psl.subspace('time'>600)
#fin50_mpiesm_sr_psl = mpiesm_sr_psl.subspace('time'>600)
#fin50_noresm1_sr_psl = noresm1_sr_psl.subspace('time'>600)
#fin50_cesm1cam4_sr_psl = cesm1cam4_sr_psl.subspace('time'>600)
#fin50_cesm1cam5_sr_psl = cesm1cam5_sr_psl.subspace('time'>600)
fin50_sprintars_sr_psl = sprintars_sr_psl.subspace('time'>600)
#fin50_hadgem2_sr_psl = hadgem2_sr_psl.subspace('time'>600)
#fin50_hadgem3_sr_psl = hadgem3_sr_psl.subspace('time'>600)
#fin50_giss_sr_psl = giss_sr_psl.subspace('time'>600)
#fin50_ipsl_sr_psl = ipsl_sr_psl.subspace('time'>600)
#fin50_echam_sr_psl = echam_sr_psl.subspace('time'>600)


# sulasiared

# In[19]:


#fin50_canesm2_sar_psl = canesm2_sar_psl.subspace('time'>600)
#fin50_mpiesm_sar_psl = mpiesm_sar_psl.subspace('time'>600)
#fin50_noresm1_sar_psl = noresm1_sar_psl.subspace('time'>600)
#fin50_cesm1cam4_sar_psl = cesm1cam4_sar_psl.subspace('time'>600)
#fin50_cesm1cam5_sar_psl = cesm1cam5_sar_psl.subspace('time'>600)
fin50_sprintars_sar_psl = sprintars_sar_psl.subspace('time'>600)
#fin50_hadgem2_sar_psl = hadgem2_sar_psl.subspace('time'>600)
#fin50_hadgem3_sar_psl = hadgem3_sar_psl.subspace('time'>600)
#fin50_giss_sar_psl = giss_sar_psl.subspace('time'>600)
#fin50_ipsl_sar_psl = ipsl_sar_psl.subspace('time'>600)
#fin50_echam_sar_psl = echam_sar_psl.subspace('time'>600)


# Collapsing the second 50 year dataset to find a time average for each model.
# //Subsequently a multimodel mean

# Base

# In[30]:




#tm = time mean

tm_fin50_canesm2_b_psl = fin50_canesm2_b_psl.collapse('mean','time')
tm_fin50_mpiesm_b_psl = fin50_mpiesm_b_psl.collapse('mean','time')
tm_fin50_noresm1_b_psl = fin50_noresm1_b_psl.collapse('mean','long_name:Time')
tm_fin50_cesm1cam4_b_psl = fin50_cesm1cam4_b_psl.collapse('mean','time') 
tm_fin50_cesm1cam5_b_psl = fin50_cesm1cam5_b_psl.collapse('mean','time') 
tm_fin50_sprintars_b_psl = fin50_sprintars_b_psl.collapse('mean','time') 
tm_fin50_hadgem2_b_psl = fin50_hadgem2_b_psl.collapse('mean','long_name:t')
#tm_fin50_hadgem3_b_psl = fin50_hadgem3_b_psl.collapse('mean','time')
tm_fin50_giss_b_psl = fin50_giss_b_psl.collapse('mean','time') 
tm_fin50_ipsl_b_psl = fin50_ipsl_b_psl.collapse('mean','time') 
tm_fin50_echam_b_psl = fin50_echam_b_psl.collapse('mean','time') 

#regridding tm_fin50_canesm2_b_psl to have 96 lats like the other models

tm_fin50_canesm2_b_psl_rg = tm_fin50_canesm2_b_psl.regrids(tm_fin50_mpiesm_b_psl, method = 'bilinear')


#mmm = multi-model-mean

#mmm_b_psl = (tm_fin50_canesm2_b_psl + tm_fin50_mpiesm_b_psl + tm_fin50_noresm1_b_psl + tm_fin50_cesm1cam4_b_psl + tm_fin50_cesm1cam5_b_psl + tm_fin50_sprintars_b_psl + tm_fin50_hadgem2_b_psl + tm_fin50_hadgem3_b_psl + tm_fin50_giss_b_psl + tm_fin50_ipsl_b_psl + tm_fin50_echam_b_psl) / 11

#mmm_b_psl = (tm_fin50_noresm1_b_psl + tm_fin50_mpiesm_b_psl)/2









# In[110]:


#plotting on map

cfp.mapset(lonmin=-360, lonmax=0, latmin=-70, latmax=90)
cfp.con(tm_fin50_canesm2_b_psl, blockfill=True, lines=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[35]:


pdrmip_dic = {'model':['canesm2_','mpiesm_','noresm1_','cesm1cam4_','cesm1cam5_','sprintars_','hadgem2_','hadgem3_','giss_','ipsl_','echam_'],
              'exp':['b_','bc_','s_','bc10a_','s10a_','s10e_','sr_','sar_'],'var':['psl']}


for key,value in pdrmip_dic.items():
 print(pdrmip_dic['model'])

#i = i.collapse('mean', 'time')

#arraysList = []
#for i in range(0,3):
#    arraysList.append([1,2,3])

#print arraysList
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
#print arraysList[1]
# [1, 2, 3]



#for items in t:
#    fin50_sprintars_sar_psl = final_50.collapse('mean', 'time')


# In[14]:


cfp.mapset(lonmin=-360, lonmax=0, latmin=-70, latmax=90)
cfp.con(test, blockfill=True, lines=False)


# In[1]:


fin_50_cesm1cam4_s10a_psl = cesm1cam4_s10a_psl.subspace('time'>600)


#canesm2_b_psl.dump() 
#mpiesm_b_psl 
#noresm1_b_psl 
#cesm1cam4_b_psl 
#cesm1cam5_b_psl 
#sprintars_b_psl 
#hadgem2_b_psl
#giss_b_psl 
#ipsl_b_psl 
#echam_b_psl 


# In[4]:


#Taking the final 50 years (years 51-100) of ALL output variables
final_50 = canesm2_b_psl.subspace('time'>600)

canesm2_b_psl 
mpiesm_b_psl 
noresm1_b_psl 
cesm1cam4_b_psl 
cesm1cam5_b_psl 
sprintars_b_psl 
hadgem2_b_psl
giss_b_psl 
ipsl_b_psl 
echam_b_psl 




# In[ ]:





# In[5]:


#finding the mean over final 50 year time period 
whole_tm = final_50.collapse('mean', 'time')


# In[68]:


cesm1cam5_s10a_psl.dump()


# In[6]:


#plotting on map

cfp.mapset(lonmin=-360, lonmax=0, latmin=-70, latmax=90)
cfp.con(whole_tm, blockfill=True, lines=False)


# In[9]:


#finding SLP anomaly, given the global mean for base case for years 51-100

global_mean_cccma = 101138.920

cccma_amon_anom = whole_tm - global_mean_cccma

cfp.mapset(lonmin=-360, lonmax=0, latmin=-90, latmax=90)
cfp.con(cccma_amon_anom, blockfill=True, lines=False)


# In[10]:


# Load in all Sulx5 Experiments 

# To read a NetCDF with one field:
#f = cf.read_field("netCDF_filename")

#Coupled Experiments
cccma_amon_c5sul = cf.read_field("/nfs/a65/eetbr/PDRMIP/CCCma_Amon_PDRMIP/abrupt5xSul/atmos/psl/r1i1p1/psl_Amon_CanESM2_pdrmip-sul_r1i1p1_185001-194912.nc")
nor_esm1_c5sul = cf.read("/nfs/a65/eetbr/PDRMIP/NorESM_Amon_PDRMIP/abrupt5xSul/psl_Amon_NorESM1_pdrmip-sulx5_coupled_200501-210512.nc")
cesm1_cam4_c5sul = cf.read_field("/nfs/a65/eetbr/PDRMIP/CESM1_CAM4_Amon_PDRMIP/abrupt5xSul/atmos/psl/r1i1p1/psl_Amon_CESM1_pdrmip-sul_r1i1p1_001101-012012.nc")
cesm1_cam5_c5sul = cf.read_field("/nfs/a65/eetbr/PDRMIP/CESM1_CAM5_Amon_PDRMIP/abrupt5xSul/psl/psl_Amon_NCAR-CESM1-CAM5_pdrmip-sulx5_coupled_200601-213712.nc")
sprintars_c5sul = cf.read_field("/nfs/a65/eetbr/PDRMIP/SPRINTARS_Amon_PDRMIP/abrupt5xSul/psl_MIROC-SPRINTARS_PDRMIP_Sul_200101-210012.nc")
hadgem2_c5sul_a = cf.read_field("/nfs/a65/eetbr/PDRMIP/HadGEM2_Amon_PDRMIP/abrupt5xSul/psl/psl_Amon_HadGEM2_abrupt5xSul_r1i1p1_185912-190911.nc")
hadgem2_c5sul_b = cf.read_field("/nfs/a65/eetbr/PDRMIP/HadGEM2_Amon_PDRMIP/abrupt5xSul/psl/psl_Amon_HadGEM2_abrupt5xSul_r1i1p1_190912-195911.nc")
giss_c5sul = cf.read_field("/nfs/a65/eetbr/PDRMIP/GISS_Amon_PDRMIP/abrupt5xSul/monthly/psl/psl_BOGUS-PDRMIP-monthly_GISS-E2-R_PDRMIP_SUL_OCEAN_r1i1p1_*")

#no SLP for Hadgem3
#IPSL-CM5A cant find SLP variable in file structure
#ECHAM no 5xsul for coupled run
#no 5xsul for MPI_ESM


# In[11]:


#cccma_amon_c5sul.dump()


# In[12]:


#taking the final 50 years (years 51-100)
final_50_c5sul = cccma_amon_c5sul.subspace('time'>600)


# In[13]:


#finding the mean over final 50 year time period 
whole_tm_c5sul = final_50_c5sul.collapse('mean', 'time')


# In[14]:


#plotting on map

cfp.mapset(lonmin=-360, lonmax=-0, latmin=-90, latmax=90)
cfp.con(whole_tm_c5sul, blockfill=True, lines=False)


# In[15]:


#determining global mean for 5x sulphur global step change increase
global_mean_5xsul = whole_tm_c5sul.collapse('X: Y: mean', weights = 'area')
global_mean_5xsul = int(global_mean_5xsul.array[0])


# In[16]:


#finding SLP anomaly, given the global mean for base case for years 51-100

cccma_amon_anom_c5sul = whole_tm_c5sul - global_mean_5xsul
1458709
cfp.mapset(lonmin=-360, lonmax=0, latmin=-90, latmax=90)
cfp.con(cccma_amon_anom_c5sul, blockfill=True, lines=False)


# In[17]:


#difference between base case and 5xsul global experiments

diff_base_5Sul = whole_tm_c5sul - whole_tm

cfp.mapset(lonmin=-360, lonmax=0, latmin=-90, latmax=90)
cfp.con(diff_base_5Sul, blockfill=True, lines=False)


# In[ ]:





# In[18]:


# Load in all Sulx10asia Experiments 

#Coupled Experiments

#nor_esm1_a10sul = cf.read("/nfs/a65/eetbr/PDRMIP/NorESM_Amon_PDRMIP/abrupt5xSul/psl_Amon_NorESM1_pdrmip-sulx5_coupled_200501-210512.nc")
#can't find SLP data output on our servers
#cesm1_cam4_a10sul = cf.read_field("/nfs/a65/eetbr/PDRMIP/CESM1_CAM4_Amon_PDRMIP/abrupt5xSul/atmos/psl/r1i1p1/psl_Amon_CESM1_pdrmip-sul_r1i1p1_001101-012012.nc")
#can't find SLP data output on our servers
cesm1_cam5_a10sul = cf.read_field("/nfs/a65/eetbr/PDRMIP/CESM1_CAM5_Amon_PDRMIP/abrupt5xSul/psl/psl_Amon_NCAR-CESM1-CAM5_pdrmip-sulx5_coupled_200601-213712.nc")
sprintars_a10sul = cf.read_field("/nfs/a65/eetbr/PDRMIP/SPRINTARS_Amon_PDRMIP/abrupt5xSul/psl_MIROC-SPRINTARS_PDRMIP_Sul_200101-210012.nc")
giss_a10sul = cf.read_field("/nfs/a65/eetbr/PDRMIP/GISS_Amon_PDRMIP/abrupt5xSul/monthly/psl/psl_BOGUS-PDRMIP-monthly_GISS-E2-R_PDRMIP_SUL_OCEAN_r1i1p1_*")

#no SLP for Hadgem3
#IPSL-CM5A cant find SLP variable in file structure

cfp.mapset(lonmin=-280, lonmax=-100, latmin=-90, latmax=90)
cfp.con(cccma_amon[1] - cccma_amon_c5sul[1], blockfill=True, lines=False)


# In[ ]:




