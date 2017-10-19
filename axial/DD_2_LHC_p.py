from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TFile, TH2F, TF3, TGraph2D, TRandom
from ROOT import gROOT, gBenchmark
from array import array
import sys
import math
import ROOT


c1 = TCanvas( 'c1', 'c', 800, 700)


#whole bunch of defintions
gDM = 1.
gu=gd=gs = 1
mn, conv_units =0.938, 2.568*pow(10.,27.)
Delta_d_p, Delta_u_p, Delta_s_p = -0.42, 0.85, -0.08


mmed_l=[]
mdm_l=[]
for line in open("input/PICOSD_p.dat"):
   elems = line.split();
   mDM = float(elems[0])
   sigma = float(elems[1])*conv_units
   mu_nDM=mn*mDM/(mn+mDM)
   f=abs(gDM*(gu*Delta_u_p+gd*Delta_d_p+gs*Delta_s_p))
   mMed=pow(f*mu_nDM,0.5)/pow(math.pi*sigma/3.,0.25);
   mmed_l.append(float(mMed))
   mdm_l.append(float(mDM))
   print str(mMed)+" "+str(mDM)
mmed_r = array('d',mmed_l)
mdm_r = array('d',mdm_l)
dt = ROOT.TGraph(len(mmed_r), mmed_r, mdm_r)

dt.SetTitle("DD2LHC Pico (p, axial);m_{Med};m_{DM}");
c1.SetLogy()
dt.SetLineWidth(2)
dt.Draw("APL");
c1.Update()
c1.SaveAs("DD_2_LHC_p.png")
c1.SaveAs("DD_2_LHC_p.pdf")
