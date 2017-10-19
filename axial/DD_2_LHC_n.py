from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TFile, TH2F, TF3, TGraph2D, TRandom
from ROOT import gROOT, gBenchmark
from array import array
import sys
import math
import ROOT


c1 = TCanvas( 'c1', 'c', 800, 700)


#whole bunch of defintions
gDM = 1
gu=gd=gs= 0.25  #here this has quite some impact
#gu=gd=gs = 1
mn=0.938
Delta_d_n, Delta_u_n, Delta_s_n = -0.42, 0.85, -0.08
conv_units=2.568*pow(10.,27.)

mmed_l=[]
mdm_l=[]
for line in open("input/LUXSD_n.dat"):
   elems = line.split();
   mDM = float(elems[0])
   sigma = float(elems[1])*conv_units
   mu_nDM=mn*mDM/(mn+mDM)
   f=abs(gDM*(gu*Delta_u_n+gd*Delta_d_n+gs*Delta_s_n))
   print f
   mMed=pow(f*mu_nDM,0.5)/pow(math.pi*sigma/3.,0.25);
   mmed_l.append(float(mMed))
   mdm_l.append(float(mDM))
   print str(mMed)+" "+str(mDM)

mmed_r = array('d',mmed_l)
mdm_r = array('d',mdm_l)
dt = ROOT.TGraph(len(mmed_r), mmed_r, mdm_r)

dt.SetTitle("DD2LHC Lux (n, axial);m_{Med};m_{DM}");
dt.Draw("APL");

c1.Update()
c1.SaveAs("DD_2_LHC_n.png")
c1.SaveAs("DD_2_LHC_n.pdf")
