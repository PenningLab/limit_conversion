#Christopher McCabe, converted and updated by Bjoern Penning
#Read in from the mDM - mMed plane and translate to direct detection
#for the scalar mediator
#assumes Lagrangian is the same as in eq 2.1 of arXiv:1503.00691


from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TFile, TH2F, TF3, TGraph2D, TRandom
from ROOT import gROOT, gBenchmark
from array import array
import sys
import math
import ROOT


c1 = TCanvas( 'c1', 'c', 800, 700)


#whole bunch of defintions
gDM = 1.
gSM = 1.
mn, conv_units =0.938, 2.568*pow(10.,27.)
v=246; #Higgs vev in GeV
fup, fdp = 0.0208, 0.0411; #from arXiv:1506.04142
fsp=0.043; #from arXiv:1301.1114
fTG=1-fup-fdp-fsp;


sigma_l=[]
mdm_l=[]
for line in open("input/mMedmDM.dat"):
   elems = line.split();
   mMed = float(elems[0])
   mDM = float(elems[1])
   mu_nDM=mn*mDM/(mn+mDM)
   f=(mn/v)*gSM*gDM*(fup+fdp+fsp+2./27.*fTG*3.)/pow(mMed,2.0);
   sigmainGeV=pow(f*mu_nDM,2.)/(math.pi);
   sigmaincm=sigmainGeV/conv_units;

   
   sigma_l.append(float(sigmaincm))
   mdm_l.append(float(mDM))
   print str(mDM)+" "+str(sigmaincm)
msigma_r = array('d',sigma_l)
mdm_r = array('d',mdm_l)
dt = ROOT.TGraph(len(msigma_r), mdm_r, msigma_r)

dt.SetTitle("DD2LHC Lux (scalar);m_{DM},#sigma");
dt.Draw("APL");
c1.Update()
c1.SaveAs("DD_2_LHC.png")
c1.SaveAs("DD_2_LHC.pdf")
