#!/usr/bin/env python
from ROOT import *
import root_numpy as rtnp
import numpy as np
from matplotlib import pyplot as plt


#import tdrstyle

#set the tdr style
#tdrstyle.setTDRStyle()

#f = TFile('/Users/cmorgoth/git/delayed_jet_analyzer/analyzer_PhaseIIMTDTDRAutumn18DR-PU200_NuGun.root')
#f = TFile('/Users/cmorgoth/NeutrinoGun_E_10GeV_all_all.root')



###############################
#############BKG###############
###############################
f = TFile('/Users/cmorgoth/NeutrinoGun_E_10GeV_all_all.root')
#f = TFile('/Users/cmorgoth/analyzer-dyll-4FEVT-jet_big.root')
tree = f.Get("L1EcalTimingAnalyzer/ecalTPTree")
mytree = rtnp.tree2array(tree)


fileout="RatesExampleMuon"

totalrate=2760*11246./1000.  # bunches * frequency , /1000 to pass to kHz

entries=tree.GetEntries()
print "TOTAL RATE: ", totalrate

print entries

jet_pt   = mytree["caloJetPt"]
jet_eta  = mytree["caloJetEta"]
jet_time = mytree["CaloJetTime_t"]


#print jet_time
pass_evts       = 0
pass_evts_2j    = 0
pass_evts_l     = []
pass_evts_2j_l  = []
rate_bkg_l      = []
rate_bkg_2j_l   = []
pt_thr_off_list = [20.,25.,30.,35.,40.,45.,50.,55.,60.,65.,70.,75.,80.,85.,90.,95.,100.]
time_thr        = 1.50
#pt_thr_off   = 40.

for pt_thr_off_i in pt_thr_off_list:
    print "=========", pt_thr_off_i
    pass_evts = 0
    pass_evts_2j = 0
    for pt,eta,time in zip(jet_pt,jet_eta,jet_time):##make event loop
        #sel = np.logical_and(np.absolute(eta) < 1.44, pt > pt_thr)
        sel = np.absolute(eta) < 1.44
        s_pt   = pt[sel]
        s_eta  = eta[sel]
        s_time = time[sel]
        _pass = False
        _ctr  = 0

        for i_pt, i_eta, i_time, in zip(s_pt,s_eta,s_time):
            if np.absolute(i_eta) < 1.392:
                pt_thr = (pt_thr_off_i-12.7224)/1.2767
            else:
                pt_thr = (pt_thr_off_i-28.9858)/1.14625

            if i_pt > pt_thr and np.absolute(i_eta) < 1.44 and i_time > time_thr:
                _pass = True
                _ctr += 1

        if _pass:
            pass_evts += 1.0

        if _ctr >= 2:
            pass_evts_2j += 1.0

    #print pass_evts/entries, pass_evts_nj/entries
    pass_evts_l.append(pass_evts/entries)
    rate_bkg_l.append(totalrate*pass_evts/entries)
    pass_evts_2j_l.append(pass_evts_2j/entries)
    rate_bkg_2j_l.append(totalrate*pass_evts_2j/entries)

###########################
#########SIGNAL############
###########################

f_signal = TFile('/Users/cmorgoth/RelValHiddenH_mH125_Phi50_ctau1E3_14TeV_L1_phaseII.root')
#f_signal = TFile('/Users/cmorgoth/analyzer-dyll-4FEVT-jet_big.root')
tree_signal = f_signal.Get("L1EcalTimingAnalyzer/ecalTPTree")
mytree_signal = rtnp.tree2array(tree_signal)


fileout="RatesExampleMuon"

totalrate=2760*11246./1000.  # bunches * frequency , /1000 to pass to kHz

entries_signal=tree_signal.GetEntries()
print "TOTAL RATE: ", totalrate

print entries_signal

jet_pt_signal   = mytree_signal["caloJetPt"]
jet_eta_signal  = mytree_signal["caloJetEta"]
jet_time_signal = mytree_signal["CaloJetTime_t"]


#print jet_time
pass_evts_signal = 0
pass_evts_l_signal = []
pass_evts_2j_l_signal = []
#pt_thr_off_list = [20.,25.,30.,35.,40.,45.,50.,55.,60.,65.,70.,75.,80.,85.,90.,95.,100.]
pass_evts_2j_signal = 0
#time_thr = 1.0
#pt_thr_off   = 40.

for pt_thr_off_i in pt_thr_off_list:
    print "=========", pt_thr_off_i
    pass_evts_signal = 0
    pass_evts_2j_signal = 0
    for pt,eta,time in zip(jet_pt_signal,jet_eta_signal,jet_time_signal):#loop over events
        #sel = np.logical_and(np.absolute(eta) < 1.44, pt > pt_thr)
        sel = np.absolute(eta) < 1.44
        s_pt   = pt[sel]
        s_eta  = eta[sel]
        s_time = time[sel]
        _pass = False
        _ctr  = 0

        for i_pt, i_eta, i_time, in zip(s_pt,s_eta,s_time):
            if np.absolute(i_eta) < 1.392:
                pt_thr = (pt_thr_off_i-12.7224)/1.2767
            else:
                pt_thr = (pt_thr_off_i-28.9858)/1.14625

            if i_pt > pt_thr and np.absolute(i_eta) < 1.44 and i_time > time_thr:
                _pass = True
                _ctr += 1

        if _pass:
            pass_evts_signal += 1.

        if _ctr >= 2:
            pass_evts_2j_signal += 1.0

    #print pass_evts/entries, pass_evts_nj/entries
    pass_evts_l_signal.append(pass_evts_signal/entries_signal)
    pass_evts_2j_l_signal.append(pass_evts_2j_signal/entries_signal)





#eff = pass_evts/entries
#eff2 = pass_evts_nj/entries

for pt_thres_off, eff_1j, eff_2j in zip(pt_thr_off_list,pass_evts_l,pass_evts_2j_l):
    print "============ offline pt-threshold ==========", pt_thres_off
    print "eff(1jet) rate (kHz): ", eff_1j, round(eff_1j*totalrate,1)
    print "eff(2jet) rate (kHz): ", eff_2j, round(eff_2j*totalrate,1)

for pt_thres_off, eff_1j, eff_2j in zip(pt_thr_off_list,pass_evts_l_signal,pass_evts_2j_l_signal):
    print "============ offline pt-threshold ==========", pt_thres_off
    print "eff(1jet) rate (kHz): ", eff_1j, round(eff_1j*totalrate,1)
    print "eff(2jet) rate (kHz): ", eff_2j, round(eff_2j*totalrate,1)


graph = TGraph(len(rate_bkg_l))
h_bkg_rate = TH1F("h_bkg_rate","bkg_rate", 20, 10, 110)
h_s_eff    = TH1F("h_s_eff","s_eff", 20, 10, 110)

ctr = 0
for s_eff, bkg_rate, pt in zip(pass_evts_l_signal,rate_bkg_l,pt_thr_off_list):
    graph.SetPoint(ctr, s_eff,bkg_rate)
    bin = h_bkg_rate.FindBin(pt)
    h_bkg_rate.SetBinContent(bin,bkg_rate)
    h_s_eff.SetBinContent(bin,s_eff)
    ctr += 1

my_outFile = TFile("my_eff_file.root", "recreate")
graph.Write("eff_graph")
h_bkg_rate.Write("bkg_rate")
h_s_eff.Write("s_eff")
