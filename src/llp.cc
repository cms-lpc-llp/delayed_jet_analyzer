#define llp_cxx
#include "llp.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void llp::Loop(TString outFileName)
{
//   In a ROOT session, you can do:
//      root> .L llp.C
//      root> llp t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch

  TFile* fout = new TFile(outFileName, "RECREATE");
  TH1F* h_higgs_pt = new TH1F("h_higgs_pt","higgs_pt", 30, 0, 1000);
  TH1F* h_higgs_pt_met120 = new TH1F("h_higgs_pt_met120","higgs_pt_met120", 30, 0, 1000);
  TH1F* h_higgs_pt_displaced = new TH1F("h_higgs_pt_displaced","higgs_pt_displaced", 30, 0, 1000);

  //MET
  TH1F* h_met = new TH1F("h_met","met", 30, 0, 1000);
  TH1F* h_met_met120 = new TH1F("h_met_met120","met_met120", 30, 0, 1000);
  TH1F* h_met_displaced = new TH1F("h_met_displaced","met_displaced", 30, 0, 1000);

  //HT
  TH1F* h_ht = new TH1F("h_ht","ht", 100, 0, 1000);
  TH1F* h_ht_met120 = new TH1F("h_ht_met120","ht_met120", 100, 0, 1000);
  TH1F* h_ht_displaced = new TH1F("h_ht_displaced","ht_displaced", 100, 0, 1000);

  //2D
  TH2F* h_met_vs_higg_pt = new TH2F("h_met_vs_higg_pt", "met_vs_higg_pt",
  100, 0, 1000, 100, 0, 1000);
  TH2F* h_met_vs_ht = new TH2F("h_met_vs_ht", "met_vs_ht",
  100, 0, 1000, 100, 0, 1000);
  TH2F* h_ht_vs_higg_pt = new TH2F("h_ht_vs_higg_pt", "ht_vs_higg_pt",
  100, 0, 1000, 100, 0, 1000);

  //lab frame
  TH1F* h_llp1_decay = new TH1F("h_llp1_decay","llp1_decay", 100, 0, 1e5);
  TH1F* h_llp2_decay = new TH1F("h_llp2_decay","llp2_decay", 100, 0, 1e5);
  //z
  TH1F* h_llp1_decay_z = new TH1F("h_llp1_decay_z","llp1_decay_z", 100, 0, 1e5);
  TH1F* h_llp2_decay_z = new TH1F("h_llp2_decay_z","llp2_decay_z", 100, 0, 1e5);
  //r
  TH1F* h_llp1_decay_r = new TH1F("h_llp1_decay_r","llp1_decay_r", 100, 0, 1e5);
  TH1F* h_llp2_decay_r = new TH1F("h_llp2_decay_r","llp2_decay_r", 100, 0, 1e5);
  //rest frame
  TH1F* h_llp1_decay_rf = new TH1F("h_llp1_decay_rf","llp1_decay_rf", 100, 0, 3e3);
  TH1F* h_llp2_decay_rf = new TH1F("h_llp2_decay_rf","llp2_decay_rf", 100, 0, 3e3);

  //gamma
  TH1F* h_gamma1 = new TH1F("h_gamma1","gamma1", 100, 0, 100);
  TH1F* h_gamma2 = new TH1F("h_gamma2","gamma2", 100, 0, 100);
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;



      h_met->Fill(metType1Pt);
      if(HLTDecision[467])h_met_met120->Fill(metType1Pt);
      if(HLTDecision[601])h_met_displaced->Fill(metType1Pt);

      //compute HT
      double ht = 0.0;
      for(int ijet = 0; ijet < nJets; ijet++)
      {
        ht += jetPt[ijet];
      }

      h_ht->Fill(ht);
      if(HLTDecision[467])h_ht_met120->Fill(ht);
      if(HLTDecision[601])h_ht_displaced->Fill(ht);

      //2D


      for( int igen = 0; igen < nGenParticle; igen++ )
      {
        if(!(gParticleId[igen]==25))continue;
        h_higgs_pt->Fill(gParticlePt[igen]);
        if(HLTDecision[467])h_higgs_pt_met120->Fill(gParticlePt[igen]);
        if(HLTDecision[601])h_higgs_pt_displaced->Fill(gParticlePt[igen]);
        h_met_vs_higg_pt->Fill(metType1Pt,gParticlePt[igen]);
        h_ht_vs_higg_pt->Fill(ht,gParticlePt[igen]);
        h_met_vs_ht->Fill(metType1Pt,ht);
        break;
      }

      float gamma1 = 1./sqrt(1-pow(gLLP_beta[0],2.0));
      float gamma2 = 1./sqrt(1-pow(gLLP_beta[1],2.0));
      h_gamma1->Fill(gamma1);
      h_gamma2->Fill(gamma2);
      //llp1
      float llp1_decay = sqrt(pow(gLLP_decay_vertex_x[0],2.0)
      +pow(gLLP_decay_vertex_y[0],2.0)+pow(gLLP_decay_vertex_z[0],2.0));
      float llp1_decay_r = sqrt(pow(gLLP_decay_vertex_x[0],2.0)
      +pow(gLLP_decay_vertex_y[0],2.0));
      float llp1_decay_z = fabs(gLLP_decay_vertex_z[0]);
      float llp1_decay_rf = sqrt(pow(gLLP_decay_vertex_x[0],2.0)
      +pow(gLLP_decay_vertex_y[0],2.0)+pow(gLLP_decay_vertex_z[0],2.0))/(gLLP_beta[0]*gamma1);

      h_llp1_decay->Fill(llp1_decay);
      h_llp1_decay_r->Fill(llp1_decay_r);
      h_llp1_decay_z->Fill(llp1_decay_z);
      h_llp1_decay_rf->Fill(llp1_decay_rf);
      //llp2
      float llp2_decay = sqrt(pow(gLLP_decay_vertex_x[1],2.0)
      +pow(gLLP_decay_vertex_y[1],2.0)+pow(gLLP_decay_vertex_z[1],2.0));
      float llp2_decay_r = sqrt(pow(gLLP_decay_vertex_x[1],2.0)
      +pow(gLLP_decay_vertex_y[1],2.0));
      float llp2_decay_z = fabs(gLLP_decay_vertex_z[1]);
      float llp2_decay_rf = sqrt(pow(gLLP_decay_vertex_x[1],2.0)
      +pow(gLLP_decay_vertex_y[1],2.0)+pow(gLLP_decay_vertex_z[1],2.0))/(gLLP_beta[1]*gamma2);

      h_llp2_decay->Fill(llp2_decay);
      h_llp2_decay_r->Fill(llp2_decay_r);
      h_llp2_decay_z->Fill(llp2_decay_z);
      h_llp2_decay_rf->Fill(llp2_decay_rf);
      // if (Cut(ientry) < 0) continue;
   }

   h_higgs_pt->Write();
   h_higgs_pt_met120->Write();
   h_higgs_pt_displaced->Write();
   h_met->Write();
   h_met_met120->Write();
   h_met_displaced->Write();
   h_ht->Write();
   h_ht_met120->Write();
   h_ht_displaced->Write();

   //2d
   h_met_vs_higg_pt->Write();
   h_ht_vs_higg_pt->Write();
   h_met_vs_ht->Write();

   //llps
   h_llp1_decay->Write();
   h_llp1_decay_r->Write();
   h_llp1_decay_z->Write();
   h_llp1_decay_rf->Write();
   h_llp2_decay->Write();
   h_llp2_decay_r->Write();
   h_llp2_decay_z->Write();
   h_llp2_decay_rf->Write();
   h_gamma1->Write();
   h_gamma2->Write();
   fout->Close();
}
