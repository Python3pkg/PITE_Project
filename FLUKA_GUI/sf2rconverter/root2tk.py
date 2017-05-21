###----------------------------------------------------------------
#
"""
   -->file contains function for converting plots from 
      s2fr_lib to tkinter canvases
   -->proper function should be choosen to handle each plot

"""
#   @Patryk Pasterny
#   @Kamil Piastowicz
#
###-----------------------------------------------------------------

#import section
import tkinter as tk
from ROOT import TH2D, TH1F
from matplotlib.pyplot import hist2d, hist, plot, title
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from .sf2r_lib import plot_1d, plot_2d, plot_3d

#function for converting d1 plots - not tested - probably buggy as hell
def plot_1d_2canvas(plot,tkroot):
   if isinstance(plot,plot_1d):
      canvases = []
      histo=plot.get_histo()
      figure = Figure(figsize=(6,5), dpi=100) 
      subplot = figure.add_subplot(111)
      xaxis = histo.GetXaxis()
      x_max_value=xaxis.GetXmax()
      values_x = [histo.GetBinContent(i) for i in range(1, xaxis.GetNbins())]
#header = plot.get_parser().get_header_info()
#bins = header['BINS']
      x = [float(i)/xaxis.GetNbins()*x_max_value for i in range(0,len(values_x))]	
      subplot.plot(x, values_x,drawstyle='steps-mid')
      subplot.text(3,0.4,histo.GetName())
      print(type(figure))
      canvases.append(FigureCanvasTkAgg(figure,master=tkroot))
      return canvases
   else:
      canvases=[]
      figure = Figure(figsize=(5,5), dpi=100)
      subplot = figure.add_subplot(111)

      xaxis = histo.GetXaxis()
      values_x = [histo.GetBinContent(i) for i in range(1, xaxis.GetNbins()+1)]
#header = plot.get_parser().get_header_info()
#rbins = header['RBINS']
#x = [float(i)/rbins*7 for i in range(0,len(values_x))]
      x = [float(i)/xaxis.GetNbins()*7 for i in range(0,len(values_x))]
      subplot.plot(x,values_x,drawstyle='steps-mid')
      subplot.text(3,0.4,histo.GetName())
      canvases.append(FigureCanvasTkAgg(figure,master=tkroot))
      return canvases  

#function for converting 2d plots - not tested
def plot_2d_2canvas(plot,tkroot):
   if isinstance(plot,plot_2d):
      canvases = []
      histos=plot.get_histo()
      num_hist=len(histos)
      for histo in histos:
#TODO try to connect the size of display with sizes of plots
         if num_hist>=1 and num_hist<3:
          figure = Figure(figsize=(5,5), dpi=100)#TODO check how big Figure is needed to fill canvas 
          subplot = figure.add_subplot(111)
         elif num_hist>=3 and num_hist<5:
          figure = Figure(figsize=(5,3), dpi=100)
          subplot = figure.add_subplot(111)         
         elif num_hist>=5 and num_hist <7:
          figure = Figure(figsize=(5,2.1), dpi=100)
          subplot = figure.add_subplot(111)
         elif num_hist>=7 and num_hist<9:
          figure = Figure(figsize=(3.5,2.1), dpi=100)#TODO check how big Figure is needed to fill canvas 
          subplot = figure.add_subplot(111)
	 yaxis = histo.GetXaxis()
	 zaxis = histo.GetYaxis()
	 values_y = [histo.GetBinContent(i) for i in range(1, xaxis.GetNbins()+1)]
	 values_z = [histo.GetBinContent(i) for i in range(1, yaxis.GetNbins()+1)]
	 #header = plot.get_parser().get_header_info()
	 #ybins = header['YBINS']
	 #zbins = header['ZBINS']
	 xy = [float(i)/xaxis.GetNbins()*7 for i in range(0,len(values_y))]
	 xz = [float(i)/yaxis.GetNbins()*7 for i in range(0,len(values_z))]
	 subplot.plot(xy,values_y,drawstyle='steps-mid')
	 subplot.plot(xz,values_z,drawstyle='steps-mid')
         subplot.text(3,0.4,histo.GetName())
	 canvases.append(FigureCanvasTkAgg(figure,master=tkroot))
      return canvases
   else:
      canvases=[]
      num_hist=len(plot)
      for histo in plot:
#TODO try to connect the size of display with sizes of plots
         if num_hist>=1 and num_hist<3:
          figure = Figure(figsize=(5,5), dpi=100)#TODO check how big Figure is needed to fill canvas 
          subplot = figure.add_subplot(111)
         elif num_hist>=3 and num_hist<5:
          figure = Figure(figsize=(5,3), dpi=100)
          subplot = figure.add_subplot(111)         
         elif num_hist>=5 and num_hist <7:
          figure = Figure(figsize=(5,2.1), dpi=100)
          subplot = figure.add_subplot(111)
         elif num_hist>=7 and num_hist<9:
          figure = Figure(figsize=(3.5,2.1), dpi=100)#TODO check how big Figure is needed to fill canvas 
          subplot = figure.add_subplot(111)
	 yaxis = histo.GetXaxis()
	 zaxis = histo.GetYaxis()
	 values_y = [histo.GetBinContent(i) for i in range(1, xaxis.GetNbins()+1)]
	 values_z = [histo.GetBinContent(i) for i in range(1, yaxis.GetNbins()+1)]
	 #header = plot.get_parser().get_header_info()
	 #ybins = header['YBINS']
	 #zbins = header['ZBINS']
	 xy = [float(i)/xaxis.GetNbins()*7 for i in range(0,len(values_y))]
	 xz = [float(i)/yaxis.GetNbins()*7 for i in range(0,len(values_z))]
	 subplot.plot(xy,values_y,drawstyle='steps-mid')
	 subplot.plot(xz,values_z,drawstyle='steps-mid')
         subplot.text(3,0.4,histo.GetName())
	 canvases.append(FigureCanvasTkAgg(figure,master=tkroot))
      return canvases

#function for converting 3d plots
def plot_3d_2canvas(plot,tkroot):
   if isinstance(plot,plot_3d):
      canvases = []
      histos=plot.get_histo()
      num_hist=len(histos)
      for histo in histos:
#TODO try to connect the size of display with sizes of plots
         if num_hist>=1 and num_hist<3:
          figure = Figure(figsize=(5,5), dpi=100)#TODO check how big Figure is needed to fill canvas 
          subplot = figure.add_subplot(111)
         elif num_hist>=3 and num_hist<5:
          figure = Figure(figsize=(5,3), dpi=100)
          subplot = figure.add_subplot(111)
         elif num_hist>=5 and num_hist <7:
          figure = Figure(figsize=(5,2.1), dpi=100)
          subplot = figure.add_subplot(111)
         elif num_hist>=7 and num_hist<9:
          figure = Figure(figsize=(3.5,2.1), dpi=100)#TODO check how big Figure is needed to fill canvas 
          subplot = figure.add_subplot(111)
	 xaxis = histo.GetXaxis()
	 values_x = [histo.GetBinContent(i) for i in range(1, xaxis.GetNbins()+1)]
	 #header = plot.get_parser().get_header_info()
	 #rbins = header['RBINS']
	 #x = [float(i)/rbins*7 for i in range(0,len(values_x))]
	 x = [float(i)/xaxis.GetNbins()*7 for i in range(0,len(values_x))]
	 subplot.plot(x,values_x,drawstyle='steps-mid')
         subplot.text(3,0.4,histo.GetName())
	 canvases.append(FigureCanvasTkAgg(figure,master=tkroot))
      return canvases

   else:
      canvases=[]
      num_hist=len(plot)
      for histo in plot:
#TODO try to connect the size of display with sizes of plots
         if num_hist>=1 and num_hist<3:
          figure = Figure(figsize=(5,5), dpi=100)#TODO check how big Figure is needed to fill canvas 
          subplot = figure.add_subplot(111)
         elif num_hist>=3 and num_hist<5:
          figure = Figure(figsize=(5,3), dpi=100)
          subplot = figure.add_subplot(111)         
         elif num_hist>=5 and num_hist <7:
          figure = Figure(figsize=(5,2.1), dpi=100)
          subplot = figure.add_subplot(111)
         elif num_hist>=7 and num_hist<9:
          figure = Figure(figsize=(3.5,2.1), dpi=100)#TODO check how big Figure is needed to fill canvas 
          subplot = figure.add_subplot(111)
	 xaxis = histo.GetXaxis()
         x_max_value=xaxis.GetXmax()
	 values_x = [histo.GetBinContent(i) for i in range(1, xaxis.GetNbins()+1)]
	 #header = plot.get_parser().get_header_info()
	 #rbins = header['RBINS']
	 #x = [float(i)/rbins*7 for i in range(0,len(values_x))]
	 x = [float(i)/xaxis.GetNbins()*x_max_value for i in range(0,len(values_x))]
	 subplot.plot(x,values_x,drawstyle='steps-mid')
         subplot.text(3,0.4,histo.GetName())
	 canvases.append(FigureCanvasTkAgg(figure,master=tkroot))
      return canvases  

#program test
if __name__ == "__main__":
 print('test?')
