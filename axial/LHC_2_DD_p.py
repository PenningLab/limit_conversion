from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TFile, TH2F, TF3, TGraph2D, TRandom
from ROOT import gROOT, gBenchmark
from array import array
import sys
import math
import ROOT

c1 = TCanvas( 'c1', 'c', 800, 700)


#whole bunch of defintions
gDM = 1.
gu=gd=gs = 1.
mn, conv_units =0.938, 2.568*pow(10.,27.) 
Delta_d_p, Delta_u_p, Delta_s_p = -0.42, 0.85, -0.08


sigma_l=[]
mdm_l=[]
for line in open("input/mMedmDM2.dat"):
   elems = line.split();
   mMed = float(elems[0])
   mDM = float(elems[1])
   mu_nDM=mn*mDM/(mn+mDM)

 
   f=gDM*(gu*Delta_u_p+gd*Delta_d_p+gs*Delta_s_p)
   sigmainGeV=3*pow(f*mu_nDM,2.)/(math.pi*pow(mMed,4.));
   sigmaincm=sigmainGeV/conv_units;
#   mmed_l.append(float(mMed))
   sigma_l.append(float(sigmaincm))
   mdm_l.append(float(mDM))
   print str(sigmaincm)+" "+str(mDM)




sigma_r = array('d',sigma_l)
mdm_r = array('d',mdm_l)
dt = ROOT.TGraph(len(sigma_r), mdm_r, sigma_r)

dt.SetTitle("DD2LHC proton (p, axial);m_{DM};sigma_{DM}");
c1.SetLogy()
c1.SetLogx()
dt.SetLineWidth(2)
dt.Draw("APL");
c1.Update()
c1.SaveAs("LHC_2_DD_p.png")
c1.SaveAs("LHC_2_DD_p.pdf")
