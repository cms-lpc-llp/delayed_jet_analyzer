//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sat Sep 14 16:15:03 2019 by ROOT version 6.13/02
// from TTree llp/selected AOD information for llp analyses
// found on file: llp_ntupler_ggHdddd_M55_1000mm.root
//////////////////////////////////////////////////////////

#ifndef llp_h
#define llp_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include "vector"

class llp {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Bool_t          isData;
   Int_t           nPV;
   UInt_t          runNum;
   UInt_t          nSlimmedSecondV;
   UInt_t          lumiNum;
   UInt_t          eventNum;
   UInt_t          eventTime;
   Float_t         pvX;
   Float_t         pvY;
   Float_t         pvZ;
   Float_t         fixedGridRhoAll;
   Float_t         fixedGridRhoFastjetAll;
   Float_t         fixedGridRhoFastjetAllCalo;
   Float_t         fixedGridRhoFastjetCentralCalo;
   Float_t         fixedGridRhoFastjetCentralChargedPileUp;
   Float_t         fixedGridRhoFastjetCentralNeutral;
   Int_t           nPVAll;
   Float_t         pvAllX[1];   //[nPVAll]
   Float_t         pvAllY[1];   //[nPVAll]
   Float_t         pvAllZ[1];   //[nPVAll]
   Float_t         pvAllLogSumPtSq[1];   //[nPVAll]
   Float_t         pvAllSumPx[1];   //[nPVAll]
   Float_t         pvAllSumPy[1];   //[nPVAll]
   Int_t           nPVTracks;
   Float_t         pvTrackPt[1];   //[nPVTracks]
   Float_t         pvTrackEta[1];   //[nPVTracks]
   Float_t         pvTrackPhi[1];   //[nPVTracks]
   Int_t           nBunchXing;
   Int_t           BunchXing[16];   //[nBunchXing]
   Int_t           nPU[16];   //[nBunchXing]
   Float_t         nPUmean[16];   //[nBunchXing]
   Int_t           nMuons;
   Float_t         muonE[10];   //[nMuons]
   Float_t         muonPt[10];   //[nMuons]
   Float_t         muonEta[10];   //[nMuons]
   Float_t         muonPhi[10];   //[nMuons]
   Int_t           muonCharge[10];   //[nMuons]
   Bool_t          muonIsLoose[10];   //[nMuons]
   Bool_t          muonIsMedium[10];   //[nMuons]
   Bool_t          muonIsTight[10];   //[nMuons]
   Float_t         muon_d0[10];   //[nMuons]
   Float_t         muon_dZ[10];   //[nMuons]
   Float_t         muon_ip3d[10];   //[nMuons]
   Float_t         muon_ip3dSignificance[10];   //[nMuons]
   UInt_t          muonType[10];   //[nMuons]
   UInt_t          muonQuality[10];   //[nMuons]
   Float_t         muon_pileupIso[10];   //[nMuons]
   Float_t         muon_chargedIso[10];   //[nMuons]
   Float_t         muon_photonIso[10];   //[nMuons]
   Float_t         muon_neutralHadIso[10];   //[nMuons]
   Float_t         muon_ptrel[10];   //[nMuons]
   Float_t         muon_chargedMiniIso[10];   //[nMuons]
   Float_t         muon_photonAndNeutralHadronMiniIso[10];   //[nMuons]
   Float_t         muon_chargedPileupMiniIso[10];   //[nMuons]
   Float_t         muon_activityMiniIsoAnnulus[10];   //[nMuons]
   Bool_t          muon_passSingleMuTagFilter[10];   //[nMuons]
   Bool_t          muon_passHLTFilter[10][100];   //[nMuons]
   Float_t         muon_validFractionTrackerHits[10];   //[nMuons]
   Bool_t          muon_isGlobal[10];   //[nMuons]
   Float_t         muon_normChi2[10];   //[nMuons]
   Float_t         muon_chi2LocalPosition[10];   //[nMuons]
   Float_t         muon_kinkFinder[10];   //[nMuons]
   Float_t         muon_segmentCompatability[10];   //[nMuons]
   Bool_t          muonIsICHEPMedium[10];   //[nMuons]
   Int_t           nElectrons;
   Float_t         eleE[5];   //[nElectrons]
   Float_t         elePt[5];   //[nElectrons]
   Float_t         eleEta[5];   //[nElectrons]
   Float_t         elePhi[5];   //[nElectrons]
   Float_t         eleCharge[5];   //[nElectrons]
   Float_t         eleEta_SC[5];   //[nElectrons]
   Float_t         eleSigmaIetaIeta[5];   //[nElectrons]
   Float_t         eleFull5x5SigmaIetaIeta[5];   //[nElectrons]
   Float_t         eleR9[5];   //[nElectrons]
   Float_t         ele_dEta[5];   //[nElectrons]
   Float_t         ele_dPhi[5];   //[nElectrons]
   Float_t         ele_HoverE[5];   //[nElectrons]
   Float_t         ele_d0[5];   //[nElectrons]
   Float_t         ele_dZ[5];   //[nElectrons]
   Float_t         ele_ip3d[5];   //[nElectrons]
   Float_t         ele_ip3dSignificance[5];   //[nElectrons]
   Float_t         ele_pileupIso[5];   //[nElectrons]
   Float_t         ele_chargedIso[5];   //[nElectrons]
   Float_t         ele_photonIso[5];   //[nElectrons]
   Float_t         ele_neutralHadIso[5];   //[nElectrons]
   Int_t           ele_MissHits[5];   //[nElectrons]
   Bool_t          ele_PassConvVeto[5];   //[nElectrons]
   Float_t         ele_OneOverEminusOneOverP[5];   //[nElectrons]
   Float_t         ele_IDMVAGeneralPurpose[5];   //[nElectrons]
   Int_t           ele_IDMVACategoryGeneralPurpose[5];   //[nElectrons]
   Float_t         ele_IDMVAHZZ[5];   //[nElectrons]
   Int_t           ele_IDMVACategoryHZZ[5];   //[nElectrons]
   Float_t         ele_RegressionE[5];   //[nElectrons]
   Float_t         ele_CombineP4[5];   //[nElectrons]
   Float_t         ele_ptrel[5];   //[nElectrons]
   Float_t         ele_chargedMiniIso[5];   //[nElectrons]
   Float_t         ele_photonAndNeutralHadronMiniIso[5];   //[nElectrons]
   Float_t         ele_chargedPileupMiniIso[5];   //[nElectrons]
   Float_t         ele_activityMiniIsoAnnulus[5];   //[nElectrons]
   Bool_t          ele_passSingleEleTagFilter[5];   //[nElectrons]
   Bool_t          ele_passTPOneTagFilter[5];   //[nElectrons]
   Bool_t          ele_passTPTwoTagFilter[5];   //[nElectrons]
   Bool_t          ele_passTPOneProbeFilter[5];   //[nElectrons]
   Bool_t          ele_passTPTwoProbeFilter[5];   //[nElectrons]
   Bool_t          ele_passHLTFilter[5][100];   //[nElectrons]
   Int_t           nTaus;
   Float_t         tauE[1];   //[nTaus]
   Float_t         tauPt[1];   //[nTaus]
   Float_t         tauEta[1];   //[nTaus]
   Float_t         tauPhi[1];   //[nTaus]
   Bool_t          tau_IsLoose[1];   //[nTaus]
   Bool_t          tau_IsMedium[1];   //[nTaus]
   Bool_t          tau_IsTight[1];   //[nTaus]
   Bool_t          tau_passEleVetoLoose[1];   //[nTaus]
   Bool_t          tau_passEleVetoMedium[1];   //[nTaus]
   Bool_t          tau_passEleVetoTight[1];   //[nTaus]
   Bool_t          tau_passMuVetoLoose[1];   //[nTaus]
   Bool_t          tau_passMuVetoMedium[1];   //[nTaus]
   Bool_t          tau_passMuVetoTight[1];   //[nTaus]
   UInt_t          tau_ID[1];   //[nTaus]
   Float_t         tau_combinedIsoDeltaBetaCorr3Hits[1];   //[nTaus]
   Float_t         tau_chargedIsoPtSum[1];   //[nTaus]
   Float_t         tau_neutralIsoPtSum[1];   //[nTaus]
   Float_t         tau_puCorrPtSum[1];   //[nTaus]
   Float_t         tau_eleVetoMVA[1];   //[nTaus]
   Int_t           tau_eleVetoCategory[1];   //[nTaus]
   Float_t         tau_muonVetoMVA[1];   //[nTaus]
   Float_t         tau_isoMVAnewDMwLT[1];   //[nTaus]
   Float_t         tau_isoMVAnewDMwoLT[1];   //[nTaus]
   Float_t         tau_leadCandPt[1];   //[nTaus]
   Int_t           tau_leadCandID[1];   //[nTaus]
   Float_t         tau_leadChargedHadrCandPt[1];   //[nTaus]
   Int_t           tau_leadChargedHadrCandID[1];   //[nTaus]
   UInt_t          nIsoPFCandidates;
   Float_t         isoPFCandidatePt[1];   //[nIsoPFCandidates]
   Float_t         isoPFCandidateEta[1];   //[nIsoPFCandidates]
   Float_t         isoPFCandidatePhi[1];   //[nIsoPFCandidates]
   Float_t         isoPFCandidateIso04[1];   //[nIsoPFCandidates]
   Float_t         isoPFCandidateD0[1];   //[nIsoPFCandidates]
   Int_t           isoPFCandidatePdgId[1];   //[nIsoPFCandidates]
   Int_t           nPhotons;
   Int_t           nPhotons_overlap;
   Float_t         phoE[1];   //[nPhotons]
   Float_t         phoPt[1];   //[nPhotons]
   Float_t         phoEta[1];   //[nPhotons]
   Float_t         phoPhi[1];   //[nPhotons]
   Float_t         phoSigmaIetaIeta[1];   //[nPhotons]
   Float_t         phoFull5x5SigmaIetaIeta[1];   //[nPhotons]
   Float_t         phoR9[1];   //[nPhotons]
   Float_t         pho_sminor[1];   //[nPhotons]
   Float_t         pho_smajor[1];   //[nPhotons]
   Float_t         pho_HoverE[1];   //[nPhotons]
   Float_t         pho_sumChargedHadronPtAllVertices[1][1000];   //[nPhotons]
   Float_t         pho_sumChargedHadronPt[1];   //[nPhotons]
   Float_t         pho_sumNeutralHadronEt[1];   //[nPhotons]
   Float_t         pho_sumPhotonEt[1];   //[nPhotons]
   Float_t         pho_ecalPFClusterIso[1];   //[nPhotons]
   Float_t         pho_hcalPFClusterIso[1];   //[nPhotons]
   Float_t         pho_trkSumPtHollowConeDR03[1];   //[nPhotons]
   Float_t         pho_sumWorstVertexChargedHadronPt[1];   //[nPhotons]
   Float_t         pho_pfIsoChargedHadronIso[1];   //[nPhotons]
   Float_t         pho_pfIsoChargedHadronIsoWrongVtx[1];   //[nPhotons]
   Float_t         pho_pfIsoNeutralHadronIso[1];   //[nPhotons]
   Float_t         pho_pfIsoPhotonIso[1];   //[nPhotons]
   Float_t         pho_pfIsoModFrixione[1];   //[nPhotons]
   Float_t         pho_pfIsoSumPUPt[1];   //[nPhotons]
   Bool_t          pho_isConversion[1];   //[nPhotons]
   Bool_t          pho_passEleVeto[1];   //[nPhotons]
   Float_t         pho_RegressionE[1];   //[nPhotons]
   Float_t         pho_RegressionEUncertainty[1];   //[nPhotons]
   Float_t         pho_IDMVA[1];   //[nPhotons]
   Float_t         pho_superClusterEnergy[1];   //[nPhotons]
   Float_t         pho_superClusterRawEnergy[1];   //[nPhotons]
   Float_t         pho_superClusterEta[1];   //[nPhotons]
   Float_t         pho_superClusterPhi[1];   //[nPhotons]
   Float_t         pho_superClusterX[1];   //[nPhotons]
   Float_t         pho_superClusterY[1];   //[nPhotons]
   Float_t         pho_superClusterZ[1];   //[nPhotons]
   Bool_t          pho_hasPixelSeed[1];   //[nPhotons]
   Bool_t          pho_passHLTFilter[1][100];   //[nPhotons]
   Int_t           pho_convType[1];   //[nPhotons]
   Float_t         pho_convTrkZ[1];   //[nPhotons]
   Float_t         pho_convTrkClusZ[1];   //[nPhotons]
   Float_t         pho_vtxSumPx[1][1000];   //[nPhotons]
   Float_t         pho_vtxSumPy[1][1000];   //[nPhotons]
   Bool_t          pho_isStandardPhoton[1];   //[nPhotons]
   Float_t         pho_seedRecHitSwitchToGain6[1];   //[nPhotons]
   Float_t         pho_seedRecHitSwitchToGain1[1];   //[nPhotons]
   Float_t         pho_anyRecHitSwitchToGain6[1];   //[nPhotons]
   Float_t         pho_anyRecHitSwitchToGain1[1];   //[nPhotons]
   Int_t           nCsc;
   Float_t         cscPhi[120];   //[nCsc]
   Float_t         cscEta[120];   //[nCsc]
   Float_t         cscX[120];   //[nCsc]
   Float_t         cscY[120];   //[nCsc]
   Float_t         cscZ[120];   //[nCsc]
   Float_t         cscNRecHits[120];   //[nCsc]
   Float_t         cscNRecHits_flag[120];   //[nCsc]
   Float_t         cscT[120];   //[nCsc]
   Float_t         cscChi2[120];   //[nCsc]
   Int_t           nRpc;
   Float_t         rpcPhi[113];   //[nRpc]
   Float_t         rpcEta[113];   //[nRpc]
   Float_t         rpcX[113];   //[nRpc]
   Float_t         rpcY[113];   //[nRpc]
   Float_t         rpcZ[113];   //[nRpc]
   Float_t         rpcT[113];   //[nRpc]
   Float_t         rpcTError[113];   //[nRpc]
   Int_t           nDt;
   Float_t         dtPhi[195];   //[nDt]
   Float_t         dtEta[195];   //[nDt]
   Float_t         dtX[195];   //[nDt]
   Float_t         dtY[195];   //[nDt]
   Float_t         dtZ[195];   //[nDt]
   Float_t         dtDirX[195];   //[nDt]
   Float_t         dtDirY[195];   //[nDt]
   Float_t         dtDirZ[195];   //[nDt]
   Float_t         dtT[195];   //[nDt]
   Float_t         dtTError[195];   //[nDt]
   Int_t           nRechits;
   Float_t         ecalRechit_Eta[1];   //[nRechits]
   Float_t         ecalRechit_Phi[1];   //[nRechits]
   Float_t         ecalRechit_E[1];   //[nRechits]
   Float_t         ecalRechit_T[1];   //[nRechits]
   Float_t         ecalRechit_E_Error[1];   //[nRechits]
   Float_t         ecalRechit_T_Error[1];   //[nRechits]
   Bool_t          ecalRechit_kSaturatedflag[1];   //[nRechits]
   Bool_t          ecalRechit_kLeadingEdgeRecoveredflag[1];   //[nRechits]
   Bool_t          ecalRechit_kPoorRecoflag[1];   //[nRechits]
   Bool_t          ecalRechit_kWeirdflag[1];   //[nRechits]
   Bool_t          ecalRechit_kDiWeirdflag[1];   //[nRechits]
   Int_t           nJets;
   Float_t         jetE[20];   //[nJets]
   Float_t         jetPt[20];   //[nJets]
   Float_t         jetEta[20];   //[nJets]
   Float_t         jetEt[20];   //[nJets]
   Float_t         jetPhi[20];   //[nJets]
   Float_t         jetCSV[20];   //[nJets]
   Float_t         jetCISV[20];   //[nJets]
   Float_t         jetProbb[20];   //[nJets]
   Float_t         jetProbc[20];   //[nJets]
   Float_t         jetProbudsg[20];   //[nJets]
   Float_t         jetProbbb[20];   //[nJets]
   Float_t         jetMass[20];   //[nJets]
   Float_t         jetJetArea[20];   //[nJets]
   Float_t         jetPileupE[20];   //[nJets]
   Float_t         jetPileupId[20];   //[nJets]
   Int_t           jetPileupIdFlag[20];   //[nJets]
   Bool_t          jetPassIDLoose[20];   //[nJets]
   Bool_t          jetPassIDTight[20];   //[nJets]
   Bool_t          jetPassMuFrac[20];   //[nJets]
   Bool_t          jetPassEleFrac[20];   //[nJets]
   Int_t           jetPartonFlavor[20];   //[nJets]
   Int_t           jetHadronFlavor[20];   //[nJets]
   Float_t         jetChargedEMEnergyFraction[20];   //[nJets]
   Float_t         jetNeutralEMEnergyFraction[20];   //[nJets]
   Float_t         jetChargedHadronEnergyFraction[20];   //[nJets]
   Float_t         jetNeutralHadronEnergyFraction[20];   //[nJets]
   Float_t         jetMuonEnergyFraction[20];   //[nJets]
   Float_t         jetHOEnergyFraction[20];   //[nJets]
   Float_t         jetHFHadronEnergyFraction[20];   //[nJets]
   Float_t         jetHFEMEnergyFraction[20];   //[nJets]
   Float_t         jetAllMuonPt[20];   //[nJets]
   Float_t         jetAllMuonEta[20];   //[nJets]
   Float_t         jetAllMuonPhi[20];   //[nJets]
   Float_t         jetAllMuonM[20];   //[nJets]
   Float_t         jetPtWeightedDZ[20];   //[nJets]
   Int_t           jetNRechits[20];   //[nJets]
   Float_t         jetRechitE[20];   //[nJets]
   Float_t         jetRechitT[20];   //[nJets]
   Float_t         jetRechitT_rms[20];   //[nJets]
   Float_t         jetRechitE_Error[20];   //[nJets]
   Float_t         jetRechitT_Error[20];   //[nJets]
   Float_t         jetAlphaMax[20];   //[nJets]
   Float_t         jetBetaMax[20];   //[nJets]
   Float_t         jetGammaMax_ET[20];   //[nJets]
   Float_t         jetGammaMax_EM[20];   //[nJets]
   Float_t         jetGammaMax_Hadronic[20];   //[nJets]
   Float_t         jetGammaMax[20];   //[nJets]
   Float_t         jetPtAllTracks[20];   //[nJets]
   Float_t         jetPtAllPVTracks[20];   //[nJets]
   Float_t         jetMedianTheta2D[20];   //[nJets]
   Float_t         jetMedianIP[20];   //[nJets]
   Float_t         jetMinDeltaRAllTracks[20];   //[nJets]
   Float_t         jetMinDeltaRPVTracks[20];   //[nJets]
   Float_t         jet_sig_et1[20];   //[nJets]
   Float_t         jet_sig_et2[20];   //[nJets]
   Float_t         jet_energy_frac[20];   //[nJets]
   Bool_t          jet_matched[20];   //[nJets]
   Int_t           nCaloJets;
   Float_t         calojetE[11];   //[nCaloJets]
   Float_t         calojetEt[11];   //[nCaloJets]
   Float_t         calojetPt[11];   //[nCaloJets]
   Float_t         calojetEta[11];   //[nCaloJets]
   Float_t         calojetPhi[11];   //[nCaloJets]
   Float_t         calojetMass[11];   //[nCaloJets]
   Float_t         calojetJetArea[11];   //[nCaloJets]
   Float_t         calojetPileupE[11];   //[nCaloJets]
   Float_t         calojetPileupId[11];   //[nCaloJets]
   Int_t           calojetPileupIdFlag[11];   //[nCaloJets]
   Bool_t          calojetPassIDLoose[11];   //[nCaloJets]
   Bool_t          calojetPassIDTight[11];   //[nCaloJets]
   Int_t           calojetNRechits[11];   //[nCaloJets]
   Float_t         calojetRechitE[11];   //[nCaloJets]
   Float_t         calojetRechitT[11];   //[nCaloJets]
   Float_t         calojetRechitT_rms[11];   //[nCaloJets]
   Float_t         calojetAlphaMax[11];   //[nCaloJets]
   Float_t         calojetBetaMax[11];   //[nCaloJets]
   Float_t         calojetGammaMax_ET[11];   //[nCaloJets]
   Float_t         calojetGammaMax_EM[11];   //[nCaloJets]
   Float_t         calojetGammaMax_Hadronic[11];   //[nCaloJets]
   Float_t         calojetGammaMax[11];   //[nCaloJets]
   Float_t         calojet_HadronicEnergyFraction[11];   //[nCaloJets]
   Float_t         calojet_EMEnergyFraction[11];   //[nCaloJets]
   Float_t         calojetPtAllTracks[11];   //[nCaloJets]
   Float_t         calojetPtAllPVTracks[11];   //[nCaloJets]
   Float_t         calojetMedianTheta2D[11];   //[nCaloJets]
   Float_t         calojetMedianIP[11];   //[nCaloJets]
   Float_t         calojetMinDeltaRAllTracks[11];   //[nCaloJets]
   Float_t         calojetMinDeltaRPVTracks[11];   //[nCaloJets]
   UInt_t          nFatJets;
   Float_t         fatJetE[1];   //[nFatJets]
   Float_t         fatJetPt[1];   //[nFatJets]
   Float_t         fatJetEta[1];   //[nFatJets]
   Float_t         fatJetPhi[1];   //[nFatJets]
   Float_t         fatJetCorrectedPt[1];   //[nFatJets]
   Float_t         fatJetPrunedM[1];   //[nFatJets]
   Float_t         fatJetTrimmedM[1];   //[nFatJets]
   Float_t         fatJetFilteredM[1];   //[nFatJets]
   Float_t         fatJetSoftDropM[1];   //[nFatJets]
   Float_t         fatJetCorrectedSoftDropM[1];   //[nFatJets]
   Float_t         fatJetUncorrectedSoftDropM[1];   //[nFatJets]
   Float_t         fatJetTau1[1];   //[nFatJets]
   Float_t         fatJetTau2[1];   //[nFatJets]
   Float_t         fatJetTau3[1];   //[nFatJets]
   Float_t         fatJetMaxSubjetCSV[1];   //[nFatJets]
   Bool_t          fatJetPassIDLoose[1];   //[nFatJets]
   Bool_t          fatJetPassIDTight[1];   //[nFatJets]
   Float_t         metPt;
   Float_t         metPhi;
   Float_t         sumMET;
   Float_t         metType0Pt;
   Float_t         metType0Phi;
   Float_t         metType1Pt_raw;
   Float_t         metType1Pt;
   Float_t         metType1Px;
   Float_t         metType1Py;
   Float_t         metType1Eta;
   Float_t         metType1Phi;
   Float_t         metType1Phi_raw;
   Float_t         metType0Plus1Pt;
   Float_t         metType0Plus1Phi;
   Float_t         metNoHFPt;
   Float_t         metNoHFPhi;
   Float_t         metPuppiPt;
   Float_t         metPuppiPhi;
   Float_t         metCaloPt;
   Float_t         metCaloPhi;
   Bool_t          Flag_HBHENoiseFilter;
   Bool_t          Flag_HBHETightNoiseFilter;
   Bool_t          Flag_HBHEIsoNoiseFilter;
   Bool_t          Flag_badChargedCandidateFilter;
   Bool_t          Flag_badMuonFilter;
   Bool_t          Flag_badGlobalMuonFilter;
   Bool_t          Flag_duplicateMuonFilter;
   Bool_t          Flag_CSCTightHaloFilter;
   Bool_t          Flag_hcalLaserEventFilter;
   Bool_t          Flag_EcalDeadCellTriggerPrimitiveFilter;
   Bool_t          Flag_EcalDeadCellBoundaryEnergyFilter;
   Bool_t          Flag_goodVertices;
   Bool_t          Flag_trackingFailureFilter;
   Bool_t          Flag_eeBadScFilter;
   Bool_t          Flag_ecalLaserCorrFilter;
   Bool_t          Flag_trkPOGFilters;
   Bool_t          Flag_trkPOG_manystripclus53X;
   Bool_t          Flag_trkPOG_toomanystripclus53X;
   Bool_t          Flag_trkPOG_logErrorTooManyClusters;
   Bool_t          Flag_BadPFMuonFilter;
   Bool_t          Flag_BadChargedCandidateFilter;
   Bool_t          Flag_ecalBadCalibFilter;
   Bool_t          Flag_METFilters;
   Bool_t          HLTDecision[602];
   Int_t           HLTPrescale[602];
   Int_t           nGenJets;
   Float_t         genJetE[80];   //[nGenJets]
   Float_t         genJetPt[80];   //[nGenJets]
   Float_t         genJetEta[80];   //[nGenJets]
   Float_t         genJetPhi[80];   //[nGenJets]
   Float_t         genMetPtCalo;
   Float_t         genMetPhiCalo;
   Float_t         genMetPtTrue;
   Float_t         genMetPhiTrue;
   Float_t         genVertexX;
   Float_t         genVertexY;
   Float_t         genVertexZ;
   Float_t         genVertexT;
   Float_t         genWeight;
   UInt_t          genSignalProcessID;
   Float_t         genQScale;
   Float_t         genAlphaQCD;
   Float_t         genAlphaQED;
   std::vector<float>   *scaleWeights;
   std::vector<float>   *pdfWeights;
   std::vector<float>   *alphasWeights;
   Int_t           nGenParticle;
   Int_t           gParticleMotherId[581];   //[nGenParticle]
   Int_t           gParticleMotherIndex[581];   //[nGenParticle]
   Int_t           gParticleId[581];   //[nGenParticle]
   Int_t           gParticleStatus[581];   //[nGenParticle]
   Float_t         gParticleE[581];   //[nGenParticle]
   Float_t         gParticlePt[581];   //[nGenParticle]
   Float_t         gParticlePx[581];   //[nGenParticle]
   Float_t         gParticlePy[581];   //[nGenParticle]
   Float_t         gParticlePz[581];   //[nGenParticle]
   Float_t         gParticleEta[581];   //[nGenParticle]
   Float_t         gParticlePhi[581];   //[nGenParticle]
   Float_t         gParticleProdVertexX[581];   //[nGenParticle]
   Float_t         gParticleProdVertexY[581];   //[nGenParticle]
   Float_t         gParticleProdVertexZ[581];   //[nGenParticle]
   Float_t         gLLP_prod_vertex_x[2];
   Float_t         gLLP_prod_vertex_y[2];
   Float_t         gLLP_prod_vertex_z[2];
   Float_t         gLLP_decay_vertex_x[2];
   Float_t         gLLP_decay_vertex_y[2];
   Float_t         gLLP_decay_vertex_z[2];
   Float_t         gLLP_beta[2];
   Float_t         gLLP_e[2];
   Float_t         gLLP_pt[2];
   Float_t         gLLP_eta[2];
   Float_t         gLLP_phi[2];
   Float_t         gLLP_travel_time[2];
   Float_t         gLLP_daughter_travel_time[4];
   Float_t         gLLP_daughter_pt[4];
   Float_t         gLLP_daughter_eta[4];
   Float_t         gLLP_daughter_phi[4];
   Float_t         gLLP_daughter_eta_ecalcorr[4];
   Float_t         gLLP_daughter_phi_ecalcorr[4];
   Float_t         gLLP_daughter_e[4];
   Float_t         photon_travel_time[4];
   Float_t         gen_time[4];
   Float_t         gen_time_pv[4];
   Float_t         gLLP_min_delta_r_match_calojet[4];
   UInt_t          gLLP_daughter_match_calojet_index[4];
   UInt_t          gLLP_daughter_match_jet_index[4];
   Float_t         gLLP_min_delta_r_match_jet[4];

   // List of branches
   TBranch        *b_isData;   //!
   TBranch        *b_nPV;   //!
   TBranch        *b_runNum;   //!
   TBranch        *b_nSlimmedSecondV;   //!
   TBranch        *b_lumiNum;   //!
   TBranch        *b_eventNum;   //!
   TBranch        *b_eventTime;   //!
   TBranch        *b_pvX;   //!
   TBranch        *b_pvY;   //!
   TBranch        *b_pvZ;   //!
   TBranch        *b_fixedGridRhoAll;   //!
   TBranch        *b_fixedGridRhoFastjetAll;   //!
   TBranch        *b_fixedGridRhoFastjetAllCalo;   //!
   TBranch        *b_fixedGridRhoFastjetCentralCalo;   //!
   TBranch        *b_fixedGridRhoFastjetCentralChargedPileUp;   //!
   TBranch        *b_fixedGridRhoFastjetCentralNeutral;   //!
   TBranch        *b_nPVAll;   //!
   TBranch        *b_pvAllX;   //!
   TBranch        *b_pvAllY;   //!
   TBranch        *b_pvAllZ;   //!
   TBranch        *b_pvAllLogSumPtSq;   //!
   TBranch        *b_pvAllSumPx;   //!
   TBranch        *b_pvAllSumPy;   //!
   TBranch        *b_nPVTracks;   //!
   TBranch        *b_pvTrackPt;   //!
   TBranch        *b_pvTrackEta;   //!
   TBranch        *b_pvTrackPhi;   //!
   TBranch        *b_nBunchXing;   //!
   TBranch        *b_BunchXing;   //!
   TBranch        *b_nPU;   //!
   TBranch        *b_nPUmean;   //!
   TBranch        *b_nMuons;   //!
   TBranch        *b_muonE;   //!
   TBranch        *b_muonPt;   //!
   TBranch        *b_muonEta;   //!
   TBranch        *b_muonPhi;   //!
   TBranch        *b_muonCharge;   //!
   TBranch        *b_muonIsLoose;   //!
   TBranch        *b_muonIsMedium;   //!
   TBranch        *b_muonIsTight;   //!
   TBranch        *b_muon_d0;   //!
   TBranch        *b_muon_dZ;   //!
   TBranch        *b_muon_ip3d;   //!
   TBranch        *b_muon_ip3dSignificance;   //!
   TBranch        *b_muonType;   //!
   TBranch        *b_muonQuality;   //!
   TBranch        *b_muon_pileupIso;   //!
   TBranch        *b_muon_chargedIso;   //!
   TBranch        *b_muon_photonIso;   //!
   TBranch        *b_muon_neutralHadIso;   //!
   TBranch        *b_muon_ptrel;   //!
   TBranch        *b_muon_chargedMiniIso;   //!
   TBranch        *b_muon_photonAndNeutralHadronMiniIso;   //!
   TBranch        *b_muon_chargedPileupMiniIso;   //!
   TBranch        *b_muon_activityMiniIsoAnnulus;   //!
   TBranch        *b_muon_passSingleMuTagFilter;   //!
   TBranch        *b_muon_passHLTFilter;   //!
   TBranch        *b_muon_validFractionTrackerHits;   //!
   TBranch        *b_muon_isGlobal;   //!
   TBranch        *b_muon_normChi2;   //!
   TBranch        *b_muon_chi2LocalPosition;   //!
   TBranch        *b_muon_kinkFinder;   //!
   TBranch        *b_muon_segmentCompatability;   //!
   TBranch        *b_muonIsICHEPMedium;   //!
   TBranch        *b_nElectrons;   //!
   TBranch        *b_eleE;   //!
   TBranch        *b_elePt;   //!
   TBranch        *b_eleEta;   //!
   TBranch        *b_elePhi;   //!
   TBranch        *b_eleCharge;   //!
   TBranch        *b_eleEta_SC;   //!
   TBranch        *b_eleSigmaIetaIeta;   //!
   TBranch        *b_eleFull5x5SigmaIetaIeta;   //!
   TBranch        *b_eleR9;   //!
   TBranch        *b_ele_dEta;   //!
   TBranch        *b_ele_dPhi;   //!
   TBranch        *b_ele_HoverE;   //!
   TBranch        *b_ele_d0;   //!
   TBranch        *b_ele_dZ;   //!
   TBranch        *b_ele_ip3d;   //!
   TBranch        *b_ele_ip3dSignificance;   //!
   TBranch        *b_ele_pileupIso;   //!
   TBranch        *b_ele_chargedIso;   //!
   TBranch        *b_ele_photonIso;   //!
   TBranch        *b_ele_neutralHadIso;   //!
   TBranch        *b_ele_MissHits;   //!
   TBranch        *b_ele_PassConvVeto;   //!
   TBranch        *b_ele_OneOverEminusOneOverP;   //!
   TBranch        *b_ele_IDMVAGeneralPurpose;   //!
   TBranch        *b_ele_IDMVACategoryGeneralPurpose;   //!
   TBranch        *b_ele_IDMVAHZZ;   //!
   TBranch        *b_ele_IDMVACategoryHZZ;   //!
   TBranch        *b_ele_RegressionE;   //!
   TBranch        *b_ele_CombineP4;   //!
   TBranch        *b_ele_ptrel;   //!
   TBranch        *b_ele_chargedMiniIso;   //!
   TBranch        *b_ele_photonAndNeutralHadronMiniIso;   //!
   TBranch        *b_ele_chargedPileupMiniIso;   //!
   TBranch        *b_ele_activityMiniIsoAnnulus;   //!
   TBranch        *b_ele_passSingleEleTagFilter;   //!
   TBranch        *b_ele_passTPOneTagFilter;   //!
   TBranch        *b_ele_passTPTwoTagFilter;   //!
   TBranch        *b_ele_passTPOneProbeFilter;   //!
   TBranch        *b_ele_passTPTwoProbeFilter;   //!
   TBranch        *b_ele_passHLTFilter;   //!
   TBranch        *b_nTaus;   //!
   TBranch        *b_tauE;   //!
   TBranch        *b_tauPt;   //!
   TBranch        *b_tauEta;   //!
   TBranch        *b_tauPhi;   //!
   TBranch        *b_tau_IsLoose;   //!
   TBranch        *b_tau_IsMedium;   //!
   TBranch        *b_tau_IsTight;   //!
   TBranch        *b_tau_passEleVetoLoose;   //!
   TBranch        *b_tau_passEleVetoMedium;   //!
   TBranch        *b_tau_passEleVetoTight;   //!
   TBranch        *b_tau_passMuVetoLoose;   //!
   TBranch        *b_tau_passMuVetoMedium;   //!
   TBranch        *b_tau_passMuVetoTight;   //!
   TBranch        *b_tau_ID;   //!
   TBranch        *b_tau_combinedIsoDeltaBetaCorr3Hits;   //!
   TBranch        *b_tau_chargedIsoPtSum;   //!
   TBranch        *b_tau_neutralIsoPtSum;   //!
   TBranch        *b_tau_puCorrPtSum;   //!
   TBranch        *b_tau_eleVetoMVA;   //!
   TBranch        *b_tau_eleVetoCategory;   //!
   TBranch        *b_tau_muonVetoMVA;   //!
   TBranch        *b_tau_isoMVAnewDMwLT;   //!
   TBranch        *b_tau_isoMVAnewDMwoLT;   //!
   TBranch        *b_tau_leadCandPt;   //!
   TBranch        *b_tau_leadCandID;   //!
   TBranch        *b_tau_leadChargedHadrCandPt;   //!
   TBranch        *b_tau_leadChargedHadrCandID;   //!
   TBranch        *b_nIsoPFCandidates;   //!
   TBranch        *b_isoPFCandidatePt;   //!
   TBranch        *b_isoPFCandidateEta;   //!
   TBranch        *b_isoPFCandidatePhi;   //!
   TBranch        *b_isoPFCandidateIso04;   //!
   TBranch        *b_isoPFCandidateD0;   //!
   TBranch        *b_isoPFCandidatePdgId;   //!
   TBranch        *b_nPhotons;   //!
   TBranch        *b_nPhotons_overlap;   //!
   TBranch        *b_phoE;   //!
   TBranch        *b_phoPt;   //!
   TBranch        *b_phoEta;   //!
   TBranch        *b_phoPhi;   //!
   TBranch        *b_phoSigmaIetaIeta;   //!
   TBranch        *b_phoFull5x5SigmaIetaIeta;   //!
   TBranch        *b_phoR9;   //!
   TBranch        *b_pho_sminor;   //!
   TBranch        *b_pho_smajor;   //!
   TBranch        *b_pho_HoverE;   //!
   TBranch        *b_pho_sumChargedHadronPtAllVertices;   //!
   TBranch        *b_pho_sumChargedHadronPt;   //!
   TBranch        *b_pho_sumNeutralHadronEt;   //!
   TBranch        *b_pho_sumPhotonEt;   //!
   TBranch        *b_pho_ecalPFClusterIso;   //!
   TBranch        *b_pho_hcalPFClusterIso;   //!
   TBranch        *b_pho_trkSumPtHollowConeDR03;   //!
   TBranch        *b_pho_sumWorstVertexChargedHadronPt;   //!
   TBranch        *b_pho_pfIsoChargedHadronIso;   //!
   TBranch        *b_pho_pfIsoChargedHadronIsoWrongVtx;   //!
   TBranch        *b_pho_pfIsoNeutralHadronIso;   //!
   TBranch        *b_pho_pfIsoPhotonIso;   //!
   TBranch        *b_pho_pfIsoModFrixione;   //!
   TBranch        *b_pho_pfIsoSumPUPt;   //!
   TBranch        *b_pho_isConversion;   //!
   TBranch        *b_pho_passEleVeto;   //!
   TBranch        *b_pho_RegressionE;   //!
   TBranch        *b_pho_RegressionEUncertainty;   //!
   TBranch        *b_pho_IDMVA;   //!
   TBranch        *b_pho_superClusterEnergy;   //!
   TBranch        *b_pho_superClusterRawEnergy;   //!
   TBranch        *b_pho_superClusterEta;   //!
   TBranch        *b_pho_superClusterPhi;   //!
   TBranch        *b_pho_superClusterX;   //!
   TBranch        *b_pho_superClusterY;   //!
   TBranch        *b_pho_superClusterZ;   //!
   TBranch        *b_pho_hasPixelSeed;   //!
   TBranch        *b_pho_passHLTFilter;   //!
   TBranch        *b_pho_convType;   //!
   TBranch        *b_pho_convTrkZ;   //!
   TBranch        *b_pho_convTrkClusZ;   //!
   TBranch        *b_pho_vtxSumPx;   //!
   TBranch        *b_pho_vtxSumPy;   //!
   TBranch        *b_pho_isStandardPhoton;   //!
   TBranch        *b_pho_seedRecHitSwitchToGain6;   //!
   TBranch        *b_pho_seedRecHitSwitchToGain1;   //!
   TBranch        *b_pho_anyRecHitSwitchToGain6;   //!
   TBranch        *b_pho_anyRecHitSwitchToGain1;   //!
   TBranch        *b_nCsc;   //!
   TBranch        *b_cscPhi;   //!
   TBranch        *b_cscEta;   //!
   TBranch        *b_cscX;   //!
   TBranch        *b_cscY;   //!
   TBranch        *b_cscZ;   //!
   TBranch        *b_cscNRecHits;   //!
   TBranch        *b_cscNRecHits_flag;   //!
   TBranch        *b_cscT;   //!
   TBranch        *b_cscChi2;   //!
   TBranch        *b_nRpc;   //!
   TBranch        *b_rpcPhi;   //!
   TBranch        *b_rpcEta;   //!
   TBranch        *b_rpcX;   //!
   TBranch        *b_rpcY;   //!
   TBranch        *b_rpcZ;   //!
   TBranch        *b_rpcT;   //!
   TBranch        *b_rpcTError;   //!
   TBranch        *b_nDt;   //!
   TBranch        *b_dtPhi;   //!
   TBranch        *b_dtEta;   //!
   TBranch        *b_dtX;   //!
   TBranch        *b_dtY;   //!
   TBranch        *b_dtZ;   //!
   TBranch        *b_dtDirX;   //!
   TBranch        *b_dtDirY;   //!
   TBranch        *b_dtDirZ;   //!
   TBranch        *b_dtT;   //!
   TBranch        *b_dtTError;   //!
   TBranch        *b_nRechits;   //!
   TBranch        *b_ecalRechit_Eta;   //!
   TBranch        *b_ecalRechit_Phi;   //!
   TBranch        *b_ecalRechit_E;   //!
   TBranch        *b_ecalRechit_T;   //!
   TBranch        *b_ecalRechit_E_Error;   //!
   TBranch        *b_ecalRechit_T_Error;   //!
   TBranch        *b_ecalRechit_kSaturatedflag;   //!
   TBranch        *b_ecalRechit_kLeadingEdgeRecoveredflag;   //!
   TBranch        *b_ecalRechit_kPoorRecoflag;   //!
   TBranch        *b_ecalRechit_kWeirdflag;   //!
   TBranch        *b_ecalRechit_kDiWeirdflag;   //!
   TBranch        *b_nJets;   //!
   TBranch        *b_jetE;   //!
   TBranch        *b_jetPt;   //!
   TBranch        *b_jetEta;   //!
   TBranch        *b_jetEt;   //!
   TBranch        *b_jetPhi;   //!
   TBranch        *b_jetCSV;   //!
   TBranch        *b_jetCISV;   //!
   TBranch        *b_jetProbb;   //!
   TBranch        *b_jetProbc;   //!
   TBranch        *b_jetProbudsg;   //!
   TBranch        *b_jetProbbb;   //!
   TBranch        *b_jetMass;   //!
   TBranch        *b_jetJetArea;   //!
   TBranch        *b_jetPileupE;   //!
   TBranch        *b_jetPileupId;   //!
   TBranch        *b_jetPileupIdFlag;   //!
   TBranch        *b_jetPassIDLoose;   //!
   TBranch        *b_jetPassIDTight;   //!
   TBranch        *b_jetPassMuFrac;   //!
   TBranch        *b_jetPassEleFrac;   //!
   TBranch        *b_jetPartonFlavor;   //!
   TBranch        *b_jetHadronFlavor;   //!
   TBranch        *b_jetChargedEMEnergyFraction;   //!
   TBranch        *b_jetNeutralEMEnergyFraction;   //!
   TBranch        *b_jetChargedHadronEnergyFraction;   //!
   TBranch        *b_jetNeutralHadronEnergyFraction;   //!
   TBranch        *b_jetMuonEnergyFraction;   //!
   TBranch        *b_jetHOEnergyFraction;   //!
   TBranch        *b_jetHFHadronEnergyFraction;   //!
   TBranch        *b_jetHFEMEnergyFraction;   //!
   TBranch        *b_jetAllMuonPt;   //!
   TBranch        *b_jetAllMuonEta;   //!
   TBranch        *b_jetAllMuonPhi;   //!
   TBranch        *b_jetAllMuonM;   //!
   TBranch        *b_jetPtWeightedDZ;   //!
   TBranch        *b_jetNRechits;   //!
   TBranch        *b_jetRechitE;   //!
   TBranch        *b_jetRechitT;   //!
   TBranch        *b_jetRechitT_rms;   //!
   TBranch        *b_jetRechitE_Error;   //!
   TBranch        *b_jetRechitT_Error;   //!
   TBranch        *b_jetAlphaMax;   //!
   TBranch        *b_jetBetaMax;   //!
   TBranch        *b_jetGammaMax_ET;   //!
   TBranch        *b_jetGammaMax_EM;   //!
   TBranch        *b_jetGammaMax_Hadronic;   //!
   TBranch        *b_jetGammaMax;   //!
   TBranch        *b_jetPtAllTracks;   //!
   TBranch        *b_jetPtAllPVTracks;   //!
   TBranch        *b_jetMedianTheta2D;   //!
   TBranch        *b_jetMedianIP;   //!
   TBranch        *b_jetMinDeltaRAllTracks;   //!
   TBranch        *b_jetMinDeltaRPVTracks;   //!
   TBranch        *b_jet_sig_et1;   //!
   TBranch        *b_jet_sig_et2;   //!
   TBranch        *b_jet_energy_frac;   //!
   TBranch        *b_jet_matched;   //!
   TBranch        *b_nCaloJets;   //!
   TBranch        *b_calojetE;   //!
   TBranch        *b_calojetEt;   //!
   TBranch        *b_calojetPt;   //!
   TBranch        *b_calojetEta;   //!
   TBranch        *b_calojetPhi;   //!
   TBranch        *b_calojetMass;   //!
   TBranch        *b_calojetJetArea;   //!
   TBranch        *b_calojetPileupE;   //!
   TBranch        *b_calojetPileupId;   //!
   TBranch        *b_calojetPileupIdFlag;   //!
   TBranch        *b_calojetPassIDLoose;   //!
   TBranch        *b_calojetPassIDTight;   //!
   TBranch        *b_calojetNRechits;   //!
   TBranch        *b_calojetRechitE;   //!
   TBranch        *b_calojetRechitT;   //!
   TBranch        *b_calojetRechitT_rms;   //!
   TBranch        *b_calojetAlphaMax;   //!
   TBranch        *b_calojetBetaMax;   //!
   TBranch        *b_calojetGammaMax_ET;   //!
   TBranch        *b_calojetGammaMax_EM;   //!
   TBranch        *b_calojetGammaMax_Hadronic;   //!
   TBranch        *b_calojetGammaMax;   //!
   TBranch        *b_calojet_HadronicEnergyFraction;   //!
   TBranch        *b_calojet_EMEnergyFraction;   //!
   TBranch        *b_calojetPtAllTracks;   //!
   TBranch        *b_calojetPtAllPVTracks;   //!
   TBranch        *b_calojetMedianTheta2D;   //!
   TBranch        *b_calojetMedianIP;   //!
   TBranch        *b_calojetMinDeltaRAllTracks;   //!
   TBranch        *b_calojetMinDeltaRPVTracks;   //!
   TBranch        *b_nFatJets;   //!
   TBranch        *b_fatJetE;   //!
   TBranch        *b_fatJetPt;   //!
   TBranch        *b_fatJetEta;   //!
   TBranch        *b_fatJetPhi;   //!
   TBranch        *b_fatJetCorrectedPt;   //!
   TBranch        *b_fatJetPrunedM;   //!
   TBranch        *b_fatJetTrimmedM;   //!
   TBranch        *b_fatJetFilteredM;   //!
   TBranch        *b_fatJetSoftDropM;   //!
   TBranch        *b_fatJetCorrectedSoftDropM;   //!
   TBranch        *b_fatJetUncorrectedSoftDropM;   //!
   TBranch        *b_fatJetTau1;   //!
   TBranch        *b_fatJetTau2;   //!
   TBranch        *b_fatJetTau3;   //!
   TBranch        *b_fatJetMaxSubjetCSV;   //!
   TBranch        *b_fatJetPassIDLoose;   //!
   TBranch        *b_fatJetPassIDTight;   //!
   TBranch        *b_metPt;   //!
   TBranch        *b_metPhi;   //!
   TBranch        *b_sumMET;   //!
   TBranch        *b_metType0Pt;   //!
   TBranch        *b_metType0Phi;   //!
   TBranch        *b_metType1Pt_raw;   //!
   TBranch        *b_metType1Pt;   //!
   TBranch        *b_metType1Px;   //!
   TBranch        *b_metType1Py;   //!
   TBranch        *b_metType1Eta;   //!
   TBranch        *b_metType1Phi;   //!
   TBranch        *b_metType1Phi_raw;   //!
   TBranch        *b_metType0Plus1Pt;   //!
   TBranch        *b_metType0Plus1Phi;   //!
   TBranch        *b_metNoHFPt;   //!
   TBranch        *b_metNoHFPhi;   //!
   TBranch        *b_metPuppiPt;   //!
   TBranch        *b_metPuppiPhi;   //!
   TBranch        *b_metCaloPt;   //!
   TBranch        *b_metCaloPhi;   //!
   TBranch        *b_Flag_HBHENoiseFilter;   //!
   TBranch        *b_Flag_HBHETightNoiseFilter;   //!
   TBranch        *b_Flag_HBHEIsoNoiseFilter;   //!
   TBranch        *b_Flag_badChargedCandidateFilter;   //!
   TBranch        *b_Flag_badMuonFilter;   //!
   TBranch        *b_Flag_badGlobalMuonFilter;   //!
   TBranch        *b_Flag_duplicateMuonFilter;   //!
   TBranch        *b_Flag_CSCTightHaloFilter;   //!
   TBranch        *b_Flag_hcalLaserEventFilter;   //!
   TBranch        *b_Flag_EcalDeadCellTriggerPrimitiveFilter;   //!
   TBranch        *b_Flag_EcalDeadCellBoundaryEnergyFilter;   //!
   TBranch        *b_Flag_goodVertices;   //!
   TBranch        *b_Flag_trackingFailureFilter;   //!
   TBranch        *b_Flag_eeBadScFilter;   //!
   TBranch        *b_Flag_ecalLaserCorrFilter;   //!
   TBranch        *b_Flag_trkPOGFilters;   //!
   TBranch        *b_Flag_trkPOG_manystripclus53X;   //!
   TBranch        *b_Flag_trkPOG_toomanystripclus53X;   //!
   TBranch        *b_Flag_trkPOG_logErrorTooManyClusters;   //!
   TBranch        *b_Flag_BadPFMuonFilter;   //!
   TBranch        *b_Flag_BadChargedCandidateFilter;   //!
   TBranch        *b_Flag_ecalBadCalibFilter;   //!
   TBranch        *b_Flag_METFilters;   //!
   TBranch        *b_HLTDecision;   //!
   TBranch        *b_HLTPrescale;   //!
   TBranch        *b_nGenJets;   //!
   TBranch        *b_genJetE;   //!
   TBranch        *b_genJetPt;   //!
   TBranch        *b_genJetEta;   //!
   TBranch        *b_genJetPhi;   //!
   TBranch        *b_genMetPtCalo;   //!
   TBranch        *b_genMetPhiCalo;   //!
   TBranch        *b_genMetPtTrue;   //!
   TBranch        *b_genMetPhiTrue;   //!
   TBranch        *b_genVertexX;   //!
   TBranch        *b_genVertexY;   //!
   TBranch        *b_genVertexZ;   //!
   TBranch        *b_genVertexT;   //!
   TBranch        *b_genWeight;   //!
   TBranch        *b_genSignalProcessID;   //!
   TBranch        *b_genQScale;   //!
   TBranch        *b_genAlphaQCD;   //!
   TBranch        *b_genAlphaQED;   //!
   TBranch        *b_scaleWeights;   //!
   TBranch        *b_pdfWeights;   //!
   TBranch        *b_alphasWeights;   //!
   TBranch        *b_nGenParticle;   //!
   TBranch        *b_gParticleMotherId;   //!
   TBranch        *b_gParticleMotherIndex;   //!
   TBranch        *b_gParticleId;   //!
   TBranch        *b_gParticleStatus;   //!
   TBranch        *b_gParticleE;   //!
   TBranch        *b_gParticlePt;   //!
   TBranch        *b_gParticlePx;   //!
   TBranch        *b_gParticlePy;   //!
   TBranch        *b_gParticlePz;   //!
   TBranch        *b_gParticleEta;   //!
   TBranch        *b_gParticlePhi;   //!
   TBranch        *b_gParticleProdVertexX;   //!
   TBranch        *b_gParticleProdVertexY;   //!
   TBranch        *b_gParticleProdVertexZ;   //!
   TBranch        *b_gLLP_prod_vertex_x;   //!
   TBranch        *b_gLLP_prod_vertex_y;   //!
   TBranch        *b_gLLP_prod_vertex_z;   //!
   TBranch        *b_gLLP_decay_vertex_x;   //!
   TBranch        *b_gLLP_decay_vertex_y;   //!
   TBranch        *b_gLLP_decay_vertex_z;   //!
   TBranch        *b_gLLP_beta;   //!
   TBranch        *b_gLLP_e;   //!
   TBranch        *b_gLLP_pt;   //!
   TBranch        *b_gLLP_eta;   //!
   TBranch        *b_gLLP_phi;   //!
   TBranch        *b_gLLP_travel_time;   //!
   TBranch        *b_gLLP_daughter_travel_time;   //!
   TBranch        *b_gLLP_daughter_pt;   //!
   TBranch        *b_gLLP_daughter_eta;   //!
   TBranch        *b_gLLP_daughter_phi;   //!
   TBranch        *b_gLLP_daughter_eta_ecalcorr;   //!
   TBranch        *b_gLLP_daughter_phi_ecalcorr;   //!
   TBranch        *b_gLLP_daughter_e;   //!
   TBranch        *b_photon_travel_time;   //!
   TBranch        *b_gen_time;   //!
   TBranch        *b_gen_time_pv;   //!
   TBranch        *b_gLLP_min_delta_r_match_calojet;   //!
   TBranch        *b_gLLP_daughter_match_calojet_index;   //!
   TBranch        *b_gLLP_daughter_match_jet_index;   //!
   TBranch        *b_gLLP_min_delta_r_match_jet;   //!

   llp(TTree *tree=0);
   virtual ~llp();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop(TString outFileName);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef llp_cxx
llp::llp(TTree *tree) : fChain(0)
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("llp_ntupler_ggHdddd_M55_1000mm.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("llp_ntupler_ggHdddd_M55_1000mm.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("llp_ntupler_ggHdddd_M55_1000mm.root:/ntuples");
      dir->GetObject("llp",tree);

   }
   Init(tree);
}

llp::~llp()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t llp::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t llp::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void llp::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   scaleWeights = 0;
   pdfWeights = 0;
   alphasWeights = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("isData", &isData, &b_isData);
   fChain->SetBranchAddress("nPV", &nPV, &b_nPV);
   fChain->SetBranchAddress("runNum", &runNum, &b_runNum);
   fChain->SetBranchAddress("nSlimmedSecondV", &nSlimmedSecondV, &b_nSlimmedSecondV);
   fChain->SetBranchAddress("lumiNum", &lumiNum, &b_lumiNum);
   fChain->SetBranchAddress("eventNum", &eventNum, &b_eventNum);
   fChain->SetBranchAddress("eventTime", &eventTime, &b_eventTime);
   fChain->SetBranchAddress("pvX", &pvX, &b_pvX);
   fChain->SetBranchAddress("pvY", &pvY, &b_pvY);
   fChain->SetBranchAddress("pvZ", &pvZ, &b_pvZ);
   fChain->SetBranchAddress("fixedGridRhoAll", &fixedGridRhoAll, &b_fixedGridRhoAll);
   fChain->SetBranchAddress("fixedGridRhoFastjetAll", &fixedGridRhoFastjetAll, &b_fixedGridRhoFastjetAll);
   fChain->SetBranchAddress("fixedGridRhoFastjetAllCalo", &fixedGridRhoFastjetAllCalo, &b_fixedGridRhoFastjetAllCalo);
   fChain->SetBranchAddress("fixedGridRhoFastjetCentralCalo", &fixedGridRhoFastjetCentralCalo, &b_fixedGridRhoFastjetCentralCalo);
   fChain->SetBranchAddress("fixedGridRhoFastjetCentralChargedPileUp", &fixedGridRhoFastjetCentralChargedPileUp, &b_fixedGridRhoFastjetCentralChargedPileUp);
   fChain->SetBranchAddress("fixedGridRhoFastjetCentralNeutral", &fixedGridRhoFastjetCentralNeutral, &b_fixedGridRhoFastjetCentralNeutral);
   fChain->SetBranchAddress("nPVAll", &nPVAll, &b_nPVAll);
   fChain->SetBranchAddress("pvAllX", &pvAllX, &b_pvAllX);
   fChain->SetBranchAddress("pvAllY", &pvAllY, &b_pvAllY);
   fChain->SetBranchAddress("pvAllZ", &pvAllZ, &b_pvAllZ);
   fChain->SetBranchAddress("pvAllLogSumPtSq", &pvAllLogSumPtSq, &b_pvAllLogSumPtSq);
   fChain->SetBranchAddress("pvAllSumPx", &pvAllSumPx, &b_pvAllSumPx);
   fChain->SetBranchAddress("pvAllSumPy", &pvAllSumPy, &b_pvAllSumPy);
   fChain->SetBranchAddress("nPVTracks", &nPVTracks, &b_nPVTracks);
   fChain->SetBranchAddress("pvTrackPt", &pvTrackPt, &b_pvTrackPt);
   fChain->SetBranchAddress("pvTrackEta", &pvTrackEta, &b_pvTrackEta);
   fChain->SetBranchAddress("pvTrackPhi", &pvTrackPhi, &b_pvTrackPhi);
   fChain->SetBranchAddress("nBunchXing", &nBunchXing, &b_nBunchXing);
   fChain->SetBranchAddress("BunchXing", BunchXing, &b_BunchXing);
   fChain->SetBranchAddress("nPU", nPU, &b_nPU);
   fChain->SetBranchAddress("nPUmean", nPUmean, &b_nPUmean);
   fChain->SetBranchAddress("nMuons", &nMuons, &b_nMuons);
   fChain->SetBranchAddress("muonE", muonE, &b_muonE);
   fChain->SetBranchAddress("muonPt", muonPt, &b_muonPt);
   fChain->SetBranchAddress("muonEta", muonEta, &b_muonEta);
   fChain->SetBranchAddress("muonPhi", muonPhi, &b_muonPhi);
   fChain->SetBranchAddress("muonCharge", muonCharge, &b_muonCharge);
   fChain->SetBranchAddress("muonIsLoose", muonIsLoose, &b_muonIsLoose);
   fChain->SetBranchAddress("muonIsMedium", muonIsMedium, &b_muonIsMedium);
   fChain->SetBranchAddress("muonIsTight", muonIsTight, &b_muonIsTight);
   fChain->SetBranchAddress("muon_d0", muon_d0, &b_muon_d0);
   fChain->SetBranchAddress("muon_dZ", muon_dZ, &b_muon_dZ);
   fChain->SetBranchAddress("muon_ip3d", muon_ip3d, &b_muon_ip3d);
   fChain->SetBranchAddress("muon_ip3dSignificance", muon_ip3dSignificance, &b_muon_ip3dSignificance);
   fChain->SetBranchAddress("muonType", muonType, &b_muonType);
   fChain->SetBranchAddress("muonQuality", muonQuality, &b_muonQuality);
   fChain->SetBranchAddress("muon_pileupIso", muon_pileupIso, &b_muon_pileupIso);
   fChain->SetBranchAddress("muon_chargedIso", muon_chargedIso, &b_muon_chargedIso);
   fChain->SetBranchAddress("muon_photonIso", muon_photonIso, &b_muon_photonIso);
   fChain->SetBranchAddress("muon_neutralHadIso", muon_neutralHadIso, &b_muon_neutralHadIso);
   fChain->SetBranchAddress("muon_ptrel", muon_ptrel, &b_muon_ptrel);
   fChain->SetBranchAddress("muon_chargedMiniIso", muon_chargedMiniIso, &b_muon_chargedMiniIso);
   fChain->SetBranchAddress("muon_photonAndNeutralHadronMiniIso", muon_photonAndNeutralHadronMiniIso, &b_muon_photonAndNeutralHadronMiniIso);
   fChain->SetBranchAddress("muon_chargedPileupMiniIso", muon_chargedPileupMiniIso, &b_muon_chargedPileupMiniIso);
   fChain->SetBranchAddress("muon_activityMiniIsoAnnulus", muon_activityMiniIsoAnnulus, &b_muon_activityMiniIsoAnnulus);
   fChain->SetBranchAddress("muon_passSingleMuTagFilter", muon_passSingleMuTagFilter, &b_muon_passSingleMuTagFilter);
   fChain->SetBranchAddress("muon_passHLTFilter", muon_passHLTFilter, &b_muon_passHLTFilter);
   fChain->SetBranchAddress("muon_validFractionTrackerHits", muon_validFractionTrackerHits, &b_muon_validFractionTrackerHits);
   fChain->SetBranchAddress("muon_isGlobal", muon_isGlobal, &b_muon_isGlobal);
   fChain->SetBranchAddress("muon_normChi2", muon_normChi2, &b_muon_normChi2);
   fChain->SetBranchAddress("muon_chi2LocalPosition", muon_chi2LocalPosition, &b_muon_chi2LocalPosition);
   fChain->SetBranchAddress("muon_kinkFinder", muon_kinkFinder, &b_muon_kinkFinder);
   fChain->SetBranchAddress("muon_segmentCompatability", muon_segmentCompatability, &b_muon_segmentCompatability);
   fChain->SetBranchAddress("muonIsICHEPMedium", muonIsICHEPMedium, &b_muonIsICHEPMedium);
   fChain->SetBranchAddress("nElectrons", &nElectrons, &b_nElectrons);
   fChain->SetBranchAddress("eleE", eleE, &b_eleE);
   fChain->SetBranchAddress("elePt", elePt, &b_elePt);
   fChain->SetBranchAddress("eleEta", eleEta, &b_eleEta);
   fChain->SetBranchAddress("elePhi", elePhi, &b_elePhi);
   fChain->SetBranchAddress("eleCharge", eleCharge, &b_eleCharge);
   fChain->SetBranchAddress("eleEta_SC", eleEta_SC, &b_eleEta_SC);
   fChain->SetBranchAddress("eleSigmaIetaIeta", eleSigmaIetaIeta, &b_eleSigmaIetaIeta);
   fChain->SetBranchAddress("eleFull5x5SigmaIetaIeta", eleFull5x5SigmaIetaIeta, &b_eleFull5x5SigmaIetaIeta);
   fChain->SetBranchAddress("eleR9", eleR9, &b_eleR9);
   fChain->SetBranchAddress("ele_dEta", ele_dEta, &b_ele_dEta);
   fChain->SetBranchAddress("ele_dPhi", ele_dPhi, &b_ele_dPhi);
   fChain->SetBranchAddress("ele_HoverE", ele_HoverE, &b_ele_HoverE);
   fChain->SetBranchAddress("ele_d0", ele_d0, &b_ele_d0);
   fChain->SetBranchAddress("ele_dZ", ele_dZ, &b_ele_dZ);
   fChain->SetBranchAddress("ele_ip3d", ele_ip3d, &b_ele_ip3d);
   fChain->SetBranchAddress("ele_ip3dSignificance", ele_ip3dSignificance, &b_ele_ip3dSignificance);
   fChain->SetBranchAddress("ele_pileupIso", ele_pileupIso, &b_ele_pileupIso);
   fChain->SetBranchAddress("ele_chargedIso", ele_chargedIso, &b_ele_chargedIso);
   fChain->SetBranchAddress("ele_photonIso", ele_photonIso, &b_ele_photonIso);
   fChain->SetBranchAddress("ele_neutralHadIso", ele_neutralHadIso, &b_ele_neutralHadIso);
   fChain->SetBranchAddress("ele_MissHits", ele_MissHits, &b_ele_MissHits);
   fChain->SetBranchAddress("ele_PassConvVeto", ele_PassConvVeto, &b_ele_PassConvVeto);
   fChain->SetBranchAddress("ele_OneOverEminusOneOverP", ele_OneOverEminusOneOverP, &b_ele_OneOverEminusOneOverP);
   fChain->SetBranchAddress("ele_IDMVAGeneralPurpose", ele_IDMVAGeneralPurpose, &b_ele_IDMVAGeneralPurpose);
   fChain->SetBranchAddress("ele_IDMVACategoryGeneralPurpose", ele_IDMVACategoryGeneralPurpose, &b_ele_IDMVACategoryGeneralPurpose);
   fChain->SetBranchAddress("ele_IDMVAHZZ", ele_IDMVAHZZ, &b_ele_IDMVAHZZ);
   fChain->SetBranchAddress("ele_IDMVACategoryHZZ", ele_IDMVACategoryHZZ, &b_ele_IDMVACategoryHZZ);
   fChain->SetBranchAddress("ele_RegressionE", ele_RegressionE, &b_ele_RegressionE);
   fChain->SetBranchAddress("ele_CombineP4", ele_CombineP4, &b_ele_CombineP4);
   fChain->SetBranchAddress("ele_ptrel", ele_ptrel, &b_ele_ptrel);
   fChain->SetBranchAddress("ele_chargedMiniIso", ele_chargedMiniIso, &b_ele_chargedMiniIso);
   fChain->SetBranchAddress("ele_photonAndNeutralHadronMiniIso", ele_photonAndNeutralHadronMiniIso, &b_ele_photonAndNeutralHadronMiniIso);
   fChain->SetBranchAddress("ele_chargedPileupMiniIso", ele_chargedPileupMiniIso, &b_ele_chargedPileupMiniIso);
   fChain->SetBranchAddress("ele_activityMiniIsoAnnulus", ele_activityMiniIsoAnnulus, &b_ele_activityMiniIsoAnnulus);
   fChain->SetBranchAddress("ele_passSingleEleTagFilter", ele_passSingleEleTagFilter, &b_ele_passSingleEleTagFilter);
   fChain->SetBranchAddress("ele_passTPOneTagFilter", ele_passTPOneTagFilter, &b_ele_passTPOneTagFilter);
   fChain->SetBranchAddress("ele_passTPTwoTagFilter", ele_passTPTwoTagFilter, &b_ele_passTPTwoTagFilter);
   fChain->SetBranchAddress("ele_passTPOneProbeFilter", ele_passTPOneProbeFilter, &b_ele_passTPOneProbeFilter);
   fChain->SetBranchAddress("ele_passTPTwoProbeFilter", ele_passTPTwoProbeFilter, &b_ele_passTPTwoProbeFilter);
   fChain->SetBranchAddress("ele_passHLTFilter", ele_passHLTFilter, &b_ele_passHLTFilter);
   fChain->SetBranchAddress("nTaus", &nTaus, &b_nTaus);
   fChain->SetBranchAddress("tauE", &tauE, &b_tauE);
   fChain->SetBranchAddress("tauPt", &tauPt, &b_tauPt);
   fChain->SetBranchAddress("tauEta", &tauEta, &b_tauEta);
   fChain->SetBranchAddress("tauPhi", &tauPhi, &b_tauPhi);
   fChain->SetBranchAddress("tau_IsLoose", &tau_IsLoose, &b_tau_IsLoose);
   fChain->SetBranchAddress("tau_IsMedium", &tau_IsMedium, &b_tau_IsMedium);
   fChain->SetBranchAddress("tau_IsTight", &tau_IsTight, &b_tau_IsTight);
   fChain->SetBranchAddress("tau_passEleVetoLoose", &tau_passEleVetoLoose, &b_tau_passEleVetoLoose);
   fChain->SetBranchAddress("tau_passEleVetoMedium", &tau_passEleVetoMedium, &b_tau_passEleVetoMedium);
   fChain->SetBranchAddress("tau_passEleVetoTight", &tau_passEleVetoTight, &b_tau_passEleVetoTight);
   fChain->SetBranchAddress("tau_passMuVetoLoose", &tau_passMuVetoLoose, &b_tau_passMuVetoLoose);
   fChain->SetBranchAddress("tau_passMuVetoMedium", &tau_passMuVetoMedium, &b_tau_passMuVetoMedium);
   fChain->SetBranchAddress("tau_passMuVetoTight", &tau_passMuVetoTight, &b_tau_passMuVetoTight);
   fChain->SetBranchAddress("tau_ID", &tau_ID, &b_tau_ID);
   fChain->SetBranchAddress("tau_combinedIsoDeltaBetaCorr3Hits", &tau_combinedIsoDeltaBetaCorr3Hits, &b_tau_combinedIsoDeltaBetaCorr3Hits);
   fChain->SetBranchAddress("tau_chargedIsoPtSum", &tau_chargedIsoPtSum, &b_tau_chargedIsoPtSum);
   fChain->SetBranchAddress("tau_neutralIsoPtSum", &tau_neutralIsoPtSum, &b_tau_neutralIsoPtSum);
   fChain->SetBranchAddress("tau_puCorrPtSum", &tau_puCorrPtSum, &b_tau_puCorrPtSum);
   fChain->SetBranchAddress("tau_eleVetoMVA", &tau_eleVetoMVA, &b_tau_eleVetoMVA);
   fChain->SetBranchAddress("tau_eleVetoCategory", &tau_eleVetoCategory, &b_tau_eleVetoCategory);
   fChain->SetBranchAddress("tau_muonVetoMVA", &tau_muonVetoMVA, &b_tau_muonVetoMVA);
   fChain->SetBranchAddress("tau_isoMVAnewDMwLT", &tau_isoMVAnewDMwLT, &b_tau_isoMVAnewDMwLT);
   fChain->SetBranchAddress("tau_isoMVAnewDMwoLT", &tau_isoMVAnewDMwoLT, &b_tau_isoMVAnewDMwoLT);
   fChain->SetBranchAddress("tau_leadCandPt", &tau_leadCandPt, &b_tau_leadCandPt);
   fChain->SetBranchAddress("tau_leadCandID", &tau_leadCandID, &b_tau_leadCandID);
   fChain->SetBranchAddress("tau_leadChargedHadrCandPt", &tau_leadChargedHadrCandPt, &b_tau_leadChargedHadrCandPt);
   fChain->SetBranchAddress("tau_leadChargedHadrCandID", &tau_leadChargedHadrCandID, &b_tau_leadChargedHadrCandID);
   fChain->SetBranchAddress("nIsoPFCandidates", &nIsoPFCandidates, &b_nIsoPFCandidates);
   fChain->SetBranchAddress("isoPFCandidatePt", &isoPFCandidatePt, &b_isoPFCandidatePt);
   fChain->SetBranchAddress("isoPFCandidateEta", &isoPFCandidateEta, &b_isoPFCandidateEta);
   fChain->SetBranchAddress("isoPFCandidatePhi", &isoPFCandidatePhi, &b_isoPFCandidatePhi);
   fChain->SetBranchAddress("isoPFCandidateIso04", &isoPFCandidateIso04, &b_isoPFCandidateIso04);
   fChain->SetBranchAddress("isoPFCandidateD0", &isoPFCandidateD0, &b_isoPFCandidateD0);
   fChain->SetBranchAddress("isoPFCandidatePdgId", &isoPFCandidatePdgId, &b_isoPFCandidatePdgId);
   fChain->SetBranchAddress("nPhotons", &nPhotons, &b_nPhotons);
   fChain->SetBranchAddress("nPhotons_overlap", &nPhotons_overlap, &b_nPhotons_overlap);
   fChain->SetBranchAddress("phoE", &phoE, &b_phoE);
   fChain->SetBranchAddress("phoPt", &phoPt, &b_phoPt);
   fChain->SetBranchAddress("phoEta", &phoEta, &b_phoEta);
   fChain->SetBranchAddress("phoPhi", &phoPhi, &b_phoPhi);
   fChain->SetBranchAddress("phoSigmaIetaIeta", &phoSigmaIetaIeta, &b_phoSigmaIetaIeta);
   fChain->SetBranchAddress("phoFull5x5SigmaIetaIeta", &phoFull5x5SigmaIetaIeta, &b_phoFull5x5SigmaIetaIeta);
   fChain->SetBranchAddress("phoR9", &phoR9, &b_phoR9);
   fChain->SetBranchAddress("pho_sminor", &pho_sminor, &b_pho_sminor);
   fChain->SetBranchAddress("pho_smajor", &pho_smajor, &b_pho_smajor);
   fChain->SetBranchAddress("pho_HoverE", &pho_HoverE, &b_pho_HoverE);
   fChain->SetBranchAddress("pho_sumChargedHadronPtAllVertices", &pho_sumChargedHadronPtAllVertices, &b_pho_sumChargedHadronPtAllVertices);
   fChain->SetBranchAddress("pho_sumChargedHadronPt", &pho_sumChargedHadronPt, &b_pho_sumChargedHadronPt);
   fChain->SetBranchAddress("pho_sumNeutralHadronEt", &pho_sumNeutralHadronEt, &b_pho_sumNeutralHadronEt);
   fChain->SetBranchAddress("pho_sumPhotonEt", &pho_sumPhotonEt, &b_pho_sumPhotonEt);
   fChain->SetBranchAddress("pho_ecalPFClusterIso", &pho_ecalPFClusterIso, &b_pho_ecalPFClusterIso);
   fChain->SetBranchAddress("pho_hcalPFClusterIso", &pho_hcalPFClusterIso, &b_pho_hcalPFClusterIso);
   fChain->SetBranchAddress("pho_trkSumPtHollowConeDR03", &pho_trkSumPtHollowConeDR03, &b_pho_trkSumPtHollowConeDR03);
   fChain->SetBranchAddress("pho_sumWorstVertexChargedHadronPt", &pho_sumWorstVertexChargedHadronPt, &b_pho_sumWorstVertexChargedHadronPt);
   fChain->SetBranchAddress("pho_pfIsoChargedHadronIso", &pho_pfIsoChargedHadronIso, &b_pho_pfIsoChargedHadronIso);
   fChain->SetBranchAddress("pho_pfIsoChargedHadronIsoWrongVtx", &pho_pfIsoChargedHadronIsoWrongVtx, &b_pho_pfIsoChargedHadronIsoWrongVtx);
   fChain->SetBranchAddress("pho_pfIsoNeutralHadronIso", &pho_pfIsoNeutralHadronIso, &b_pho_pfIsoNeutralHadronIso);
   fChain->SetBranchAddress("pho_pfIsoPhotonIso", &pho_pfIsoPhotonIso, &b_pho_pfIsoPhotonIso);
   fChain->SetBranchAddress("pho_pfIsoModFrixione", &pho_pfIsoModFrixione, &b_pho_pfIsoModFrixione);
   fChain->SetBranchAddress("pho_pfIsoSumPUPt", &pho_pfIsoSumPUPt, &b_pho_pfIsoSumPUPt);
   fChain->SetBranchAddress("pho_isConversion", &pho_isConversion, &b_pho_isConversion);
   fChain->SetBranchAddress("pho_passEleVeto", &pho_passEleVeto, &b_pho_passEleVeto);
   fChain->SetBranchAddress("pho_RegressionE", &pho_RegressionE, &b_pho_RegressionE);
   fChain->SetBranchAddress("pho_RegressionEUncertainty", &pho_RegressionEUncertainty, &b_pho_RegressionEUncertainty);
   fChain->SetBranchAddress("pho_IDMVA", &pho_IDMVA, &b_pho_IDMVA);
   fChain->SetBranchAddress("pho_superClusterEnergy", &pho_superClusterEnergy, &b_pho_superClusterEnergy);
   fChain->SetBranchAddress("pho_superClusterRawEnergy", &pho_superClusterRawEnergy, &b_pho_superClusterRawEnergy);
   fChain->SetBranchAddress("pho_superClusterEta", &pho_superClusterEta, &b_pho_superClusterEta);
   fChain->SetBranchAddress("pho_superClusterPhi", &pho_superClusterPhi, &b_pho_superClusterPhi);
   fChain->SetBranchAddress("pho_superClusterX", &pho_superClusterX, &b_pho_superClusterX);
   fChain->SetBranchAddress("pho_superClusterY", &pho_superClusterY, &b_pho_superClusterY);
   fChain->SetBranchAddress("pho_superClusterZ", &pho_superClusterZ, &b_pho_superClusterZ);
   fChain->SetBranchAddress("pho_hasPixelSeed", &pho_hasPixelSeed, &b_pho_hasPixelSeed);
   fChain->SetBranchAddress("pho_passHLTFilter", &pho_passHLTFilter, &b_pho_passHLTFilter);
   fChain->SetBranchAddress("pho_convType", &pho_convType, &b_pho_convType);
   fChain->SetBranchAddress("pho_convTrkZ", &pho_convTrkZ, &b_pho_convTrkZ);
   fChain->SetBranchAddress("pho_convTrkClusZ", &pho_convTrkClusZ, &b_pho_convTrkClusZ);
   fChain->SetBranchAddress("pho_vtxSumPx", &pho_vtxSumPx, &b_pho_vtxSumPx);
   fChain->SetBranchAddress("pho_vtxSumPy", &pho_vtxSumPy, &b_pho_vtxSumPy);
   fChain->SetBranchAddress("pho_isStandardPhoton", &pho_isStandardPhoton, &b_pho_isStandardPhoton);
   fChain->SetBranchAddress("pho_seedRecHitSwitchToGain6", &pho_seedRecHitSwitchToGain6, &b_pho_seedRecHitSwitchToGain6);
   fChain->SetBranchAddress("pho_seedRecHitSwitchToGain1", &pho_seedRecHitSwitchToGain1, &b_pho_seedRecHitSwitchToGain1);
   fChain->SetBranchAddress("pho_anyRecHitSwitchToGain6", &pho_anyRecHitSwitchToGain6, &b_pho_anyRecHitSwitchToGain6);
   fChain->SetBranchAddress("pho_anyRecHitSwitchToGain1", &pho_anyRecHitSwitchToGain1, &b_pho_anyRecHitSwitchToGain1);
   fChain->SetBranchAddress("nCsc", &nCsc, &b_nCsc);
   fChain->SetBranchAddress("cscPhi", cscPhi, &b_cscPhi);
   fChain->SetBranchAddress("cscEta", cscEta, &b_cscEta);
   fChain->SetBranchAddress("cscX", cscX, &b_cscX);
   fChain->SetBranchAddress("cscY", cscY, &b_cscY);
   fChain->SetBranchAddress("cscZ", cscZ, &b_cscZ);
   fChain->SetBranchAddress("cscNRecHits", cscNRecHits, &b_cscNRecHits);
   fChain->SetBranchAddress("cscNRecHits_flag", cscNRecHits_flag, &b_cscNRecHits_flag);
   fChain->SetBranchAddress("cscT", cscT, &b_cscT);
   fChain->SetBranchAddress("cscChi2", cscChi2, &b_cscChi2);
   fChain->SetBranchAddress("nRpc", &nRpc, &b_nRpc);
   fChain->SetBranchAddress("rpcPhi", rpcPhi, &b_rpcPhi);
   fChain->SetBranchAddress("rpcEta", rpcEta, &b_rpcEta);
   fChain->SetBranchAddress("rpcX", rpcX, &b_rpcX);
   fChain->SetBranchAddress("rpcY", rpcY, &b_rpcY);
   fChain->SetBranchAddress("rpcZ", rpcZ, &b_rpcZ);
   fChain->SetBranchAddress("rpcT", rpcT, &b_rpcT);
   fChain->SetBranchAddress("rpcTError", rpcTError, &b_rpcTError);
   fChain->SetBranchAddress("nDt", &nDt, &b_nDt);
   fChain->SetBranchAddress("dtPhi", dtPhi, &b_dtPhi);
   fChain->SetBranchAddress("dtEta", dtEta, &b_dtEta);
   fChain->SetBranchAddress("dtX", dtX, &b_dtX);
   fChain->SetBranchAddress("dtY", dtY, &b_dtY);
   fChain->SetBranchAddress("dtZ", dtZ, &b_dtZ);
   fChain->SetBranchAddress("dtDirX", dtDirX, &b_dtDirX);
   fChain->SetBranchAddress("dtDirY", dtDirY, &b_dtDirY);
   fChain->SetBranchAddress("dtDirZ", dtDirZ, &b_dtDirZ);
   fChain->SetBranchAddress("dtT", dtT, &b_dtT);
   fChain->SetBranchAddress("dtTError", dtTError, &b_dtTError);
   fChain->SetBranchAddress("nRechits", &nRechits, &b_nRechits);
   fChain->SetBranchAddress("ecalRechit_Eta", &ecalRechit_Eta, &b_ecalRechit_Eta);
   fChain->SetBranchAddress("ecalRechit_Phi", &ecalRechit_Phi, &b_ecalRechit_Phi);
   fChain->SetBranchAddress("ecalRechit_E", &ecalRechit_E, &b_ecalRechit_E);
   fChain->SetBranchAddress("ecalRechit_T", &ecalRechit_T, &b_ecalRechit_T);
   fChain->SetBranchAddress("ecalRechit_E_Error", &ecalRechit_E_Error, &b_ecalRechit_E_Error);
   fChain->SetBranchAddress("ecalRechit_T_Error", &ecalRechit_T_Error, &b_ecalRechit_T_Error);
   fChain->SetBranchAddress("ecalRechit_kSaturatedflag", &ecalRechit_kSaturatedflag, &b_ecalRechit_kSaturatedflag);
   fChain->SetBranchAddress("ecalRechit_kLeadingEdgeRecoveredflag", &ecalRechit_kLeadingEdgeRecoveredflag, &b_ecalRechit_kLeadingEdgeRecoveredflag);
   fChain->SetBranchAddress("ecalRechit_kPoorRecoflag", &ecalRechit_kPoorRecoflag, &b_ecalRechit_kPoorRecoflag);
   fChain->SetBranchAddress("ecalRechit_kWeirdflag", &ecalRechit_kWeirdflag, &b_ecalRechit_kWeirdflag);
   fChain->SetBranchAddress("ecalRechit_kDiWeirdflag", &ecalRechit_kDiWeirdflag, &b_ecalRechit_kDiWeirdflag);
   fChain->SetBranchAddress("nJets", &nJets, &b_nJets);
   fChain->SetBranchAddress("jetE", jetE, &b_jetE);
   fChain->SetBranchAddress("jetPt", jetPt, &b_jetPt);
   fChain->SetBranchAddress("jetEta", jetEta, &b_jetEta);
   fChain->SetBranchAddress("jetEt", jetEt, &b_jetEt);
   fChain->SetBranchAddress("jetPhi", jetPhi, &b_jetPhi);
   fChain->SetBranchAddress("jetCSV", jetCSV, &b_jetCSV);
   fChain->SetBranchAddress("jetCISV", jetCISV, &b_jetCISV);
   fChain->SetBranchAddress("jetProbb", jetProbb, &b_jetProbb);
   fChain->SetBranchAddress("jetProbc", jetProbc, &b_jetProbc);
   fChain->SetBranchAddress("jetProbudsg", jetProbudsg, &b_jetProbudsg);
   fChain->SetBranchAddress("jetProbbb", jetProbbb, &b_jetProbbb);
   fChain->SetBranchAddress("jetMass", jetMass, &b_jetMass);
   fChain->SetBranchAddress("jetJetArea", jetJetArea, &b_jetJetArea);
   fChain->SetBranchAddress("jetPileupE", jetPileupE, &b_jetPileupE);
   fChain->SetBranchAddress("jetPileupId", jetPileupId, &b_jetPileupId);
   fChain->SetBranchAddress("jetPileupIdFlag", jetPileupIdFlag, &b_jetPileupIdFlag);
   fChain->SetBranchAddress("jetPassIDLoose", jetPassIDLoose, &b_jetPassIDLoose);
   fChain->SetBranchAddress("jetPassIDTight", jetPassIDTight, &b_jetPassIDTight);
   fChain->SetBranchAddress("jetPassMuFrac", jetPassMuFrac, &b_jetPassMuFrac);
   fChain->SetBranchAddress("jetPassEleFrac", jetPassEleFrac, &b_jetPassEleFrac);
   fChain->SetBranchAddress("jetPartonFlavor", jetPartonFlavor, &b_jetPartonFlavor);
   fChain->SetBranchAddress("jetHadronFlavor", jetHadronFlavor, &b_jetHadronFlavor);
   fChain->SetBranchAddress("jetChargedEMEnergyFraction", jetChargedEMEnergyFraction, &b_jetChargedEMEnergyFraction);
   fChain->SetBranchAddress("jetNeutralEMEnergyFraction", jetNeutralEMEnergyFraction, &b_jetNeutralEMEnergyFraction);
   fChain->SetBranchAddress("jetChargedHadronEnergyFraction", jetChargedHadronEnergyFraction, &b_jetChargedHadronEnergyFraction);
   fChain->SetBranchAddress("jetNeutralHadronEnergyFraction", jetNeutralHadronEnergyFraction, &b_jetNeutralHadronEnergyFraction);
   fChain->SetBranchAddress("jetMuonEnergyFraction", jetMuonEnergyFraction, &b_jetMuonEnergyFraction);
   fChain->SetBranchAddress("jetHOEnergyFraction", jetHOEnergyFraction, &b_jetHOEnergyFraction);
   fChain->SetBranchAddress("jetHFHadronEnergyFraction", jetHFHadronEnergyFraction, &b_jetHFHadronEnergyFraction);
   fChain->SetBranchAddress("jetHFEMEnergyFraction", jetHFEMEnergyFraction, &b_jetHFEMEnergyFraction);
   fChain->SetBranchAddress("jetAllMuonPt", jetAllMuonPt, &b_jetAllMuonPt);
   fChain->SetBranchAddress("jetAllMuonEta", jetAllMuonEta, &b_jetAllMuonEta);
   fChain->SetBranchAddress("jetAllMuonPhi", jetAllMuonPhi, &b_jetAllMuonPhi);
   fChain->SetBranchAddress("jetAllMuonM", jetAllMuonM, &b_jetAllMuonM);
   fChain->SetBranchAddress("jetPtWeightedDZ", jetPtWeightedDZ, &b_jetPtWeightedDZ);
   fChain->SetBranchAddress("jetNRechits", jetNRechits, &b_jetNRechits);
   fChain->SetBranchAddress("jetRechitE", jetRechitE, &b_jetRechitE);
   fChain->SetBranchAddress("jetRechitT", jetRechitT, &b_jetRechitT);
   fChain->SetBranchAddress("jetRechitT_rms", jetRechitT_rms, &b_jetRechitT_rms);
   fChain->SetBranchAddress("jetRechitE_Error", jetRechitE_Error, &b_jetRechitE_Error);
   fChain->SetBranchAddress("jetRechitT_Error", jetRechitT_Error, &b_jetRechitT_Error);
   fChain->SetBranchAddress("jetAlphaMax", jetAlphaMax, &b_jetAlphaMax);
   fChain->SetBranchAddress("jetBetaMax", jetBetaMax, &b_jetBetaMax);
   fChain->SetBranchAddress("jetGammaMax_ET", jetGammaMax_ET, &b_jetGammaMax_ET);
   fChain->SetBranchAddress("jetGammaMax_EM", jetGammaMax_EM, &b_jetGammaMax_EM);
   fChain->SetBranchAddress("jetGammaMax_Hadronic", jetGammaMax_Hadronic, &b_jetGammaMax_Hadronic);
   fChain->SetBranchAddress("jetGammaMax", jetGammaMax, &b_jetGammaMax);
   fChain->SetBranchAddress("jetPtAllTracks", jetPtAllTracks, &b_jetPtAllTracks);
   fChain->SetBranchAddress("jetPtAllPVTracks", jetPtAllPVTracks, &b_jetPtAllPVTracks);
   fChain->SetBranchAddress("jetMedianTheta2D", jetMedianTheta2D, &b_jetMedianTheta2D);
   fChain->SetBranchAddress("jetMedianIP", jetMedianIP, &b_jetMedianIP);
   fChain->SetBranchAddress("jetMinDeltaRAllTracks", jetMinDeltaRAllTracks, &b_jetMinDeltaRAllTracks);
   fChain->SetBranchAddress("jetMinDeltaRPVTracks", jetMinDeltaRPVTracks, &b_jetMinDeltaRPVTracks);
   fChain->SetBranchAddress("jet_sig_et1", jet_sig_et1, &b_jet_sig_et1);
   fChain->SetBranchAddress("jet_sig_et2", jet_sig_et2, &b_jet_sig_et2);
   fChain->SetBranchAddress("jet_energy_frac", jet_energy_frac, &b_jet_energy_frac);
   fChain->SetBranchAddress("jet_matched", jet_matched, &b_jet_matched);
   fChain->SetBranchAddress("nCaloJets", &nCaloJets, &b_nCaloJets);
   fChain->SetBranchAddress("calojetE", calojetE, &b_calojetE);
   fChain->SetBranchAddress("calojetEt", calojetEt, &b_calojetEt);
   fChain->SetBranchAddress("calojetPt", calojetPt, &b_calojetPt);
   fChain->SetBranchAddress("calojetEta", calojetEta, &b_calojetEta);
   fChain->SetBranchAddress("calojetPhi", calojetPhi, &b_calojetPhi);
   fChain->SetBranchAddress("calojetMass", calojetMass, &b_calojetMass);
   fChain->SetBranchAddress("calojetJetArea", calojetJetArea, &b_calojetJetArea);
   fChain->SetBranchAddress("calojetPileupE", calojetPileupE, &b_calojetPileupE);
   fChain->SetBranchAddress("calojetPileupId", calojetPileupId, &b_calojetPileupId);
   fChain->SetBranchAddress("calojetPileupIdFlag", calojetPileupIdFlag, &b_calojetPileupIdFlag);
   fChain->SetBranchAddress("calojetPassIDLoose", calojetPassIDLoose, &b_calojetPassIDLoose);
   fChain->SetBranchAddress("calojetPassIDTight", calojetPassIDTight, &b_calojetPassIDTight);
   fChain->SetBranchAddress("calojetNRechits", calojetNRechits, &b_calojetNRechits);
   fChain->SetBranchAddress("calojetRechitE", calojetRechitE, &b_calojetRechitE);
   fChain->SetBranchAddress("calojetRechitT", calojetRechitT, &b_calojetRechitT);
   fChain->SetBranchAddress("calojetRechitT_rms", calojetRechitT_rms, &b_calojetRechitT_rms);
   fChain->SetBranchAddress("calojetAlphaMax", calojetAlphaMax, &b_calojetAlphaMax);
   fChain->SetBranchAddress("calojetBetaMax", calojetBetaMax, &b_calojetBetaMax);
   fChain->SetBranchAddress("calojetGammaMax_ET", calojetGammaMax_ET, &b_calojetGammaMax_ET);
   fChain->SetBranchAddress("calojetGammaMax_EM", calojetGammaMax_EM, &b_calojetGammaMax_EM);
   fChain->SetBranchAddress("calojetGammaMax_Hadronic", calojetGammaMax_Hadronic, &b_calojetGammaMax_Hadronic);
   fChain->SetBranchAddress("calojetGammaMax", calojetGammaMax, &b_calojetGammaMax);
   fChain->SetBranchAddress("calojet_HadronicEnergyFraction", calojet_HadronicEnergyFraction, &b_calojet_HadronicEnergyFraction);
   fChain->SetBranchAddress("calojet_EMEnergyFraction", calojet_EMEnergyFraction, &b_calojet_EMEnergyFraction);
   fChain->SetBranchAddress("calojetPtAllTracks", calojetPtAllTracks, &b_calojetPtAllTracks);
   fChain->SetBranchAddress("calojetPtAllPVTracks", calojetPtAllPVTracks, &b_calojetPtAllPVTracks);
   fChain->SetBranchAddress("calojetMedianTheta2D", calojetMedianTheta2D, &b_calojetMedianTheta2D);
   fChain->SetBranchAddress("calojetMedianIP", calojetMedianIP, &b_calojetMedianIP);
   fChain->SetBranchAddress("calojetMinDeltaRAllTracks", calojetMinDeltaRAllTracks, &b_calojetMinDeltaRAllTracks);
   fChain->SetBranchAddress("calojetMinDeltaRPVTracks", calojetMinDeltaRPVTracks, &b_calojetMinDeltaRPVTracks);
   fChain->SetBranchAddress("nFatJets", &nFatJets, &b_nFatJets);
   fChain->SetBranchAddress("fatJetE", &fatJetE, &b_fatJetE);
   fChain->SetBranchAddress("fatJetPt", &fatJetPt, &b_fatJetPt);
   fChain->SetBranchAddress("fatJetEta", &fatJetEta, &b_fatJetEta);
   fChain->SetBranchAddress("fatJetPhi", &fatJetPhi, &b_fatJetPhi);
   fChain->SetBranchAddress("fatJetCorrectedPt", &fatJetCorrectedPt, &b_fatJetCorrectedPt);
   fChain->SetBranchAddress("fatJetPrunedM", &fatJetPrunedM, &b_fatJetPrunedM);
   fChain->SetBranchAddress("fatJetTrimmedM", &fatJetTrimmedM, &b_fatJetTrimmedM);
   fChain->SetBranchAddress("fatJetFilteredM", &fatJetFilteredM, &b_fatJetFilteredM);
   fChain->SetBranchAddress("fatJetSoftDropM", &fatJetSoftDropM, &b_fatJetSoftDropM);
   fChain->SetBranchAddress("fatJetCorrectedSoftDropM", &fatJetCorrectedSoftDropM, &b_fatJetCorrectedSoftDropM);
   fChain->SetBranchAddress("fatJetUncorrectedSoftDropM", &fatJetUncorrectedSoftDropM, &b_fatJetUncorrectedSoftDropM);
   fChain->SetBranchAddress("fatJetTau1", &fatJetTau1, &b_fatJetTau1);
   fChain->SetBranchAddress("fatJetTau2", &fatJetTau2, &b_fatJetTau2);
   fChain->SetBranchAddress("fatJetTau3", &fatJetTau3, &b_fatJetTau3);
   fChain->SetBranchAddress("fatJetMaxSubjetCSV", &fatJetMaxSubjetCSV, &b_fatJetMaxSubjetCSV);
   fChain->SetBranchAddress("fatJetPassIDLoose", &fatJetPassIDLoose, &b_fatJetPassIDLoose);
   fChain->SetBranchAddress("fatJetPassIDTight", &fatJetPassIDTight, &b_fatJetPassIDTight);
   fChain->SetBranchAddress("metPt", &metPt, &b_metPt);
   fChain->SetBranchAddress("metPhi", &metPhi, &b_metPhi);
   fChain->SetBranchAddress("sumMET", &sumMET, &b_sumMET);
   fChain->SetBranchAddress("metType0Pt", &metType0Pt, &b_metType0Pt);
   fChain->SetBranchAddress("metType0Phi", &metType0Phi, &b_metType0Phi);
   fChain->SetBranchAddress("metType1Pt_raw", &metType1Pt_raw, &b_metType1Pt_raw);
   fChain->SetBranchAddress("metType1Pt", &metType1Pt, &b_metType1Pt);
   fChain->SetBranchAddress("metType1Px", &metType1Px, &b_metType1Px);
   fChain->SetBranchAddress("metType1Py", &metType1Py, &b_metType1Py);
   fChain->SetBranchAddress("metType1Eta", &metType1Eta, &b_metType1Eta);
   fChain->SetBranchAddress("metType1Phi", &metType1Phi, &b_metType1Phi);
   fChain->SetBranchAddress("metType1Phi_raw", &metType1Phi_raw, &b_metType1Phi_raw);
   fChain->SetBranchAddress("metType0Plus1Pt", &metType0Plus1Pt, &b_metType0Plus1Pt);
   fChain->SetBranchAddress("metType0Plus1Phi", &metType0Plus1Phi, &b_metType0Plus1Phi);
   fChain->SetBranchAddress("metNoHFPt", &metNoHFPt, &b_metNoHFPt);
   fChain->SetBranchAddress("metNoHFPhi", &metNoHFPhi, &b_metNoHFPhi);
   fChain->SetBranchAddress("metPuppiPt", &metPuppiPt, &b_metPuppiPt);
   fChain->SetBranchAddress("metPuppiPhi", &metPuppiPhi, &b_metPuppiPhi);
   fChain->SetBranchAddress("metCaloPt", &metCaloPt, &b_metCaloPt);
   fChain->SetBranchAddress("metCaloPhi", &metCaloPhi, &b_metCaloPhi);
   fChain->SetBranchAddress("Flag_HBHENoiseFilter", &Flag_HBHENoiseFilter, &b_Flag_HBHENoiseFilter);
   fChain->SetBranchAddress("Flag_HBHETightNoiseFilter", &Flag_HBHETightNoiseFilter, &b_Flag_HBHETightNoiseFilter);
   fChain->SetBranchAddress("Flag_HBHEIsoNoiseFilter", &Flag_HBHEIsoNoiseFilter, &b_Flag_HBHEIsoNoiseFilter);
   fChain->SetBranchAddress("Flag_badChargedCandidateFilter", &Flag_badChargedCandidateFilter, &b_Flag_badChargedCandidateFilter);
   fChain->SetBranchAddress("Flag_badMuonFilter", &Flag_badMuonFilter, &b_Flag_badMuonFilter);
   fChain->SetBranchAddress("Flag_badGlobalMuonFilter", &Flag_badGlobalMuonFilter, &b_Flag_badGlobalMuonFilter);
   fChain->SetBranchAddress("Flag_duplicateMuonFilter", &Flag_duplicateMuonFilter, &b_Flag_duplicateMuonFilter);
   fChain->SetBranchAddress("Flag_CSCTightHaloFilter", &Flag_CSCTightHaloFilter, &b_Flag_CSCTightHaloFilter);
   fChain->SetBranchAddress("Flag_hcalLaserEventFilter", &Flag_hcalLaserEventFilter, &b_Flag_hcalLaserEventFilter);
   fChain->SetBranchAddress("Flag_EcalDeadCellTriggerPrimitiveFilter", &Flag_EcalDeadCellTriggerPrimitiveFilter, &b_Flag_EcalDeadCellTriggerPrimitiveFilter);
   fChain->SetBranchAddress("Flag_EcalDeadCellBoundaryEnergyFilter", &Flag_EcalDeadCellBoundaryEnergyFilter, &b_Flag_EcalDeadCellBoundaryEnergyFilter);
   fChain->SetBranchAddress("Flag_goodVertices", &Flag_goodVertices, &b_Flag_goodVertices);
   fChain->SetBranchAddress("Flag_trackingFailureFilter", &Flag_trackingFailureFilter, &b_Flag_trackingFailureFilter);
   fChain->SetBranchAddress("Flag_eeBadScFilter", &Flag_eeBadScFilter, &b_Flag_eeBadScFilter);
   fChain->SetBranchAddress("Flag_ecalLaserCorrFilter", &Flag_ecalLaserCorrFilter, &b_Flag_ecalLaserCorrFilter);
   fChain->SetBranchAddress("Flag_trkPOGFilters", &Flag_trkPOGFilters, &b_Flag_trkPOGFilters);
   fChain->SetBranchAddress("Flag_trkPOG_manystripclus53X", &Flag_trkPOG_manystripclus53X, &b_Flag_trkPOG_manystripclus53X);
   fChain->SetBranchAddress("Flag_trkPOG_toomanystripclus53X", &Flag_trkPOG_toomanystripclus53X, &b_Flag_trkPOG_toomanystripclus53X);
   fChain->SetBranchAddress("Flag_trkPOG_logErrorTooManyClusters", &Flag_trkPOG_logErrorTooManyClusters, &b_Flag_trkPOG_logErrorTooManyClusters);
   fChain->SetBranchAddress("Flag_BadPFMuonFilter", &Flag_BadPFMuonFilter, &b_Flag_BadPFMuonFilter);
   fChain->SetBranchAddress("Flag_BadChargedCandidateFilter", &Flag_BadChargedCandidateFilter, &b_Flag_BadChargedCandidateFilter);
   fChain->SetBranchAddress("Flag_ecalBadCalibFilter", &Flag_ecalBadCalibFilter, &b_Flag_ecalBadCalibFilter);
   fChain->SetBranchAddress("Flag_METFilters", &Flag_METFilters, &b_Flag_METFilters);
   fChain->SetBranchAddress("HLTDecision", HLTDecision, &b_HLTDecision);
   fChain->SetBranchAddress("HLTPrescale", HLTPrescale, &b_HLTPrescale);
   fChain->SetBranchAddress("nGenJets", &nGenJets, &b_nGenJets);
   fChain->SetBranchAddress("genJetE", genJetE, &b_genJetE);
   fChain->SetBranchAddress("genJetPt", genJetPt, &b_genJetPt);
   fChain->SetBranchAddress("genJetEta", genJetEta, &b_genJetEta);
   fChain->SetBranchAddress("genJetPhi", genJetPhi, &b_genJetPhi);
   fChain->SetBranchAddress("genMetPtCalo", &genMetPtCalo, &b_genMetPtCalo);
   fChain->SetBranchAddress("genMetPhiCalo", &genMetPhiCalo, &b_genMetPhiCalo);
   fChain->SetBranchAddress("genMetPtTrue", &genMetPtTrue, &b_genMetPtTrue);
   fChain->SetBranchAddress("genMetPhiTrue", &genMetPhiTrue, &b_genMetPhiTrue);
   fChain->SetBranchAddress("genVertexX", &genVertexX, &b_genVertexX);
   fChain->SetBranchAddress("genVertexY", &genVertexY, &b_genVertexY);
   fChain->SetBranchAddress("genVertexZ", &genVertexZ, &b_genVertexZ);
   fChain->SetBranchAddress("genVertexT", &genVertexT, &b_genVertexT);
   fChain->SetBranchAddress("genWeight", &genWeight, &b_genWeight);
   fChain->SetBranchAddress("genSignalProcessID", &genSignalProcessID, &b_genSignalProcessID);
   fChain->SetBranchAddress("genQScale", &genQScale, &b_genQScale);
   fChain->SetBranchAddress("genAlphaQCD", &genAlphaQCD, &b_genAlphaQCD);
   fChain->SetBranchAddress("genAlphaQED", &genAlphaQED, &b_genAlphaQED);
   fChain->SetBranchAddress("scaleWeights", &scaleWeights, &b_scaleWeights);
   fChain->SetBranchAddress("pdfWeights", &pdfWeights, &b_pdfWeights);
   fChain->SetBranchAddress("alphasWeights", &alphasWeights, &b_alphasWeights);
   fChain->SetBranchAddress("nGenParticle", &nGenParticle, &b_nGenParticle);
   fChain->SetBranchAddress("gParticleMotherId", gParticleMotherId, &b_gParticleMotherId);
   fChain->SetBranchAddress("gParticleMotherIndex", gParticleMotherIndex, &b_gParticleMotherIndex);
   fChain->SetBranchAddress("gParticleId", gParticleId, &b_gParticleId);
   fChain->SetBranchAddress("gParticleStatus", gParticleStatus, &b_gParticleStatus);
   fChain->SetBranchAddress("gParticleE", gParticleE, &b_gParticleE);
   fChain->SetBranchAddress("gParticlePt", gParticlePt, &b_gParticlePt);
   fChain->SetBranchAddress("gParticlePx", gParticlePx, &b_gParticlePx);
   fChain->SetBranchAddress("gParticlePy", gParticlePy, &b_gParticlePy);
   fChain->SetBranchAddress("gParticlePz", gParticlePz, &b_gParticlePz);
   fChain->SetBranchAddress("gParticleEta", gParticleEta, &b_gParticleEta);
   fChain->SetBranchAddress("gParticlePhi", gParticlePhi, &b_gParticlePhi);
   fChain->SetBranchAddress("gParticleProdVertexX", gParticleProdVertexX, &b_gParticleProdVertexX);
   fChain->SetBranchAddress("gParticleProdVertexY", gParticleProdVertexY, &b_gParticleProdVertexY);
   fChain->SetBranchAddress("gParticleProdVertexZ", gParticleProdVertexZ, &b_gParticleProdVertexZ);
   fChain->SetBranchAddress("gLLP_prod_vertex_x", gLLP_prod_vertex_x, &b_gLLP_prod_vertex_x);
   fChain->SetBranchAddress("gLLP_prod_vertex_y", gLLP_prod_vertex_y, &b_gLLP_prod_vertex_y);
   fChain->SetBranchAddress("gLLP_prod_vertex_z", gLLP_prod_vertex_z, &b_gLLP_prod_vertex_z);
   fChain->SetBranchAddress("gLLP_decay_vertex_x", gLLP_decay_vertex_x, &b_gLLP_decay_vertex_x);
   fChain->SetBranchAddress("gLLP_decay_vertex_y", gLLP_decay_vertex_y, &b_gLLP_decay_vertex_y);
   fChain->SetBranchAddress("gLLP_decay_vertex_z", gLLP_decay_vertex_z, &b_gLLP_decay_vertex_z);
   fChain->SetBranchAddress("gLLP_beta", gLLP_beta, &b_gLLP_beta);
   fChain->SetBranchAddress("gLLP_e", gLLP_e, &b_gLLP_e);
   fChain->SetBranchAddress("gLLP_pt", gLLP_pt, &b_gLLP_pt);
   fChain->SetBranchAddress("gLLP_eta", gLLP_eta, &b_gLLP_eta);
   fChain->SetBranchAddress("gLLP_phi", gLLP_phi, &b_gLLP_phi);
   fChain->SetBranchAddress("gLLP_travel_time", gLLP_travel_time, &b_gLLP_travel_time);
   fChain->SetBranchAddress("gLLP_daughter_travel_time", gLLP_daughter_travel_time, &b_gLLP_daughter_travel_time);
   fChain->SetBranchAddress("gLLP_daughter_pt", gLLP_daughter_pt, &b_gLLP_daughter_pt);
   fChain->SetBranchAddress("gLLP_daughter_eta", gLLP_daughter_eta, &b_gLLP_daughter_eta);
   fChain->SetBranchAddress("gLLP_daughter_phi", gLLP_daughter_phi, &b_gLLP_daughter_phi);
   fChain->SetBranchAddress("gLLP_daughter_eta_ecalcorr", gLLP_daughter_eta_ecalcorr, &b_gLLP_daughter_eta_ecalcorr);
   fChain->SetBranchAddress("gLLP_daughter_phi_ecalcorr", gLLP_daughter_phi_ecalcorr, &b_gLLP_daughter_phi_ecalcorr);
   fChain->SetBranchAddress("gLLP_daughter_e", gLLP_daughter_e, &b_gLLP_daughter_e);
   fChain->SetBranchAddress("photon_travel_time", photon_travel_time, &b_photon_travel_time);
   fChain->SetBranchAddress("gen_time", gen_time, &b_gen_time);
   fChain->SetBranchAddress("gen_time_pv", gen_time_pv, &b_gen_time_pv);
   fChain->SetBranchAddress("gLLP_min_delta_r_match_calojet", gLLP_min_delta_r_match_calojet, &b_gLLP_min_delta_r_match_calojet);
   fChain->SetBranchAddress("gLLP_daughter_match_calojet_index", gLLP_daughter_match_calojet_index, &b_gLLP_daughter_match_calojet_index);
   fChain->SetBranchAddress("gLLP_daughter_match_jet_index", gLLP_daughter_match_jet_index, &b_gLLP_daughter_match_jet_index);
   fChain->SetBranchAddress("gLLP_min_delta_r_match_jet", gLLP_min_delta_r_match_jet, &b_gLLP_min_delta_r_match_jet);
   Notify();
}

Bool_t llp::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void llp::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t llp::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef llp_cxx
