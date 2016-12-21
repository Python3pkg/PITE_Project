###----------------------------------------------------------------
#
"""
   -->file contains function for converting plots from 
      s2fr_lib to tkinter canvases
   -->proper function should be choosen to handle each plot

"""
#
#   @Kamil Piastowicz
#
###-----------------------------------------------------------------

#import section
import Tkinter as tk
from ROOT import TH2D, TH1F
from matplotlib.pyplot import hist2d, hist, plot, title
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from sf2r_lib import plot_1d, plot_2d, plot_3d

#function for converting d1 plots - not tested - probably buggy as hell
def plot_1d_2canvas(plot,tkroot):
   if isinstance(plot,plot_1d):
      canvases = []
      for histo in plot.get_histo():
         figure = Figure(figsize=(5,3), dpi=100)#TODO check how big Figure is needed to fill canvas
         subplot = figure.add_subplot(111)
	 xaxis = histo.GetXaxis()
	 values_x = [histo.GetBinContent(i) for i in range(1, xaxis.GetNbins()+1)]
	 header = plot.get_parser().get_header_info()
	 bins = header['BINS']
	 x = [float(i)/rbins*7 for i in range(0,111)]	
	 subplot.plot(x, values_x)
         subplot.text(3,0.4,histo.GetName())
	 canvases.append(FigureCanvasTkAgg(figure,master=tkroot))
      return canvases
   else:
      return [[Canvas()]]

#function for converting 2d plots - not tested
def plot_2d_2canvas(plot,tkroot):
   if isinstance(plot,plot_2d):
      canvases = []
      for histo in plot.get_histo():
         figure = Figure(figsize=(5,3), dpi=100)#TODO check how big Figure is needed to fill canvas
         subplot = figure.add_subplot(111)
	 yaxis = histo.GetXaxis()
	 zaxis = histo.GetYaxis()
	 values_y = [histo.GetBinContent(i) for i in range(1, xaxis.GetNbins()+1)]
	 values_z = [histo.GetBinContent(i) for i in range(1, yaxis.GetNbins()+1)]
	 header = plot.get_parser().get_header_info()
	 ybins = header['YBINS']
	 zbins = header['ZBINS']
	 xy = [float(i)/ybins*7 for i in range(0,111)]
	 xz = [float(i)/zbins*7 for i in range(0,111)]
	 subplot.plot(x,values_y)
	 subplot.plot(x,values_z)
         subplot.text(3,0.4,histo.GetName())
	 canvases.append(FigureCanvasTkAgg(figure,master=tkroot))
      return canvases
   else:
      return [[Canvas()]]

#function for converting 3d plots
def plot_3d_2canvas(plot,tkroot):
   if isinstance(plot,plot_3d):
      canvases = []
      for histo in plot.get_histo():
         figure = Figure(figsize=(5,3), dpi=100)#TODO check how big Figure is needed to fill canvas 
         subplot = figure.add_subplot(111)
	 xaxis = histo.GetXaxis()
	 values_x = [histo.GetBinContent(i) for i in range(1, xaxis.GetNbins()+1)]
	 header = plot.get_parser().get_header_info()
	 rbins = header['RBINS']
	 x = [float(i)/rbins*7 for i in range(0,111)]
	 subplot.plot(x,values_x)
         subplot.text(3,0.4,histo.GetName())
	 canvases.append(FigureCanvasTkAgg(figure,master=tkroot))
      return canvases
   else:
      return [[Canvas()]]

#program test
if __name__ == "__main__":
 print 'test?'
