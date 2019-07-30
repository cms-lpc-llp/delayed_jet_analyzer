# Instructions for Running Muon System LLP Analyzer Notebook(s)

The main notebook for development purposes is muon_roi_trigger_data_nocluster.ipynb. The following instructions will thus be focused on how to run the aforementioned notebook. The other notebooks, which will be transferred to this folder soon, have specific target purposes as defined below.
* muon_roi_trigger_data.ipynb: Implements k-means clustering to identify clusters of CSC hits (Under development)

## Getting Started

### Prerequisites

#### ntuple

To run the notebook, processed MC/data (signal, background, and minBias/ZeroBias) ntuples are required. These ntuples are generated from the CMS data processing workflow. Details of AOD production can be found here [h-to-ss1ss2-madgraph](https://github.com/cms-lpc-llp/h-to-ss1ss2-madgraph)

##### *General CMS Data Processing Workflow*
![CMS Data Processing Workflow](cms_workflow(1).png?raw=true)

1. At the top are samples produced by Madgraph at the Les Houches Event (LHE) stage, which contain only matrix calculations for the model you specify. 

2. These LHE files are then converted into GENSIM samples that include information not available at the level of basic Feynman diagrams. This conversion is done by the CMS offline software known as CMSSW, which contains programs such as Pythia that have access to numerous theories and models and can assist in adding new information or reconstructing physics objects. 

3. At the end of the CMSSW step, the simulated detector readouts created from the LHE stage is replaced with reconstructed physics objects in a form known as Analysis Object Data (AOD). 

4. Finally, an ntupler is used to further reduce the size of the samples and select variables for analysis.

##### *Accessing/Generating ntuples*
For this analysis, nearly all of the AODs required have been processed and placed in the Caltech Tier 2. Instructions on using the ntupler and the locations of the key AODs can be found here: [jet_timing_studies ntupler](https://github.com/cms-lpc-llp/jet_timing_studies)

Currently, the notebook is configured for the signal model ggH -> G<sub>0+</sub> + G<sub>0-</sub> -> MET + bb (for more information on the theory of the model, check out [Naturalness in the Dark at the LHC](https://arxiv.org/pdf/1501.05310.pdf)). ![Feynman Diagram of LLP process](http://inspirehep.net/record/1340705/files/glueball_production.png)
*Note: This will be expanded to include wH production as well as bbbb final states.*

[zeroBias AODs](https://cmsweb.cern.ch/das/request?view=list&limit=150&instance=prod%2Fglobal&input=dataset+dataset%3D%2FZeroBias%2FRun2018*-17Sep2018-v*%2FAOD)

zeroBias ntuples:

```/mnt/hadoop/store/group/phys_exotica/delayedjets/jet_timing_studies/ZeroBias-17Sep2018-v1/ZeroBias/crab_CMSSW_10_2_0_ZeroBias-Run2018A-17Sep2018-v1_jettimingstudies_CaltechT2```

```/mnt/hadoop/store/group/phys_exotica/delayedjets/jet_timing_studies/ZeroBias-17Sep2018-v1/ZeroBias/crab_CMSSW_10_2_0_ZeroBias-Run2018B-17Sep2018-v1_jettimingstudies_CaltechT2```

```/mnt/hadoop/store/group/phys_exotica/delayedjets/jet_timing_studies/ZeroBias-17Sep2018-v1/ZeroBias/crab_CMSSW_10_2_0_ZeroBias-Run2018C-17Sep2018-v1_jettimingstudies_CaltechT2```

#### Tier 2
Verify that you have write access to T2 user space by performing the following from lxplus
```bash
[username@lxplus ~]$ voms-proxy-init -voms cms
[username@lxplus ~]$ cmsenv
[username@lxplus ~]$ source /cvmfs/cms.cern.ch/crab3/crab.sh
[username@lxplus ~]$ crab checkwrite --site T2_US_Caltech
```
*Note: Please use ssh instead of gsissh to access the Tier2 server*
*Further information on the T2 user space can be found [here](https://caltech.teamwork.com/#notebooks/119930)*

Verify that a corresponding GPU account has been created for you on Flere by following the instructions [here](https://github.com/cmscaltech/gpuservers).
*Note: This step will most likely be adjusted in the near future.*

## Setting up the Notebook

### Step 1
Install python2.7, numpy, ROOT, root_numpy, jupyter-notebook (in this order). Make sure to install the packages compatible with python2.7. Note that the Flere GPU server already has the necessary tools for running this notebook.

### Step 2
Setup up the repository in your preferred dir
```bash
git clone https://github.com/cms-lpc-llp/delayed_jet_analyzer.git cms_lpc_llp/delayed_jet_analyzer
```

### Step 3
Include the preferred dir where the delayed_jet_analyzer repository is copied in the notebook
```python
work_location = input("Username: ")
if work_location == 'nasurijr':
    pwd = '/nfshome/nasurijr/delayed_jet_analyzer/'
elif work_location == '<Insert identification here>':
    pwd = '/home/cms/delayed_jet_analyzer/'
```

### Step 4
Check that the data paths and files are correct
```python
data_path = pwd+'data/'
fpath['qcd'] = data_path +'jet_timing_studies_ntuple_RunIIFall17DRPremix_QCD_Pt_170to300_TuneCP5_13TeV_pythia8_1.root'
# etc...
```
The notebook is currently setup for 4 signal samples and 2 background samples as described in the table below:

|  |  | c&tau; | fpath Key | TTree Name | TTree Key |
|--------------|----------------------------|--------|---------------|-----------------|-----------|
| Signal (ggH) | mX = 50 GeV mH = 125 GeV | 1 m | m50ct1m | T | m50ct1m |
| Signal (ggH) | mX = 50 GeV mH = 125 GeV | 10 m | m50ct10000mm | T\_low\_ctau10 | m50ct10m |
| Signal (ggH) | mX = 975 GeV mH = 2000 GeV | 1 m | m975ct1000mm | T\_high\_ctau1 | m975ct1m |
| Signal (ggH) | mX = 975 GeV mH = 2000 GeV | 10 m | m975ct10000mm | T\_high\_ctau10 | m975ct10m |
| Background | QCD |  | qcd | T_bkg | qcd |
| Background | ZeroBias |  | zeroBias | T_minBias | zeroBias |

### Step 5
Run the notebook. If there are any errors, check the surrounding comments or ask @nsurijr
