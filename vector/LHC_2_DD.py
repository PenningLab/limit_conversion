#Original from Christopher McCabe, updated and converted by Bjoern Penning
#Read in from the mDM - mMed plane and translate to the direct detection plane
#for the vector mediator
#assumes the Lagrangian is the same as eq 2.1 of arXiv:1407.8257


from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TFile, TH2F, TF3, TGraph2D, TRandom
from ROOT import gROOT, gBenchmark
from array import array
import sys
import math
import ROOT

c1 = TCanvas( 'c1', 'c', 800, 700)

#define couplings
#define gu and gd separately to allow for them to differ
gDM=1.
gu=1.
gd=gu
mn=0.938
conv_units=2.568*pow(10.,27.)

sigma_l=[]
mdm_l=[]
for line in open("input/mMedmDM.dat"):
   elems = line.split();
   mMed = float(elems[0])
   mDM = float(elems[1])
   mu_nDM=mn*mDM/(mn+mDM)

   sigmainGeV=pow((2*gu+gd)*gDM*mu_nDM,2.)/(math.pi*pow(mMed,4.));
   sigmaincm=sigmainGeV/conv_units;

   sigma_l.append(float(sigmaincm))
   mdm_l.append(float(mDM))
   print str(mDM)+" "+str(sigmaincm)

sigma_r = array('d',sigma_l)
mdm_r = array('d',mdm_l)
dt = ROOT.TGraph(len(mdm_r), mdm_r, sigma_r )

dt.GetYaxis().SetRange(0, 1);
#dt.SetLogy()
dt.SetTitle("LHC2DD Lux (vector); m_{DM}; #sigma");
dt.Draw("APL");
c1.Update()
c1.SaveAs("LHC_2_DD.png")
c1.SaveAs("LHC_2_DD.pdf")
