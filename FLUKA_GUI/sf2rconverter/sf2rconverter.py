###-------------------------------------------------------------------
#
""" 
   --> smart fluka to root histogram converter, it can iterate over
       any number of files containg data from fluka for both 1d and 2d
       deposit projections
   --> it is presumed that the file with memory map will always have
       extension .lis!

"""
#
#  @Agnieszka Oblakowska-Mucha
#  @Tomasz Szumlak
#
###--------------------------------------------------------------------

# import section
import os, sys, getopt
from subprocess import getoutput
from .sf2r_lib import sf2r_manager
from ROOT import TFile, gPad, TCanvas, gStyle

DEBUG = False
PLOT1D = True
PLOT2D = True
PLOT3D = True

# this is the converter manager code
#---
if __name__ == '__main__':
   # configure and run
   _MGR = sf2r_manager( DEBUG )
   _MGR.ff_type_detector()
   plots = _MGR.run()
   file = None
   if not os.path.exists( 'fluka2root.root' ):
       file = TFile( 'fluka2root.root', 'new' )
   else:
       file = TFile( 'fluka2root.root', 'recreate' )

   # set for apperance
   c = TCanvas('f2r_test', 'f2r Test', 600, 400)
   gStyle.SetPalette(1)
   gStyle.SetOptStat(0)
   gStyle.SetOptFit(0)

   # make a test plot and store plots in file
   for plot in plots:
       if plot.get_type() == '1DPLOT':
           if PLOT1D:
               plot.get_histo().Draw('P')
           plot.get_histo().Write()
       if plot.get_type() == '2DPLOT':
           if PLOT2D:
               gPad.SetLogz();
               gPad.SetGridx();
               gPad.SetGridy();
               plot.get_histo().Draw('COLZ')
           plot.get_histo().Write()
       if plot.get_type() == '3DPLOT':
           if PLOT3D:
               gPad.SetLogz();
               gPad.SetGridx();
               gPad.SetGridy();
               hist = plot.get_histo()
               for i in range(len(hist)):
                  hist[i].Draw()
                  input('Close the window and press enter')
                  hist[i].Write()

   file.Close()

   print(' --> Press enter to finish... ')
   input()





   

