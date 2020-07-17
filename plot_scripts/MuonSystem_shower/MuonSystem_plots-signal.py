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

   # sel_ev2[k]= (np.sum(T.array('gLLP_eta'),axis = 1) > 0)
    # add this to sel_ev if doing that thing [np.logical_and((np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])))), (np.logical_not(np.isnan((T.array('gLLP_ctau')[:,1])))))]
   # t1= (T.array('gLLP_ctau')[:,0])[np.logical_and((np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])))),
    #                             (np.logical_not(np.isnan((T.array('gLLP_ctau')[:,1])))))]
   # t2= (T.array('gLLP_ctau')[:,1])[np.logical_and((np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])))),
    #                             (np.logical_not(np.isnan((T.array('gLLP_ctau')[:,1])))))]
  #  t2= (T.array('gLLP_ctau')[:,1])[sel_ev[k]][np.logical_and((np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))),
#(np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))))]
  #  t1= np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])))
   # t2= np.logical_not(np.isnan((T.array('gLLP_ctau')[:,1])))
   # print(t1)
   # print(len(t1))
   # print(len(sel_ev[k]))
   # print(len(sel_ev[k]), 'sel ev len')
   # print(len(t1),'t1 len')
#     tau_old= 100
#     tau_new=1
#     expIn= (t1+t2)* ((1/tau_old)-(1/tau_new))
#     weight1= (tau_old/tau_new)**2
#     weight2=np.exp(expIn)
#     weight_ctau[k]=weight1*weight2
#     newSumTotal= sum(weight_ctau[k])
#     newSum= sum(weight_ctau[k][sel_ev[k]])
   # print(newSum/newSumTotal)
  
  #  print(weight_ctau[k][sel_ev[k]])
    #print(len(weight_ctau[k][sel_ev[k]]))
#wait so look at weight_ctau[k][sel_ev[k]] at 10^6?

#and 10^4, 10^5 for the bb curve
    #10,  1000, 5000, 10000, 100000
# you might still want to keep np.logical_and((np.logical_not(np.isnan((T.array(‘gLLP_ctau’)[:,0])[sel_ev[k]]) then
# and add it to sel_ev[k] as well to keep them the same length
#     def whatType(lst):
#         newLst=[]
#         for i in range(0,len(lst)-1):
#             if type(lst[i]) not in newLst:
#                 newLst.append(type(lst[i]))
#         return newLst

                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
   # print(weight_ctau[k], 'weight US' , len(weight_ctau[k]), 'eln')
    #newSum=sum(weight_ctau[sel_ev[k]])
  #  newVar= ((weight_ctau[k])[sel_ev[k]])
 #   newSum= sum((weight_ctau[k])[sel_ev[k]])
  #  print(sum((weight_ctau[k])[sel_ev[k]]))
  #  newSum2= sum(weight_ctau[k])
   # print(sum(weight_ctau[k]))
   # print(newSum/newSum2)
    
   # print(sum((weight_ctau[k])[sel_ev[k]]), 'sum Sel')
  
    #print(newSum ,'sum sel' ,k)
    #print(sum(weight_ctau[k]), 'sum unselc')
  #  print(newSum/(sum(weight_ctau[k])))
   # print(weight_ctau[k], 'weight', len(weight_ctau[k]), 'len weight')
   # print(weight_ctau[k][sel_ev[k]], 'selected weight', len(weight_ctau[k][sel_ev[k]]), 'selected len')
   # selWeight=weight_ctau[k][sel_ev[k]]
    #print(selWeight)
   # print(k)
   # print(weight_ctau[])
   # newSum= sum(selWeight)
   # print(newSum, 'sum of weight US')
   # print(len(newSum))
  #  print(weight_ctau[sel_ev[k]])
   #  print(newSum, 'sum of weight US')
    
   #
#print(newSum/len(weight_ctau[k]), 'accep')
   # print(weight_ctau[sel_ev[k]], )
   # print(newSum/len(weight_ctau[k]), 'newAccep')
   # print(len(sel_ev[k]), 'len sel')
  #  print(weight_ctau[k][sel_ev[k]])
  #  print(len(sel_ev[k]), 'len sel')
        
    
    #use sel_ev[k] to index the weight_ctau[k] that pass the selection
    

#     def WeightThatPassesSel(weight):
#         sum=0
#         for i in range(0, len(weight)-1):
#             sum+=weight[i]
#         return sum
   # print(CutAtWeight(Nrechits, 150,  weight_ctau[k]), 'over 150')
   # print(sum(weight_ctau[k]))
    #print((CutAtWeight(Nrechits, 400,  weight_ctauNew[k]))/(sum(weight_ctauNew[k])))
   # print((weight_ctau[k])[sel_ev[k]])
  #  print(WeightThatPassesSel(weight_ctau[sel_ev[k]])/sum(weight_ctau[k]), 'new accep')

   # print((CutAtWeightUW(Nrechits, 400))/len(Nrechits))
  #  print((np.count_nonzero(sel_ev[k])) , 'nonzero count for sel_ev')
#     y2=(np.count_nonzero(sum_sel_rechitcluster2))/len(sum_sel_rechitcluster2)
#    # print((np.count_nonzero(sel_ev[k]))/len(sel_ev[k]), 'acceptance') #acceptances for unweighted 
#     Accep= (np.count_nonzero(sel_ev[k]))/len(sel_ev[k])
    
#     #CHANGEDDDDDDDDDDD
#     clusterMatched=(np.count_nonzero(sum_sel_rechitcluster))/len(sum_sel_rechitcluster)
#     Acceptance= ((np.count_nonzero(sel_ev[k]))/len(sel_ev[k]))
#     ClusteringEff= clusterMatched/Acceptance

#     sel_ev[k] = (np.sum(T.array('gLLP_csc'),axis = 1) > 0)
#     sel_rechitcluster2= T.array('cscRechitCluster' + cluster_index + '_match_gLLP_e') 
#     sum_sel_rechitcluster2= sel_rechitcluster2.any()
#     gLLP_eta[k]= T.array('gLLP_eta')[sel_ev[k]]
# ok great
# 4:24
# so you should define sel_ev[k] and sum_sel_rechitcluster the same way
# 4:25
# so before you simply counted the number of events with the two conditions
# 4:25
# regardless of LLP eta
# 4:25
# but now you want to calculate the efficiency wrt to eta
# 4:26
# so you should get the eta that corresponds to those events that you counted 

#     print(y2/ Accep, 'ce')
# you can use sel_ev[k] to index the weight_ctau[k] that pass the selection
# 11:18
# and take the sum

   # sel_ev[k]  = np.logical_and(sel_ev[k],sel_rechitcluster.sum() == 1) 
   # sel_ev2[k]  = np.logical_and(sel_ev2[k],sel_rechitcluster.sum() == 1) 
#   print(T.array('gLLP_csc'))
#    print(sel_ev[k

   # print(np.count_nonzero(weight_ctau[k]), 'nonzero for weight')
   # print(sum())
    #the acceptance, which is the number of events that has at least 1 LLP decay in CSC. 
# calculate the acceptance(the one you did in slide 2) for different ctau
# so in slide 2 you assumed ctau of 500mm for m=1GeV and pi0pi0 decay, then you can reweight
# that sample to 100, 200, 300mm, and recalculate the acceptance after the reweight
  #  t1= (T.array('gLLP_ctau')[:,0])[sel_ev[k]][np.logical_and((np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))),
  #                                (np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))))]
  #  t2= (T.array('gLLP_ctau')[:,1])[sel_ev[k]][np.logical_and((np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))),
#(np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))))]

    
  #     def countAccep(): 
#         newSum=0
#         for i in range(0, len(sel_ev[k])-1):
#             if sel_ev[k][i]==True:
#                 newSum+=1
#         return newSum
  

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
#    # print(len(t1), 't1 len')
# #you should sum the weights of events that pass the Nrechit cut and divide by the sum of all weights
# #ok so for the weighted i can sumthe weights of events that pass the cut and then divide by the sum  and for the not weighted just do it with sel_ev[k[
#     #print(k, 't1', np.sum(t1))
#     #the acceptance, which is the number of events that has at least 1 LLP decay in CSC. 
    t2= (T.array('gLLP_ctau')[:,1])[sel_ev[k]][np.logical_and((np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))),
                                  (np.logical_not(np.isnan((T.array('gLLP_ctau')[:,0])[sel_ev[k]]))))]

    tau_old= 100
    tau_new=50
    expIn= (t1+t2)* ((1/tau_old)-(1/tau_new))
    weight1= (tau_old/tau_new)**2
    weight2=np.exp(expIn)
    weight_ctau[k]=weight1*weight2
    
#     tau_old_100= 100
#     tau_new_500= 10
#     expInNew= (t1+t2)* ((1/tau_old_100)-(1/tau_new_500))
#     weight1New= (tau_old_100/tau_new_500)**2
#     weight2New=np.exp(expInNew)
#     weight_ctauNew[k]=weight1New*weight2New
   # sum_weight_ctauNew= sum(weight_ctauNew[k])
    #print('sum', sum_weight_ctauNew)
    #print('sum',sum_weight_ctau)
   # print(weight_ctau[k])
  #  print(len(weight_ctau[k]), 'len weight')
    
#     t1NEW[k]= T.array('gLLP_ctau')[:,0][np.logical_and(np.logical_not(np.isnan(T.array('gLLP_ctau')[:,0])),
#                                   (np.logical_not(np.isnan(T.array('gLLP_ctau')[:,1]))))]
#   #  print(k,t1NEW[k] )
#    # print('t1', t1NEW[k],'sum', sum(t1NEW[k]))
#    # print(k, 't1NEW sum',np.sum(t1NEW[k]))
#   #  print(len(t1NEW[k]))
#     t2NEW[k]= T.array('gLLP_ctau')[:,1][np.logical_and(np.logical_not(np.isnan(T.array('gLLP_ctau')[:,0])),
#                                   (np.logical_not(np.isnan(T.array('gLLP_ctau')[:,1]))))]
#    # print('t2',t2NEW[k], 'sum', sum(t2NEW[k]) )
#    # print(len(t2NEW[k]))
#     expInNEW= (t1NEW[k]+t2NEW[k])* ((1/tau_old)-(1/tau_new))
#    # print('expInNEW',expInNEW, 'sum', sum(expInNEW) )
#   #  print(k, 'expInNEW', np.sum(expInNEW))
#     weight2NEW=np.exp(expInNEW)
#    # print('weight2NEW',weight2NEW, 'sum', sum(weight2NEW) )
#     NEWweight_ctau[k]=weight1*weight2NEW
#   #  print('NEWweight_ctau[k]',NEWweight_ctau[k], 'sum', sum(NEWweight_ctau[k]) )
#   #  print('w', NEWweight_ctau[k])
    
    
#    # print(len(t2NEW[k]))
#     tau_old_100= 10
#     tau_new_500= 50
#     expInNEW= (t1NEW[k]+t2NEW[k])* ((1/ tau_old_100)-(1/tau_new_500))
#    # print(expIn_1002500, 'sum ExpIn', sum(expIn_1002500))
#     weight1_1002500= (tau_old_100/tau_new_500)**2
#    # print(k, 'expInNEW', np.sum(expInNEW))
#     weight2_1002500=np.exp(expInNEW)
#     weight_ctau_1002500[k]=weight1_1002500*weight2_1002500
 #   print('weight_ctau_1002500', weight_ctau_1002500, 'sum', sum(weight_ctau_1002500))
   # print('w', NEWweight_ctau[k])
    #print(k, np.sum(NEWweight_ctau[k]))
  #  print(len(NEWweight_ctau[k]))
    #print(weight_ctau[k])
    #print(len(weight_ctau[k]))
  #  print(type(weight_ctau))
   # newDict={}
    #newDict.update({k: weight_ctau})
   
   # print(len(t1NEW))
   # print(len(NEWweight_ctau[k]))
 #   print(weight_ctau.shape[0])
    #print(len(t1))
  #  print(len(weight_ctau))
   # print(weight_ctau)
#     weight=weight.flatten()
  #  print(weight_ctau)
  #  np.exp()
                                                              
    gLLP_beta[k] = T.array('gLLP_beta')[sel_ev[k]]
    gLLP_csc[k] = T.array('gLLP_csc')[sel_ev[k]] #this one!!
  #  gLLP_eta[k]= T.array('gLLP_eta')[sel_ev[k]]
    gLLP_eta[k]= T.array('gLLP_eta')[T.array('gLLP_csc')==1]    #cut off after eta after
  #  gLLP_eta2[k]= T.array('gLLP_eta')[sel_ev[k]]
   # print(gLLP_eta[k])
    weight[k] = T.array('weight')[sel_ev[k]]
    evtNum[k] =  T.array('evtNum')[sel_ev[k]]  #UNDO LATER UNDO UNDOUNDOUNDOUNDOUNDOUNDOYNDO
#   # print('events?',evtNum[k] )
    runNum[k] =  T.array('runNum')[sel_ev[k]]
    lumiSec[k] =  T.array('lumiSec')[sel_ev[k]]
#     so you should have a list of gLLP_eta
# 3:27
# and another list of gLLP_eta, where you know the LLP is matched to a cluster, which means it made a cluster
# 3:28
# when you simply take the ratio of the length of the two lists, you should get your inclusive efficiency
 #   print(len(sel_rechitcluster)/ len(gLLP_eta[k]))
    
  
   # print((np.count_nonzero(sel_ev[k]))/len(sel_ev[k]), 'acceptance') #acceptances for unweighted 
    Accep= (np.count_nonzero(sel_ev[k]))/len(sel_ev[k])
    
    #CHANGEDDDDDDDDDDD
    clusterMatched=(np.count_nonzero(sum_sel_rechitcluster))/len(sum_sel_rechitcluster)
    Acceptance= ((np.count_nonzero(sel_ev[k]))/len(sel_ev[k]))
    ClusteringEff= clusterMatched/Acceptance
  

   # print(np.count_nonzero(sum_sel_rechitcluster)/len(gLLP_eta[k]), 'ms')  #DIS WHAT YOU WANT DIS RIGHT HERE WHAT YOU ARE GRAPH
#     def countNEw():
#         newSum=0
#         for i in range(0, len(sel_rechitcluster)-1):
#             for j in range(0, len(sel_rechitcluster[i])-1):
#                 newSum+=np.count_nonzero(sel_rechitcluster[i][j])
#         return newSum
#     print(countNEw())
    #print((np.count_nonzero(gLLP_csc[k])))

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
    #print(Bigger(sel_rechitcluster2[k].flatten(), gLLP_eta[k]))
    #print(sel_rechitcluster2[k], 'sel')
   # print(gLLP_eta[k],'eta')
    #HEREHERHEHERHEHERHEHEHEREHEREHEREHERHERHEREHEREHEHEREHERHEHERHEHREHRHREHRHEHRHEHRHEHRH
    # sel_rechitcluster2= ((T.array('cscRechitCluster' + cluster_index + '_match_gLLP_eta'))[sum_sel_rechitcluster])
    # sum_sel_rechitcluster2= sel_rechitcluster2.any()
    # sel_rechitcluster = T.array('cscRechitCluster' + cluster_index + '_match_gLLP_csc') ==1   #this pone!!
    # sum_sel_rechitcluster = sel_rechitcluster.any()
    # sel_ev[k] = (np.sum(T.array('gLLP_csc'),axis = 1) > 0)
    # gLLP_eta[k]= T.array('gLLP_eta')[T.array('gLLP_csc')==1]

    #print(len(sel_rechitcluster2[k])/len(gLLP_eta[k]), 'should print cluster eff') #THIS RIGHT BOYSSSSSSSSSSSSSSSSSSSSSSS   
# correc t wout sum

  #  print(len(sel_rechitcluster2)/len(gLLP_eta[k]), 'sum')
#     also you should name sel_rechitcluster2 to something more meaningful, like cluster_match_eta
#     also it has to be a dictionary

  #  print(len(sel_rechitcluster2)/len(gLLP_eta[k]), 'should print cluster eff') #THIS RIGHT BOYSSSSSSSSSSSSSSSSSSSSSSS
    
#     sel_rechitcluster2= T.array('cscRechitCluster' + cluster_index + '_match_gLLP_eta')  
#     sum_sel_rechitcluster2= sel_rechitcluster2.any()
#     print(len(sel_rechitcluster2[k]) ,'num len')
#     print(np.shape(hm), 'shapehm')
   
   # print(cscRechitClusterAvgStation[k])
  #  print(cscRechitClusterEta[k].shape[0])
#print(cscRechitClusterEta[k].shape)
   # print('u', len(cscRechitClusterEta[k]))
 #   print(type(cscRechitClusterEta[k]))
 #   print(cscRechitClusterEta[k])
  #  print(cscRechitCluster3Eta)
#print((tree.keys()))
        # 100, 150, 200, 300, 400 percent that passes the cuts
    def CutAtWeight(lst, num, weight):
        sum=0
        for i in range(0, len(lst)-1):
            if lst[i]>num:
                sum+=weight[i]
        return sum
    # print(CutAtWeight(Nrechits, 150,  weight_ctau[k]), 'over 150')
    # print(sum(weight_ctau[k]))
   # print((CutAtWeight(Nrechits, 400,  weight_ctau[k]))/(sum(weight_ctau[k])))


#     def CutAtWeightUW(lst,num):
#         sum=0
#         for i in range(0, len(lst)-1):
#             if lst[i]>num:
#                 sum+=1
#         return sum
   # print((CutAtWeightUW(Nrechits, 400))/len(Nrechits))
   # print(len(Nrechits), 'len')
  #  weight_ctau[k]
  #  weight_ctauNew[k]
  #  print(k)
       # print( t1) t1NEW= (T.array('gLLP_ctau')[:,0])
#     t2NEW= (T.array('gLLP_ctau')[:,1])
#     tau_oldNEW= 1000
#     tau_newNEW=500
#     expInNEW= (t1NEW+t2NEW)* ((1/tau_oldNEW)-(1/tau_newNEW))
#     weight1NEW= (tau_oldNEW/tau_newNEW)**2
#     weight2NEW=np.exp(expInNEW)
#     NEWweight_ctau[k]=weight1NEW*weight2NEW
   # print( T.array('gLLP_ctau'))

#so for the unweighted ones, you could just count the number of 
#events that pass the cut divided by the total number of events(not summing Nrechits)
#print(T.array('cscRechitCluster'  + 'NStation')[sel_rechitcluster][sel_ev[k]].flatten())
#print(T.show())
#print(cscRechitCluster3Eta)
#print(newDict)
#print(tree.keys())
#print(tree.keys().get(1))
#print(enumerate(tree.keys()))
#print(tree.keys().get(0))
# 10^6 len= 488469
# 10^5 len= 488469
# 10^4 len= 488469

#10^4= 2988000
#10^5= 2988000
#10^6= 2988000

#so you want to get the list of gLLP_eta for the events that pass sel_ev[k]


# ## 1D histograms

# In[20]:


#pretend he works

#can you plot ee and pi0 with the original 500mm samples, and dd, tautau, bb reweighted from 1000 to 500
#and maybe do it for all the plots you have in the slides, 
#and just put the new plots on the left, so we can see both plots in the same slides
#if possible, maybe try to use the same color for the decay modes, so its easier to compare

c = rt.TCanvas('c','c',800,800)
h = {}
leg = rt.TLegend(0.18,.73,0.35,0.94)  # 1= left/right, 2= height/space out of legend vertical 3 = space of legend horiz
# 4 = vertical height 
leg.SetTextSize(0.022)
leg.SetBorderSize(0)
leg.SetTextFont(42)
# for i, k in enumerate(tree.keys()): #works
#   #  print(k, len(cscRechitCluster3XSpread[k]))
#     h[k] = create_TH1D( cscRechitCluster3XSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, \
#                        binning=[50,0,100], weights= weight_ctau[k])
#     h[k].SetLineColor(std_color_list[i])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)

newN1='dd, m_{s} = 1 GeV, c#tau = 500 mm'
newN2='#tau#tau, m_{s} = 7 GeV, c#tau = 500 mm'
newN3='bb, m_{s} = 15 GeV, c#tau = 500 mm'

kNNEW=(newN1, newN2,newN3)
#     h[k].DrawNormalized('same hist')
new1='dd, m_{s} = 1 GeV, c#tau = 1000 mm'
new2='#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm'
new3='bb, m_{s} = 15 GeV, c#tau = 1000 mm'
kNEW=(new1, new2,new3)
i=4
j=0

for k in kNEW:
   # print(weight_ctau[k])
   # print('len avg station', len(cscRechitClusterAvgStation[k]), 'len weight', len(weight_ctau[k]))
    h[k] = create_TH1D(  cscRechitClusterEta[k], axis_title=['RechitCluster Eta', 'Events'], name=k, binning=[30,0,2.5], weights=weight_ctau[k])
   
    h[k].SetLineColor(std_color_list[i])
    leg.AddEntry(h[k], kNNEW[j])
    h[k].GetXaxis().SetLabelSize(0.04)
    h[k].DrawNormalized('same hist')
    j+=1
    i+=1

#key1= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 100 mm'
k2= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm'
h[k2] = create_TH1D(  cscRechitClusterEta[k2], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k2, binning=[30,0,2.5])
h[k2].SetLineColor(std_color_list[3])
leg.AddEntry(h[k2], k2)
h[k2].GetXaxis().SetLabelSize(0.04)
h[k2].DrawNormalized('same hist')  

##newKey1= 'ee, m_{s} = 0.1 GeV, c#tau = 100 mm'
k3= 'ee, m_{s} = 0.1 GeV, c#tau = 500 mm'
newK= 'ee, m_{s} = 1 GeV, c#tau = 500 mm'
h[k3] = create_TH1D(   cscRechitClusterEta[k3], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k3, binning=[30,0,2.5])
h[k3].SetLineColor(std_color_list[1])
leg.AddEntry(h[k3], newK)
h[k3].GetXaxis().SetLabelSize(0.04)
h[k3].DrawNormalized('same hist')  
#you should sum the weights of events that pass the Nrechit cut and divide by the sum of all weights
# 100, 150, 200, 300, 400
#and calculate the percentage of signal events in each sample passes those cuts

#     h[k] = create_TH1D( cscRechitCluster3YSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, binning=[50,0,200])
#     h[k].SetLineColor(std_color_list[3])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')  
# for i,k in ('ee, m_{s} = 0.1 GeV, c#tau = 100 mm','ee, m_{s} = 0.1 GeV, c#tau = 500 mm'):
#     h[k] = create_TH1D( cscRechitCluster3YSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, binning=[50,0,200])
#     h[k].SetLineColor(std_color_list[4])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')      
  

leg.Draw()
c.SetLogy()
c.Draw()
c.SaveAs()


# In[85]:


#pretend he works

#can you plot ee and pi0 with the original 500mm samples, and dd, tautau, bb reweighted from 1000 to 500
#and maybe do it for all the plots you have in the slides, 
#and just put the new plots on the left, so we can see both plots in the same slides
#if possible, maybe try to use the same color for the decay modes, so its easier to compare

c = rt.TCanvas('c','c',800,800)
h = {}
leg = rt.TLegend(0.26,.73,0.20,0.94)  # 1= left/right, 2= height/space out of legend vertical 3 = space of legend horiz
# 4 = vertical height 
leg.SetTextSize(0.022)
leg.SetBorderSize(0)
leg.SetTextFont(42)
# for i, k in enumerate(tree.keys()): #works
#   #  print(k, len(cscRechitCluster3XSpread[k]))
#     h[k] = create_TH1D( cscRechitCluster3XSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, \
#                        binning=[50,0,100], weights= weight_ctau[k])
#     h[k].SetLineColor(std_color_list[i])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
kNEW=(new1, new2,new3)
newN1='dd, m_{s} = 1 GeV, c#tau = 500 mm'
newN2='#tau#tau, m_{s} = 7 GeV, c#tau = 500 mm'
newN3='bb, m_{s} = 15 GeV, c#tau = 500 mm'
kNNEW=(newN1, newN2,newN3)
#     h[k].DrawNormalized('same hist')
new1='dd, m_{s} = 1 GeV, c#tau = 1000 mm'
new2='#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm'
new3='bb, m_{s} = 15 GeV, c#tau = 1000 mm'
i=4
j=0
for k in kNEW:
    print(weight_ctau[k])
    h[k] = create_TH1D(cscRechitClusterEta[k], axis_title=['RechitCluster3 Eta', 'Events'], name=k, binning=[30, 0, 2.5], weights=np.ones(shape=len(weight_ctau[k])))
    h[k].SetLineColor(std_color_list[i])
    leg.AddEntry(h[k], kNNEW[j])
    h[k].GetXaxis().SetLabelSize(0.04)
    h[k].DrawNormalized('same hist')
    j+=1
    i+=1

#key1= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 100 mm'
k2= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm'
h[k2] = create_TH1D(cscRechitClusterEta[k2], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k2, binning=[30, 0, 2.5])
h[k2].SetLineColor(std_color_list[3])
leg.AddEntry(h[k2], k2)
h[k2].GetXaxis().SetLabelSize(0.04)
h[k2].DrawNormalized('same hist')  

##newKey1= 'ee, m_{s} = 0.1 GeV, c#tau = 100 mm'
k3= 'ee, m_{s} = 0.1 GeV, c#tau = 500 mm'
h[k3] = create_TH1D( cscRechitClusterEta[k3], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k3, binning=[30, 0, 2.5])
h[k3].SetLineColor(std_color_list[1])
leg.AddEntry(h[k3], k3)
h[k3].GetXaxis().SetLabelSize(0.04)
h[k3].DrawNormalized('same hist')  

#     h[k] = create_TH1D( cscRechitCluster3YSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, binning=[50,0,200])
#     h[k].SetLineColor(std_color_list[3])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')  
# for i,k in ('ee, m_{s} = 0.1 GeV, c#tau = 100 mm','ee, m_{s} = 0.1 GeV, c#tau = 500 mm'):
#     h[k] = create_TH1D( cscRechitCluster3YSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, binning=[50,0,200])
#     h[k].SetLineColor(std_color_list[4])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')      
  

leg.Draw()
c.SetLogy()
c.Draw()
c.SaveAs()


# In[ ]:


# Plotting ncsc



#FOR THE CHECK
start_t = time.time()
c = rt.TCanvas('c','c', 800, 800)
h = {}
leg = rt.TLegend(0.5,.73,0.45,0.94)  # 1= left/right, 2= height/space out of legend vertical 3 = space of legend horiz
# 4 = vertical height 
leg.SetTextSize(0.022)
leg.SetBorderSize(0)
leg.SetTextFont(42)
#NEWweight_ctau[k]
# for i, k in enumerate(tree.keys()):
#     print('sum', np.sum(NEWweight_ctau[k]), 'len', len(NEWweight_ctau[k]))
#     print('sum', np.sum(t1NEW[k]), 'len', len((t1NEW[k])))
#     h[k] = create_TH1D(t1NEW[k], axis_title=['RechitCluster3 gLLp_ctau', 'Events'], name=k, \
#                        binning=[50,0,1000], weights=NEWweight_ctau[k])
#     h[k].SetLineColor(std_color_list[i])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')
    
#     h[k].GetXaxis().SetLabelSize(0.04)

newN1='dd, m_{s} = 1 GeV, c#tau = 500 mm weighted'
newN2='#tau#tau, m_{s} = 7 GeV, c#tau = 500 mm weighted'
newN3='bb, m_{s} = 15 GeV, c#tau = 500 mm weighted'
kNNEW=(newN1, newN2,newN3)
#     h[k].DrawNormalized('same hist')
new1='dd, m_{s} = 1 GeV, c#tau = 1000 mm'
new2='#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm'
new3='bb, m_{s} = 15 GeV, c#tau = 1000 mm'
kNEW=(new1, new2,new3)
i=4
j=0
for k in kNEW:
    h[k] = create_TH1D( cscRechitCluster3XSpread[k], axis_title=['RechitCluster3 check', 'Events'], name=k, binning=[50, 0, 1000], weights=NEWweight_ctau[k])
    h[k].SetLineColor(std_color_list[i])
    leg.AddEntry(h[k], kNNEW[j])
    h[k].GetXaxis().SetLabelSize(0.04)
    h[k].DrawNormalized('same hist')
    j+=1
    i+=1


k2= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm'
h[k2] = create_TH1D( cscRechitCluster3XSpread[k2], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k2, binning=[50, 0, 1000])
h[k2].SetLineColor(std_color_list[3])
leg.AddEntry(h[k2], k2)
h[k2].GetXaxis().SetLabelSize(0.04)
h[k2].DrawNormalized('same hist')  

k3= 'ee, m_{s} = 0.1 GeV, c#tau = 500 mm'
h[k3] = create_TH1D( cscRechitCluster3XSpread[k3], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k3, binning=[50, 0, 1000])
h[k3].SetLineColor(std_color_list[2])
leg.AddEntry(h[k3], k3)
h[k3].GetXaxis().SetLabelSize(0.04)
h[k3].DrawNormalized('same hist')  

leg.Draw()
c.SetLogy()
c.Draw()
c.SaveAs()


# In[1]:


# Plotting ncsc



#FOR THE CHECK
start_t = time.time()
c = rt.TCanvas('c','c', 800, 800)
h = {}
leg = rt.TLegend(0.5,.73,0.45,0.94)  # 1= left/right, 2= height/space out of legend vertical 3 = space of legend horiz
# 4 = vertical height 
leg.SetTextSize(0.022)
leg.SetBorderSize(0)
leg.SetTextFont(42)
#NEWweight_ctau[k]
# for i, k in enumerate(tree.keys()):
#     print('sum', np.sum(NEWweight_ctau[k]), 'len', len(NEWweight_ctau[k]))
#     print('sum', np.sum(t1NEW[k]), 'len', len((t1NEW[k])))
#     h[k] = create_TH1D(t1NEW[k], axis_title=['RechitCluster3 gLLp_ctau', 'Events'], name=k, \
#                        binning=[50,0,1000], weights=NEWweight_ctau[k])
#     h[k].SetLineColor(std_color_list[i])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')
    
#     h[k].GetXaxis().SetLabelSize(0.04)

newN1='dd, m_{s} = 1 GeV, c#tau = 500 mm weighted'
newN2='#tau#tau, m_{s} = 7 GeV, c#tau = 500 mm weighted'
newN3='bb, m_{s} = 15 GeV, c#tau = 500 mm weighted'
kNNEW=(newN1, newN2,newN3)
#     h[k].DrawNormalized('same hist')
new1='dd, m_{s} = 1 GeV, c#tau = 1000 mm'
new2='#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm'
new3='bb, m_{s} = 15 GeV, c#tau = 1000 mm'
kNEW=(new1, new2,new3)
i=4
j=0
for k in kNEW:
    #print(weight_ctau[k])
    h[k] = create_TH1D(t1NEW[k], axis_title=['RechitCluster3 check', 'Events'], name=k, binning=[50, 0, 1000], weights=NEWweight_ctau[k])
    h[k].SetLineColor(std_color_list[i])
    leg.AddEntry(h[k], kNNEW[j])
    h[k].GetXaxis().SetLabelSize(0.04)
    h[k].DrawNormalized('same hist')
    j+=1
    i+=1

NKey1= 'ee, m_{s} = 0.1 GeV, c#tau = 100 mm'
NKey2= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 100 mm'
Nkey= (NKey1, NKey2)

Nkey1NEW= 'ee, m_{s} = 0.1 GeV, c#tau = 500 mm weighted'
Nkey2NEW= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 500 mm weighted'
NkeyNEW= (Nkey1NEW, Nkey2NEW)
p=0
l=0
for k5 in Nkey:
  #  print('1002500',weight_ctau_1002500[k5], 'sum', sum(weight_ctau_1002500[k5]))
    h[k5] = create_TH1D(t1NEW[k5], axis_title=['RechitCluster3 check', 'Events'], name=k5, binning=[50, 0, 1000], weights=weight_ctau_1002500[k5])
    h[k5].SetLineColor(std_color_list[p])
    leg.AddEntry(h[k5], NkeyNEW[l])
    h[k5].GetXaxis().SetLabelSize(0.04)
    h[k5].DrawNormalized('same hist')
    l+=1
    p+=1

#key1= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 100 mm'
k2= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm'
h[k2] = create_TH1D(t1NEW[k2], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k2, binning=[50, 0, 1000])
h[k2].SetLineColor(std_color_list[3])
leg.AddEntry(h[k2], k2)
h[k2].GetXaxis().SetLabelSize(0.04)
h[k2].DrawNormalized('same hist')  

##newKey1= 'ee, m_{s} = 0.1 GeV, c#tau = 100 mm'
k3= 'ee, m_{s} = 0.1 GeV, c#tau = 500 mm'
h[k3] = create_TH1D(t1NEW[k3], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k3, binning=[50, 0, 1000])
h[k3].SetLineColor(std_color_list[2])
leg.AddEntry(h[k3], k3)
h[k3].GetXaxis().SetLabelSize(0.04)
h[k3].DrawNormalized('same hist')  

leg.Draw()
c.SetLogy()
c.Draw()
c.SaveAs()

#leg.SetEntrySeparation(0.01)
#     print(len(t1NEW[k]))
#     print(len(NEWweight_ctau[k]))
#     if not i == 0:continue
   # print(k, len(cscRechitCluster3XSpread[k]))
  #  , weights=NEWweight_ctau[k]
# for i, k in enumerate(tree.keys()):
    
# #    # t2NEW[= (T.array('gLLP_ctau')[:,1])
# #     print(len(t1NEW[k]))
# #     print(len(NEWweight_ctau[k]))
#     h[k] = create_TH1D(t1NEW[k] , axis_title=['RechitCluster3 gLLp_ctau', 'Events'], name=k, binning=[50,0,200], weights=NEWweight_ctau[k])
#     h[k].SetLineColor(std_color_list[1])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')   
# leg.Draw()
# #c.SetLogy()
# c.Draw()
# c.SaveAs()

#h = {}
#h1={}
#t1NEW={}
#t2NEW={}

#can you plot ee and pi0 with the original 500mm samples, and dd, tautau, bb reweighted from 1000 to 500
#and maybe do it for all the plots you have in the slides, 
#and just put the new plots on the left, so we can see both plots in the same slides
#if possible, maybe try to use the same color for the decay modes, so its easier to compare



#print(cscRechitCluster3NStation[k])
# for i, k in enumerate(tree.keys()):
#     print(k, len(cscRechitClusterX[k]))
#     h[k] = create_TH1D( cscRechitCluster3XSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, \
#                        binning=[50,0,100])
#     h[k].SetLineColor(std_color_list[i])
#    # leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')
# fpath['ee, m_{s} = 0.1 GeV, c#tau = 100 mm'] 
# fpath['ee, m_{s} = 0.1 GeV, c#tau = 500 mm'] 
# fpath['#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 100 mm'] 
# fpath['#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm'] '
# fpath['dd, m_{s} = 1 GeV, c#tau = 1000 mm'] 
# fpath['#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm']
# fpath['bb, m_{s} = 15 GeV, c#tau = 1000 mm']
# tree.keys()
#,'bb, m_{s} = 15 GeV, c#tau = 1000 mm'
#odict_keys(['ee, m_{s} = 0.1 GeV, c#tau = 100 mm', 'ee, m_{s} = 0.1 GeV, c#tau = 500 mm', '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 100 mm',
#'#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm', 'dd, m_{s} = 1 GeV, c#tau = 1000 mm', '#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm',
#'bb, m_{s} = 15 GeV, c#tau = 1000 mm'])
# >>> for i in enumerate(['a', 'b']):
# ...   print(i[0], i[1])
# ...
# 0 a
# 1 b
#T.array(‘gLLP_ctau’)[sel_ev[k]][:,0] for the first LLP and [:,1]
# def newKeys():
#     for k, T in tree.items():
#         t1NEW= (T.array('gLLP_ctau')[:,0])
#         t2NEW= (T.array('gLLP_ctau')[:,1])

#         tau_oldNEW= 1000
#         tau_newNEW=500
#         expInNEW= (t1NEW+t2NEW)* ((1/tau_oldNEW)-(1/tau_newNEW))
#         weight1NEW= (tau_oldNEW/tau_newNEW)**2
#         weight2NEW=np.exp(expInNEW)
#         weight_ctau[k]=weight1NEW*weight2NEW
#     return weight_ctau[k]

#weight_ctauNEW[k]=newKeys()    #WORKS
# for i, k in enumerate(tree.keys()):
#     h[k] = create_TH1D(t1NEW , axis_title=['RechitCluster3 gLLp_ctau', 'Events'], name=k, binning=[1000,0,200], weights=newKeys())
#     h[k].SetLineColor(std_color_list[1])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')
# for k, T in tree.items():
#     t1= (T.array('gLLP_ctau')[:,0])
#     t2= (T.array('gLLP_ctau')[:,1])
#     expInNEW= (t1+t2)* ((1/tau_old)-(1/tau_new))
#     weight1NEW= (tau_old/tau_new)**2
#     weight2NEW=np.exp(expInNEW)
#     NEWweight_ctau[k]=weight1NEW*weight2NEW
#     t1NEW[k]= t1

    
    
    
#     h1[k] = create_TH1D(t1NEW , axis_title=['RechitCluster3 yeet]', 'Events'], name=k, binning=[1000,0,200])
#     h1[k].SetLineColor(std_color_list[0])
#     leg.AddEntry(h1[k], k)
#     h1[k].GetXaxis().SetLabelSize(0.04)
#     h1[k].DrawNormalized('same hist')


# new1='dd, m_{s} = 1 GeV, c#tau = 1000 mm'
# new2='#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm'
# new3='bb, m_{s} = 15 GeV, c#tau = 1000 mm'
# kNEW=(new1, new2,new3)
# i=4
# for k in kNEW:
#     h[k] = create_TH1D( cscRechitCluster3YSpread[k], axis_title=['RechitCluster3 Y Spread [cm] weighted', 'Events'], name=k, binning=[50,0,200], weights=weight_ctau[k])
#     h[k].SetLineColor(std_color_list[i])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')  
#     i+=1

# #key1= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 100 mm'
# k2= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm'
# h[k2] = create_TH1D( cscRechitCluster3YSpread[k2], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k2, binning=[50,0,200])
# h[k2].SetLineColor(std_color_list[3])
# leg.AddEntry(h[k2], k2)
# h[k2].GetXaxis().SetLabelSize(0.04)
# h[k2].DrawNormalized('same hist')  

# #newKey1= 'ee, m_{s} = 0.1 GeV, c#tau = 100 mm'
# k3= 'ee, m_{s} = 0.1 GeV, c#tau = 500 mm'

# h[k3] = create_TH1D( cscRechitCluster3YSpread[k3], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k3, binning=[50,0,200])
# h[k3].SetLineColor(std_color_list[1])
# leg.AddEntry(h[k3], k3)
# h[k3].GetXaxis().SetLabelSize(0.04)
# h[k3].DrawNormalized('same hist')  

#     h[k] = create_TH1D( cscRechitCluster3YSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, binning=[50,0,200])
#     h[k].SetLineColor(std_color_list[3])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')  
# for i,k in ('ee, m_{s} = 0.1 GeV, c#tau = 100 mm','ee, m_{s} = 0.1 GeV, c#tau = 500 mm'):
#     h[k] = create_TH1D( cscRechitCluster3YSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, binning=[50,0,200])
#     h[k].SetLineColor(std_color_list[4])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')      
  

#countAccep() 
 # def countAccep(): 
#         newSum=0
#         for i in range(0, len(sel_ev[k])-1):
#             if selev[k][i]==True:
#                 newSum+=1
#         return newSum
#    print(T.array('gLLP_csc'))
#    print(sel_ev[k])
#print(sel_ev[k])


# In[11]:


start_t = time.time()
c = rt.TCanvas('c','c', 800, 800)
h = {}



leg = rt.TLegend(0.8,.82,0.5,0.92)  # 1= left/right, 2= height/space out of legend vertical 3 = space of legend horiz
# 4 = vertical height 
leg.SetTextSize(0.022)
leg.SetBorderSize(0)
leg.SetTextFont(42)
#'ee, m_{s} = 0.1 GeV, c#tau = 100 mm',,'bb, m_{s} = 15 GeV, c#tau = 1000 mm'
keys= ('ee, m_{s} = 1 GeV, c#tau = 500 mm','#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm',
       'dd, m_{s} = 1 GeV, c#tau = 1000 mm','#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm', 'bb, m_{s} = 15 GeV, c#tau = 1000 mm')
#[2.62, 15.65, 12.08, 9.63,7.26, 5.50, 4.16], 
Acceptances= [[2.72, 15.71, 12.07, 9.49, 6.59, 3.74, 0.96], [2.35, 15.58,12.03,9.48,6.58, 3.70, 0.65],
              [2.37, 16.03,12.26,9.62,6.65, 3.74, 0.57],
              [2.43e-03, 4.98,11.44,14.63,16.24,14.15, 4.41],[7.40e-06, 0.94,4.41,7.95,12.77, 16.35, 6.52]]
RW= (10,100,200,300,500,1000,10000)
#print(k[5])
i=0
j=0
for k in keys:
    h[k] = create_TGraph( (RW), Acceptances[i] ,axis_title = ['ct [mm]', 'Acceptance (%)'])
    h[k].SetLineColor(std_color_list[j])
    leg.AddEntry(h[k], k)
    h[k].GetXaxis().SetLabelSize(0.04)
    h[k].GetXaxis().SetLimits(10, 10500)
    h[k].GetYaxis().SetRangeUser(0,21)
    h[k].Draw('AC' if i == 0 else 'C')
    h[k].SetLineWidth(3)
   
    i+=1
    if j==5:
        j+=1
    j+=1
    #make string of keys, iterate thru


leg.Draw()
c.SetLogx()
c.Draw()
c.SaveAs()
print(Acceptances[0])


# In[64]:


#if you want to calculate the efficiency of another variable, 
#say the xspread, then you would be able to use the same function CutAtWeight, but just a different lst, which contains the xpsread values
#Clustering efficiency wrt eta, energy, position(Z, R)


# In[7]:


start_t = time.time()
c = rt.TCanvas('c','c', 800, 800)
h = {}
leg = rt.TLegend(0.8,.82,0.5,0.92)  # 1= left/right, 2= height/space out of legend vertical 3 = space of legend horiz
# 4 = vertical height 
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
    hm = create_TH1D(cscRechitClusterEta[k].flatten(), axis_title=['Number of Rechits', 'Signal Efficiency'], name='hey', binning=[30,0,2.5])
    hb = create_TH1D((cscRechitClusterPhi[k]).flatten(), axis_title=['Number of Rechits', 'Signal Efficiency'], name= 'hey', binning=[30,0,2.5])
    pEff1 = rt.TEfficiency(hm,hb)
    pEff1.Draw()


leg.Draw()
#c.SetLogx()
c.Draw()
c.SaveAs()


#    print(len(gLLP_eta[k]),'len gllp')
#     print(len(sel_rechitcluster2[k]), 'len rechit2')
#     print(sel_rechitcluster2[k])
 #print(gLLP_eta[k], 'not flat')
   # print(gLLP_eta[k].flatten(), 'flat')


# In[11]:


#pretend he works

#can you plot ee and pi0 with the original 500mm samples, and dd, tautau, bb reweighted from 1000 to 500
#and maybe do it for all the plots you have in the slides, 
#and just put the new plots on the left, so we can see both plots in the same slides
#if possible, maybe try to use the same color for the decay modes, so its easier to compare

c = rt.TCanvas('c','c',800,800)
h = {}
leg = rt.TLegend(0.18,.73,0.35,0.94)  # 1= left/right, 2= height/space out of legend vertical 3 = space of legend horiz
# 4 = vertical height 
leg.SetTextSize(0.022)
leg.SetBorderSize(0)
leg.SetTextFont(42)
# for i, k in enumerate(tree.keys()): #works
#   #  print(k, len(cscRechitCluster3XSpread[k]))
#     h[k] = create_TH1D( cscRechitCluster3XSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, \
#                        binning=[50,0,100], weights= weight_ctau[k])
#     h[k].SetLineColor(std_color_list[i])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)

newN1='dd, m_{s} = 1 GeV, c#tau = 500 mm'
newN2='#tau#tau, m_{s} = 7 GeV, c#tau = 500 mm'
newN3='bb, m_{s} = 15 GeV, c#tau = 500 mm'

kNNEW=(newN1, newN2,newN3)
#     h[k].DrawNormalized('same hist')
new1='dd, m_{s} = 1 GeV, c#tau = 1000 mm'
new2='#tau#tau, m_{s} = 7 GeV, c#tau = 1000 mm'
new3='bb, m_{s} = 15 GeV, c#tau = 1000 mm'
kNEW=(new1, new2,new3)
i=4
j=0

for k in kNEW:
   # print(weight_ctau[k])
   # print('len avg station', len(cscRechitClusterAvgStation[k]), 'len weight', len(weight_ctau[k]))
    h[k] = create_TH1D(  cscRechitClusterEta[k], axis_title=['RechitCluster Eta', 'Events'], name=k, binning=[30,0,2.5], weights=weight_ctau[k])
   
    h[k].SetLineColor(std_color_list[i])
    leg.AddEntry(h[k], kNNEW[j])
    h[k].GetXaxis().SetLabelSize(0.04)
    h[k].DrawNormalized('same hist')
    j+=1
    i+=1

#key1= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau = 100 mm'
k2= '#pi^{0}#pi^{0}, m_{s} = 1 GeV, c#tau= 500 mm'
h[k2] = create_TH1D(  cscRechitClusterEta[k2], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k2, binning=[30,0,2.5])
h[k2].SetLineColor(std_color_list[3])
leg.AddEntry(h[k2], k2)
h[k2].GetXaxis().SetLabelSize(0.04)
h[k2].DrawNormalized('same hist')  

##newKey1= 'ee, m_{s} = 0.1 GeV, c#tau = 100 mm'
k3= 'ee, m_{s} = 0.1 GeV, c#tau = 500 mm'
newK= 'ee, m_{s} = 1 GeV, c#tau = 500 mm'
h[k3] = create_TH1D(   cscRechitClusterEta[k3], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k3, binning=[30,0,2.5])
h[k3].SetLineColor(std_color_list[1])
leg.AddEntry(h[k3], newK)
h[k3].GetXaxis().SetLabelSize(0.04)
h[k3].DrawNormalized('same hist')  
#you should sum the weights of events that pass the Nrechit cut and divide by the sum of all weights
# 100, 150, 200, 300, 400
#and calculate the percentage of signal events in each sample passes those cuts

#     h[k] = create_TH1D( cscRechitCluster3YSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, binning=[50,0,200])
#     h[k].SetLineColor(std_color_list[3])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')  
# for i,k in ('ee, m_{s} = 0.1 GeV, c#tau = 100 mm','ee, m_{s} = 0.1 GeV, c#tau = 500 mm'):
#     h[k] = create_TH1D( cscRechitCluster3YSpread[k], axis_title=['RechitCluster3 Y Spread [cm]', 'Events'], name=k, binning=[50,0,200])
#     h[k].SetLineColor(std_color_list[4])
#     leg.AddEntry(h[k], k)
#     h[k].GetXaxis().SetLabelSize(0.04)
#     h[k].DrawNormalized('same hist')      
  

leg.Draw()
c.SetLogy()
c.Draw()
c.SaveAs()


# In[ ]:




