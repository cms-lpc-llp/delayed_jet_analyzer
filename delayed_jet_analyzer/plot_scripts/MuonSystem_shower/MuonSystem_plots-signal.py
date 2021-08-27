#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ROOT as rt
import csv
import re
import sys
import collections

from collections import OrderedDict
import uproot
import awkward
import numpy as np
import time
from matplotlib import pyplot as plt
sys.path.append('/storage/user/christiw/gpu/christiw/llp/delayed_jet_analyzer/lib/')

from histo_utilities import create_TH1D, create_TH2D, std_color_list, create_TGraph

import CMS_lumi, tdrstyle
tdrstyle.setTDRStyle()
CMS_lumi.writeExtraText = 0

print(sys.version)


# # Load ntuples

# In[2]:


get_ipython().run_cell_magic('time', '', "\nfpath =OrderedDict()\ntree = OrderedDict()\n# can you write decay mode, ms and ctau, in that order\n# pl is the same thing as ctau (edited) \n# for example: bb, m_s = 15 GeV, c#tau = 1000 mm\n# the unit for ctau and pl are both mm and for ms is 15 GeV (edited) \n# for example you are missing ms for the first four legends\n# the # sign will give you the actual greek letter, and underscore will give you a subscript i think\n\n# the ms for ee are 0.1GeV, not 0 DONE\n# can you add units to the mass DONE\n# and add units to ctau DONE\n# also if you are writing ee and bb, can you write tautau and pi0pi0 as well\n# does that make sense, because for all these signal simulations, they are all LLPs decaying to two particles, \n# and the difference is just that what they decay to, the mass of LLP and the lifetime of the LLP\n# can you do it in this format: bb, m_s = 15 GeV, c#tau = 1000 mm\n# also for the last one, bbMS1ctau1000, that one is actually ddMS1ctau1000, there was a mistake in naming the file\n\n\n# looks good, can you make pi also #pi\n# ohhh its pi naught right\n# oh you might have to do m_{s}  it is m subscript s\n# yeah, try #pi^{0} it is pi subscript 0\n\n# and can you also order it by mass and then by ctau if its the same\n# so move the last one to third to last and the 15 GeV to the last one\n# so you would need to change the order in fpath\npath = '/mnt/hadoop/store/group/phys_exotica/delayedjets/displacedJetMuonAnalyzer/csc/V1p17/MC_Fall18/v1/v8/normalized/'\n\nfpath['ee, m_{s} = 0.1 GeV, c#tau = 100 mm'] = path + 'ggH_HToSS_SToEE_ms0p1_pl100_1pb_weighted.root'\nfpath['ee, m_{s} = 0.1 GeV, c#tau = 500 mm'] = path + 'ggH_HToSS_SToEE_ms0p1_pl500_1pb_weighted.root'\nfpath['#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 100 mm'] = path + 'ggH_HToSS_SToPi0Pi0_ms1_pl100_1pb_weighted.root'\nfpath['#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm'] = path + 'ggH_HToSS_SToPi0Pi0_ms1_pl500_1pb_weighted.root'\nfpath['dd, m_{s} = 1 GeV, c#tau = 1000 mm'] = path +  'ggH_HToSSTobbbb_ms1_pl1000_1pb_weighted.root'\nfpath['#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm'] = path +  'ggH_HToSSTo4Tau_MH-125_MS-7_ctau-1000_TuneCP5_13TeV-powheg-pythia8_1pb_weighted.root'\nfpath['bb, m_{s} = 15 GeV, c#tau = 1000 mm'] = path +  'ggH_HToSSTobbbb_MH-125_MS-15_ctau-1000_TuneCP5_13TeV-powheg-pythia8_1pb_weighted.root'\n\n#so you should label your legend according the the decay mode, ms and ctau\n#HToSSTobbbb means the LLPs decay to 2 b quarks, MH is the higgs mass, MS is the LLP mass and ctau is the lifetime\nfor k,v in fpath.items():\n    \n    print (k, v)\n    root_dir = uproot.open(v) \n    tree[k] = root_dir['MuonSystem']\n    print(len(tree[k]))")


# # Helper Functions

# In[3]:


import math
def deltaPhi( phi1,  phi2):
    dphi = phi1-phi2
    while (dphi > math.pi):
        dphi -= 2*math.pi
    while (dphi <= -math.pi):
        dphi += 2*math.pi
    return dphi
def deltaR(eta1, phi1, eta2, phi2):
    dphi = deltaPhi(phi1,phi2)
    deta = eta1 - eta2
    return (dphi*dphi + deta*deta)**0.5


# # Load variables

# In[ ]:





# In[4]:



JET_PT_CUT = 10.0
MUON_PT_CUT = 20.0
jetPt_cut = 50
cluster_index = '3'


weight = {}
pileupWeight = {}

evtNum = {}
runNum = {}
lumiSec = {}
sel_ev = {}
gLLP_beta = {}
gLLP_csc = {}
gLLP_ctau = {}
gLLP_eta={}
cscRechitClusterX = {}
cscRechitClusterY = {}
cscRechitClusterZ = {}
cscRechitClusterPhi = {}
cscRechitClusterEta = {}
cscRechitCluster3NStation = {}
cscRechitClusterNChamber = {}
cscRechitClusterSize = {}
cscRechitClusterAvgStation = {}
cscRechitCluster3XSpread={}
cscRechitCluster3YSpread={}
cscRechitClusterSize={}
cscRechitCluster3Eta={}
cscRechitCluster3AvgStation5={}
weight_ctau={}
NEWweight_ctau={}
t1NEW={}
t2NEW={}
weight_ctauNew={}
sel_ev2={}
gLLP_eta2={}
sel_rechitcluster2={}
weight_ctau_1002500={}
#print(type(cscRechitCluster))

#print(tree.items())
for k, T in tree.items():
        
########### SELECTION: CLUSTERS ############
   
   # print(k)
    sel_rechitcluster = T.array('cscRechitCluster' + cluster_index + '_match_gLLP_csc') ==1   #this pone!!
    
   # print(sel_rechitcluster, 'sel')
  #  sel_rechitcluster2= T.array('cscRechitCluster' + cluster_index + '_match_gLLP_eta') == 1 
   # print(cscRechitCluster3_match_gLLP_eta, k)
    sum_sel_rechitcluster = sel_rechitcluster.any()
   # print(sum_sel_rechitcluster, 'sum')
   # sum_sel_rechitcluster2= sel_rechitcluster2.any()
    
    #print(sel_rechitcluster, 'sel rechit')
    #print(sum_sel_rechitcluster, 'any')
    #print(sel_rechitcluster)
 #   print((np.count_nonzero(sum_sel_rechitcluster))) #% events with a cluster matched to LLP
   # y=(np.count_nonzero(sum_sel_rechitcluster))/len(sum_sel_rechitcluster)
   # print((np.count_nonzero(sum_sel_rechitcluster))/len(sum_sel_rechitcluster) ,'smthn')
    
  #  print(sel_rechitcluster.shape)
   # print( sel_rechitcluster )
  #  print(sel_rechitcluster.any())
    
    
#     def countNew(): 
#         newSum=0
#         for i in range(0, len(sel_rechitcluster)-1):
#             for j in range(0, len(sel_rechitcluster[i])-1):
#                 if sel_rechitcluster[i][j]==True:
#                     newSum+=1
#         return newSum
#     print(countNew())



   
  #  print((np.count_nonzero(sel_rechitcluster.all())))
  #  print((np.count_nonzero(sel_rechitcluster)))
 #   print(countNew())
  #  print(sel_rechitcluster)
 #   sel_rechitcluster = np.logical_and(sel_rechitcluster, np.abs(T.array('cscRechitCluster' + cluster_index + 'Eta')) < 2.0)
   # print (sel_rechitcluster)
#     me1112_veto = 0
#     sel_rechitcluster = np.logical_and(sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + 'NRechitChamberPlus11') == 0)
#     sel_rechitcluster = np.logical_and(sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + 'NRechitChamberPlus12') == 0)
#     sel_rechitcluster = np.logical_and(sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + 'NRechitChamberMinus11') == 0)
#     sel_rechitcluster = np.logical_and(sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + 'NRechitChamberMinus12') == 0)

#     sel_rechitcluster = np.logical_and(sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + '_match_MB1Seg_0p4') == me1112_veto)
#     sel_rechitcluster = np.logical_and(sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + '_match_RE12_0p4') == me1112_veto)
#     sel_rechitcluster = np.logical_and(sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + '_match_RB1_0p4') == me1112_veto)
#     sel_rechitcluster = np.logical_and(sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + 'TimeSpread') <= 20)
    
#     sel_rechitcluster = np.logical_and( sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + 'JetVetoPt') < JET_PT_CUT)
#     sel_rechitcluster = np.logical_and( sel_rechitcluster, T.array('cscRechitCluster' + cluster_index + 'MuonVetoPt') < MUON_PT_CUT)
#     sel_rechitcluster = np.logical_and(sel_rechitcluster, np.logical_and(T.array('cscRechitCluster' + cluster_index + 'TimeTotal') < 12.5, T.array('cscRechitCluster' + cluster_index + 'TimeTotal') > -5.0))
        
########### SELECTION: JETS ############
   
    sel_jet = np.logical_and(T.array('jetPt') > jetPt_cut, np.abs(T.array('jetEta')) < 2.4 )

########### SELECTION: EVENTS ############

    sel_ev[k] = (np.sum(T.array('gLLP_csc'),axis = 1) > 0)

                                               
                                                            
                                                           
#print(newSum/len(weight_ctau[k]), 'accep')
   # print(weight_ctau[sel_ev[k]], )
   # print(newSum/len(weight_ctau[k]), 'newAccep')
   # print(len(sel_ev[k]), 'len sel')
  #  print(weight_ctau[k][sel_ev[k]])
  #  print(len(sel_ev[k]), 'len sel')


#     sel_ev[k]   = np.logical_and(sel_ev[k], T['HLTDecision'].array()[:,310]) # MET trigger
#     sel_ev[k]  = np.logical_and(sel_ev[k], T.array('category') == 0)

#     sel_ev[k] = np.logical_and(sel_ev[k] ,T.array('met') > 200)
#     sel_ev[k] = np.logical_and(sel_ev[k] ,T.array('nLeptons') == 0)
#     sel_ev[k] = np.logical_and(sel_ev[k] , sel_jet.sum()>=1)
#     sel_ev[k] = np.logical_and(sel_ev[k],T.array('Flag2_all'))

########### BRANCHES ############

   ##### event variables ##### 
 #  () tauold/tau new)^2 esp((t1+t2)times (1/tauold- 1/tau new))
 #print(len(t1NEW[k]))
    #print(len(tau_old))
   
    #print(k, 'beta', np.max(T.array('gLLP_beta')[:,0]))

    t1= (T.array('gLLP_ctau')[:,0])[sel_ev[k]][np.logical_and((np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))),
                                   (np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))))]

    t2= (T.array('gLLP_ctau')[:,1])[sel_ev[k]][np.logical_and((np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))),
                                  (np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))))]

    tau_old= 100
    tau_new=50
    expIn= (t1+t2)* ((1/tau_old)-(1/tau_new))
    weight1= (tau_old/tau_new)**2
    weight2=np.exp(expIn)
    weight_ctau[k]=weight1*weight2
    
            
    gLLP_beta[k] = T.array('gLLP_beta')[sel_ev[k]]
    gLLP_csc[k] = T.array('gLLP_csc')[sel_ev[k]] #this one!!
  #  gLLP_eta[k]= T.array('gLLP_eta')[sel_ev[k]]
    gLLP_eta[k]= T.array('gLLP_eta')[T.array('gLLP_csc')==1]    #cut off after eta after
  #  gLLP_eta2[k]= T.array('gLLP_eta')[sel_ev[k]]
   # print(gLLP_eta[k])
    weight[k] = T.array('weight')[sel_ev[k]]
    evtNum[k] =  T.array('evtNum')[sel_ev[k]]  
#   # print('events?',evtNum[k] )
    runNum[k] =  T.array('runNum')[sel_ev[k]]
    lumiSec[k] =  T.array('lumiSec')[sel_ev[k]]
#old for CEFF
    Accep= (np.count_nonzero(sel_ev[k]))/len(sel_ev[k])
    
    #CHANGEDDDDDDDDDDD
    clusterMatched=(np.count_nonzero(sum_sel_rechitcluster))/len(sum_sel_rechitcluster)
    Acceptance= ((np.count_nonzero(sel_ev[k]))/len(sel_ev[k]))
    ClusteringEff= clusterMatched/Acceptance

    if k[:2] == 'mc':
        pileupWeight[k] = T.array('pileupWeight')[sel_ev[k]]
    else:                                   #UNDO LATER UNDO UNDOUNDOUNDOUNDOUNDOUNDOYNDO
        pileupWeight[k] = np.ones(weight[k].shape, dtype=bool)
    if k[:2] == 'mc':
        weight[k] = weight[k]*lumi
    
    ##### cluster-level variables ####  #UNDO LATER UNDO UNDOUNDOUNDOUNDOUNDOUNDOYNDO#UNDO LATER UNDO UNDOUNDOUNDOUNDOUNDOUNDOYNDO#UNDO LATER UNDO UNDOUNDOUNDOUNDOUNDOUNDOYNDO#UNDO LATER UNDO UNDOUNDOUNDOUNDOUNDOUNDOYNDO    # cscRechitCluster3AvgStation5=T.array('cscRechitCluster' + cluster_index + 'AvgStation5')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitClusterPhi[k] = T.array('cscRechitCluster' + cluster_index + 'Phi')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitCluster3NStation[k] = T.array('cscRechitCluster' + cluster_index + 'NStation')[sel_rechitcluster][sel_ev[k]].flatten()
   #  cscRechitCluster3Eta= T.array('cscRechitCluster' + cluster_index + 'Eta')[sel_rechitcluster][sel_ev[k]].flatten()
    # cscRechitClusterSize[k] = T.array('cscRechitCluster' + cluster_index + 'Size')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitClusterX[k] = T.array('cscRechitCluster' + cluster_index + 'X')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitCluster3XSpread[k]=T.array('cscRechitCluster' + cluster_index + 'XSpread')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitCluster3YSpread[k]=T.array('cscRechitCluster' + cluster_index + 'YSpread')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitClusterY[k] = T.array('cscRechitCluster' + cluster_index + 'Y')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitClusterZ[k] = T.array('cscRechitCluster' + cluster_index + 'Z')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitClusterEta[k] = T.array('cscRechitCluster' + cluster_index + 'Eta')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitClusterPhi[k] = T.array('cscRechitCluster' + cluster_index + 'Phi')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitClusterAvgStation[k] = T.array('cscRechitCluster' + cluster_index + 'AvgStation5')[sel_rechitcluster][sel_ev[k]].flatten()
    cscRechitClusterSize[k] =  T.array('cscRechitCluster' + cluster_index + 'Size')[sel_rechitcluster][sel_ev[k]].flatten()
   # cscRechitCluster3_match_gLLP_eta= T.array('cscRechitCluster' + cluster_index + '_match_gLLP_eta')[sel_rechitcluster][sel_ev[k]].flatten()
   # print(cscRechitCluster3_match_gLLP_eta)
    Nrechits=  cscRechitClusterSize[k]
    
#     #print(Nrechits, 'num rechits')
    cscRechitClusterEta[k]= np.abs(cscRechitClusterEta[k])
    cscRechitClusterAvgStation[k]=np.abs(cscRechitClusterAvgStation[k])
   # print(sum_sel_rechitcluster)


    # print((np.count_nonzero(sel_ev[k]))/len(sel_ev[k]), 'acceptance') #acceptances for unweighted 
  
   # print(np.count_nonzero(sum_sel_rechitcluster)/ len(gLLP_eta[k])) #prints correct CLust3erin Eff

    sel_rechitcluster2[k]= ((T.array('cscRechitCluster' + cluster_index + '_match_gLLP_eta'))[sum_sel_rechitcluster])
   # sum_sel_rechitcluster2= sel_rechitcluster2.any()

    def Bigger(lst1, lst2):
        newL=[]
        for i in range(0, len(lst1)):
            if lst1[i]>lst2[i]:
                newL.append(lst1[i]/lst2[i])
        return newL
  
    #HEREHERHEHERHEHERHEHEHEREHEREHEREHERHERHEREHEREHEHEREHERHEHERHEHREHRHREHRHEHRHEHRHEHRH
    #christina the variables i used i copied right here for clarity
    # sel_rechitcluster2= ((T.array('cscRechitCluster' + cluster_index + '_match_gLLP_eta'))[sum_sel_rechitcluster])
    # sum_sel_rechitcluster2= sel_rechitcluster2.any()
    # sel_rechitcluster = T.array('cscRechitCluster' + cluster_index + '_match_gLLP_csc') ==1   #this pone!!
    # sum_sel_rechitcluster = sel_rechitcluster.any()
    # sel_ev[k] = (np.sum(T.array('gLLP_csc'),axis = 1) > 0)
    # gLLP_eta[k]= T.array('gLLP_eta')[T.array('gLLP_csc')==1]

    print(len(sel_rechitcluster2[k])/len(gLLP_eta[k]), ' cluster eff')


# ## 1D histograms

# In[20]:
#christina

start_t = time.time()
c = rt.TCanvas('c','c', 800, 800)
h = {}
leg = rt.TLegend(0.8,.82,0.5,0.92) 
leg.SetTextSize(0.022)
leg.SetBorderSize(0)
leg.SetTextFont(42)

for i, k in enumerate(tree.keys()): 
#     print(sel_rechitcluster2[k], 'sel', len(sel_rechitcluster2[k]), 'len')
#     print(gLLP_eta[k], 'eta', len(gLLP_eta[k]), 'eln')
#     print(len(cscRechitClusterEta[k]), 'eta')
#     print(len(cscRechitClusterPhi[k]), 'phi')
    #print(Bigger(sel_rechitcluster2[k].flatten(), gLLP_eta[k]))
#     print(len(sel_rechitcluster2[k]))
#     print(len(gLLP_eta[k]))
    hm = create_TH1D(sel_rechitcluster2[k].flatten(), axis_title=['Number of Rechits', 'Signal Efficiency'], name='hey', binning=[30,0,2.5])
    hb = create_TH1D((gLLP_eta[k]).flatten(), axis_title=['Number of Rechits', 'Signal Efficiency'], name= 'hey', binning=[30,0,2.5])
    pEff1 = rt.TEfficiency(hm,hb)
    pEff1.Draw()


leg.Draw()
#c.SetLogx()
c.Draw()
c.SaveAs()


# In[ ]:




