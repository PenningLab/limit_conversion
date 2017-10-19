#Original from Christopher McCabe 8 Dec 2015, converted to python and updated by Bjoern Penning
#Read in from the mDM - mMed plane and translate to the direct detection plane
#for the vector mediator
##assumes the Lagrangian is the same as eq 2.1 of arXiv:1407.8257

from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TFile, TH2F, TF3, TGraph2D, TRandom
from ROOT import gROOT, gBenchmark
from array import array
import sys
import math
import ROOT

c1 = TCanvas( 'c1', 'c', 800, 700)


#bunch of defintions
gDM = 1.
gu=gd=gs = 1.0
mn, conv_units =0.938, 2.568*pow(10.,27.)
Delta_d_p, Delta_u_p, Delta_s_p = -0.42, 0.85, -0.08


mmed_l=[]
mdm_l=[]
for line in open("input/LUX1.dat"):
   elems = line.split();
   mDM = float(elems[0])
   sigma = float(elems[1])*conv_units
   mu_nDM=mn*mDM/(mn+mDM)
   mMed=pow((2*gu+gd)*gDM*mu_nDM,0.5)/pow(math.pi*sigma,0.25);
   mmed_l.append(float(mMed))
   mdm_l.append(float(mDM))
   print str(mMed)+" "+str(mDM)
mmed_r = array('d',mmed_l)
mdm_r = array('d',mdm_l)
dt = ROOT.TGraph(len(mmed_r), mmed_r, mdm_r)

dt.SetTitle("DD2LHC Lux (vector);m_{Med};m_{DM}");
dt.Draw("APL");
c1.Update()
c1.SaveAs("DD_2_LHC.png")
c1.SaveAs("DD_2_LHC.pdf")
