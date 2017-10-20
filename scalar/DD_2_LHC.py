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


mmed_l=[]
mdm_l=[]
for line in open("input/LUX1.dat"):
   elems = line.split();
   mDM = float(elems[0])
   sigma = float(elems[1])*conv_units
   mu_nDM=mn*mDM/(mn+mDM)
   #this is f*mMed^2
   fmMed2=(mn/v)*gSM*gDM*(fup+fdp+fsp+2./27.*fTG*3.);
   mMed=pow(fmMed2*mu_nDM,0.5)/pow(math.pi*sigma,0.25);
   mmed_l.append(float(mMed))
   mdm_l.append(float(mDM))
   print str(mMed)+" "+str(mDM)
mmed_r = array('d',mmed_l)
mdm_r = array('d',mdm_l)
dt = ROOT.TGraph(len(mmed_r), mmed_r, mdm_r)

dt.SetTitle("DD2LHC Lux (scalar);m_{Med};m_{DM}");
dt.Draw("APL");
c1.Update()
c1.SaveAs("DD_2_LHC.png")
c1.SaveAs("DD_2_LHC.pdf")
