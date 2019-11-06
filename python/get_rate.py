#!/usr/bin/env python 
from ROOT import *
import root_numpy as rtnp
import numpy as np
from matplotlib import pyplot as plt


#import tdrstyle

#set the tdr style
#tdrstyle.setTDRStyle()

f = TFile('/Users/cmorgoth/git/delayed_jet_analyzer/analyzer_PhaseIIMTDTDRAutumn18DR-PU200_NuGun.root')
tree = f.Get("L1EcalTimingAnalyzer/ecalTPTree")
mytree = rtnp.tree2array(tree)


fileout="RatesExampleMuon"

totalrate=2760*11246./1000  # bunches * frequency , /1000 to pass to kHz

entries=tree.GetEntries()
print "TOTAL RATE: ", totalrate

print entries

jet_pt   = mytree["caloJetPt"]
jet_eta  = mytree["caloJetEta"]
jet_time = mytree["CaloJetTime_t"]


#print jet_time
pass_evts = 0
pass_evts_nj = 0
time_thr = 1.0
pt_thr_off   = 50.

for pt,eta,time in zip(jet_pt,jet_eta,jet_time):
    #sel = np.logical_and(np.absolute(eta) < 1.44, pt > pt_thr)
    sel = np.absolute(eta) < 1.44
    s_pt   = pt[sel]
    s_eta  = eta[sel]
    s_time = time[sel]
    _pass = False
    _ctr  = 0
    for i_pt, i_eta, i_time, in zip(s_pt,s_eta,s_time):
        if np.absolute(i_eta) < 1.392:
            pt_thr = (pt_thr_off-12.7224)/1.2767
        else:
            pt_thr = (pt_thr_off-28.9858)/1.14625
        
        if i_pt > pt_thr and np.absolute(i_eta) < 1.44 and i_time > time_thr:
            _pass = True
            _ctr += 1
            #if 

    if _pass:
        pass_evts += 1.
        
    if _ctr >= 2:
        pass_evts_nj += 1.0


eff = pass_evts/entries
eff2 = pass_evts_nj/entries
print "eff(1jet), rate (kHz): ", eff, round(eff*totalrate,1)
print "eff(2jet), rate (kHz): ", eff2, round(eff2*totalrate,1)
