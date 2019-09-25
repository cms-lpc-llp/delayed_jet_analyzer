#include <iostream>
//ROOT
#include <TROOT.h>
#include <TFile.h>
#include <TDirectory.h>
#include <TTree.h>
//LOCAL
#include <llp.h>
#include <CommandLineInput.hh>

int main(int argc, char** argv )
{
  gROOT->Reset();
  //------------------
  //get root file name
  //------------------
  std::string  fname = ParseCommandLine( argc, argv, "-fname=" );
  if (  fname == "" )
  {
    std::cerr << "[ERROR]: please provide a file name --fname=<path_to_file.root>" << std::endl;
    return -1;
  }

  std::string  out_file_name = ParseCommandLine( argc, argv, "-out_file_name=" );
  if (  out_file_name == "" )
  {
    std::cerr << "[ERROR]: please provide a file name --out_file_name=<path_to_file.root>" << std::endl;
    return -1;
  }

  //LOAD FILE AND TTree
  TFile* fin = new TFile(fname.c_str(), "READ");
  TTree* tree = (TTree*)(((TDirectory*)fin->Get("ntuples"))->Get("llp"));

  //create llp Object
  llp* my_llp = new llp(tree);
  my_llp->Loop(out_file_name);
  fin->Close();
  return 0;
}
