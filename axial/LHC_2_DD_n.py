#Christopher McCabe, converted and adapter Bjoern Penning
#Read in from the mDM - mMed plane and translate to the direct detection plane
# for the axial mediator
#translates to the neutron cross-section
#assumes the Lagrangian is the same as eq 2.2 of arXiv:1407.8257

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
for line in open("input/mMedmDM1.dat"):
   elems = line.split();
   mMed = float(elems[0])
   mDM = float(elems[1])
   mu_nDM=mn*mDM/(mn+mDM)

 
   f=gDM*(gu*Delta_u_p+gd*Delta_d_p+gs*Delta_s_p)
   sigmainGeV=3*pow(f*mu_nDM,2.)/(math.pi*pow(mMed,4.));
   sigmaincm=sigmainGeV/conv_units;
   sigma_l.append(float(sigmaincm))
   mdm_l.append(float(mDM))
   print str(sigmaincm)+" "+str(mDM)




sigma_r = array('d',sigma_l)
mdm_r = array('d',mdm_l)
dt = ROOT.TGraph(len(sigma_r), mdm_r, sigma_r)

dt.SetTitle("DD2LHC n (n, axial);m_{DM};sigma_{DM}");
c1.SetLogy()
c1.SetLogx()
dt.SetLineWidth(2)
dt.Draw("APL");
c1.Update()
c1.SaveAs("LHC_2_DD_n.png")
c1.SaveAs("LHC_2_DD_n.pdf")




