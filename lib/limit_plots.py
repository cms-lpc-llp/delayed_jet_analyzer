import ROOT as rt
import numpy as np
from array import array
from scipy.interpolate import Rbf, interp1d
from scipy.interpolate import NearestNDInterpolator
from scipy.interpolate import LinearNDInterpolator

def interpolate2D(x,y,z,hist,epsilon=0.2,smooth=0,norm = 'euclidean', inter = 'linear'):

    binWidthX = float(hist.GetXaxis().GetBinWidth(1))
    binWidthY = float(hist.GetYaxis().GetBinWidth(1))

    mgMin = hist.GetXaxis().GetBinCenter(1)
    mgMax = hist.GetXaxis().GetBinCenter(hist.GetNbinsX())#+hist.GetXaxis().GetBinWidth(hist.GetNbinsX())
    mchiMin = hist.GetYaxis().GetBinCenter(1)
    mchiMax = hist.GetYaxis().GetBinCenter(hist.GetNbinsY())#+hist.GetYaxis().GetBinWidth(hist.GetNbinsY())

    myX = np.linspace(mgMin, mgMax, hist.GetNbinsX())
    myY = np.linspace(mchiMin, mchiMax, hist.GetNbinsY())
    myXI, myYI = np.meshgrid(myX,myY)

    if inter == 'linear':rbf = LinearNDInterpolator(list(zip(x, y)), z)
    else: rbf = Rbf(x, y, z, function='multiquadric', epsilon=epsilon,smooth=smooth, norm = norm)

    myZI = rbf(myXI, myYI)
    for i in range(1, hist.GetNbinsX()+1):
        for j in range(1, hist.GetNbinsY()+1):
            hist.SetBinContent(i,j,10**(myZI[j-1][i-1]))
    return hist


def log_scale_conversion(h):
    
    ##########################
    # convert x and y axis to mass/ctau
    ###########################

    oldX = []
    for i_bin in range(1, h.GetNbinsX()+1):
        oldX.append(h.GetXaxis().GetBinLowEdge(i_bin))
    oldX.append(h.GetXaxis().GetBinUpEdge(h.GetNbinsX()))
    
    oldY = []
    for i_bin in range(1, h.GetNbinsY()+1):
        oldY.append(h.GetYaxis().GetBinLowEdge(i_bin))
    oldY.append(h.GetYaxis().GetBinUpEdge(h.GetNbinsY()))
    
    myX = 10**np.array(oldX)
    myY = 10**np.array(oldY)
    h_new = rt.TH2D('', '', len(myX)-1, array('f',myX), len(myY)-1, array('f', myY))
    for i in range(1, h.GetNbinsX()+1):
        for j in range(1, h.GetNbinsY()+1):
            h_new.SetBinContent(i,j,h.GetBinContent(i,j))
    h_new.GetXaxis().SetTitle(h.GetXaxis().GetTitle())
    h_new.GetYaxis().SetTitle(h.GetYaxis().GetTitle())
    h_new.GetZaxis().SetTitle(h.GetZaxis().GetTitle())
    return h_new
def frameTH2D(hin,frameValue=1000,eps=0.001):
    xw = hin.GetXaxis().GetBinWidth(1)
    yw = hin.GetYaxis().GetBinWidth(1)
    nx = hin.GetNbinsX()
    ny = hin.GetNbinsY()
    x0 = hin.GetXaxis().GetXmin()
    x1 = hin.GetXaxis().GetXmax()
    y0 = hin.GetYaxis().GetXmin()
    y1 = hin.GetYaxis().GetXmax()
    xbins = array('d',[frameValue]*(nx+3))
    ybins = array('d',[frameValue]*(ny+3))
    xbins[0] = x0 - eps*xw - xw
    xbins[1] = x0 + eps*xw - xw;
    for ix in range(2, nx+1):
        xbins[ix] = x0 + (ix-1)*xw
    xbins[nx+1] = x1 - eps*xw + xw
    xbins[nx+2] = x1 + eps*xw + xw
    ybins[0] = y0 - eps*yw - yw
    ybins[1] = y0 + eps*yw - yw
    for iy in range(2, ny+1):
        ybins[iy] = y0 + (iy-1)*yw
    ybins[ny+1] = y1 - eps*yw + yw
    ybins[ny+2] = y1 + eps*yw + yw
    
    framed = rt.TH2D("%s framed"%hin.GetName(),"%s framed"%hin.GetTitle(),nx + 2, xbins,ny + 2, ybins)

    for ix in range(1, nx+1):
        for iy in range(1, ny+1):
            framed.SetBinContent(1+ix, 1+iy, hin.GetBinContent(ix,iy))

    nx = framed.GetNbinsX();
    ny = framed.GetNbinsY();
    for ix in range(1, nx+1):
        framed.SetBinContent(ix,  1, frameValue)
        framed.SetBinContent(ix, ny, frameValue)
    for iy in range(2, ny):
        framed.SetBinContent( 1, iy, frameValue)
        framed.SetBinContent(nx, iy, frameValue)
    return framed
