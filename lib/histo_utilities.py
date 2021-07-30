import numpy as np
import ROOT as rt
import root_numpy as rtnp
import matplotlib.pyplot as plt
from array import array

std_color_list = [1, 2, 4, 8, 6, 28, 43, 7, 25, 36, 30, 40, 42, 49, 46, 38, 32, 800, 600, 900, 870, 840]

def quantile(a, p, weight=None, f=None):
    if a.shape[0] == 0:
        return None, None
    if weight is None:
        q = np.percentile(a, 100*p).astype(np.float64)
        weight = np.full_like(a, 1.0/a.shape[0], np.float64)
    else:
        i_sort = np.argsort(a)
        a = a[i_sort]
        weight = weight[i_sort]
        cum_sum = np.cumsum(weight, dtype=np.float128)
        idx_q = np.argmax(cum_sum>p*cum_sum[-1])
        q = a[idx_q]

        weight /= np.sum(weight)

    if not f==None:
        f_q = f(q)
    else:
        h = create_TH1D(a, binning=[None, np.percentile(a, 2), np.percentile(a, 98)], weights=weight)
        f_q = h.GetBinContent(h.FindBin(q))/h.GetBinWidth(h.FindBin(q))
    if f_q == 0:
        f_q = 1e-3
        print ('[ERROR]: Failed to estimate pdf')
    sigma_q = np.sqrt(p*(1-p)/(a.shape[0]*f_q**2))
    return q, sigma_q

def EstimateDispersion(aux, w=None):
    q_up, e_up = quantile(aux, 0.15, weight=w)
    q_dwn, e_dwn = quantile(aux, 0.85, weight=w)
    if q_up == None or q_dwn == None:
        print ('[WARNING] Quantile estimation failed')
        print (aux.shape)
        print (q_up, q_dwn)
    disp_est = 0.5*np.abs(q_up - q_dwn)
    disp_unc = 0.5*np.hypot(e_up, e_dwn)
    return disp_est, disp_unc

def create_TH1D(x, name='h', title=None, binning=[None, None, None], weights=None, h2clone=None, axis_title = ['',''], bin_list=False):
    if title is None:
        title = name
    if h2clone == None:
        if binning[1] is None:
            binning[1] = min(x)
        if binning[2] is None:
            if ((np.percentile(x, 95)-np.percentile(x, 50))<0.2*(max(x)-np.percentile(x, 95))):
                binning[2] = np.percentile(x, 90)
            else:
                binning[2] = max(x)
        if binning[0] is None:
            bin_w = 4*(np.percentile(x,75) - np.percentile(x,25))/(len(x))**(1./3.)
            if bin_w == 0:
                bin_w = 0.5*np.std(x)
            if bin_w == 0:
                bin_w = 1
            binning[0] = int((binning[2] - binning[1])/bin_w) + 5

        if len(binning) > 3 or bin_list:
            h = rt.TH1D(name, title, len(binning)-1, array('f',binning))
        else:
            h = rt.TH1D(name, title, binning[0], binning[1], binning[2])
    else:
        h = h2clone.Clone(name)
        h.SetTitle(title)
        h.Reset()

    rtnp.fill_hist(h, x, weights=weights)
    h.SetXTitle(axis_title[0])
    h.SetYTitle(axis_title[1])
    h.binning = binning
    return h

def create_prof1D(x, y, name='h', title=None, binning=[None, None, None], h2clone=None, axis_title = ['',''], opt=''):
    if title is None:
        title = name
    if h2clone == None:
        if binning[1] is None:
            binning[1] = min(x)
        if binning[2] is None:
            if ((np.percentile(x, 95)-np.percentile(x, 50))<0.2*(max(x)-np.percentile(x, 95))):
                binning[2] = np.percentile(x, 90)
            else:
                binning[2] = max(x)
        if binning[0] is None:
            bin_w = 4*(np.percentile(x,75) - np.percentile(x,25))/(len(x))**(1./3.)
            if bin_w == 0:
                bin_w = 0.5*np.std(x)
            if bin_w == 0:
                bin_w = 1
            binning[0] = int((binning[2] - binning[1])/bin_w) + 5

        h = rt.TH1D(name, title, binning[0], binning[1], binning[2])
    else:
        h = h2clone.Clone(name)
        h.SetTitle(title)
        h.Reset()

    for i in range(1, binning[0]+1):
        xl = h.GetBinCenter(i) - h.GetBinWidth(i)/2.
        xu = h.GetBinCenter(i) + h.GetBinWidth(i)/2.

        sel = np.logical_and(x<xu, x>xl)
        aux = y[sel]

        if len(aux) > 0:
            if 'Res' in opt:
                q_up, e_up = quantile(aux, 0.15)
                q_dwn, e_dwn = quantile(aux, 0.85)
                if q_up == None or q_dwn == None:
                    print ('[WARNING] Quantile estimation failed')
                    print (aux.shape)
                    print (q_up, q_dwn)
                    return
                disp_est = 0.5*np.abs(q_up - q_dwn)
                h.SetBinContent(i, disp_est)
                disp_unc = 0.5*np.hypot(e_up, e_dwn)
                h.SetBinError(i, disp_unc)
            else:
                h.SetBinContent(i, np.mean(aux))

                if 's' in opt:
                    q_up, e_up = quantile(aux, 0.15)
                    q_dwn, e_dwn = quantile(aux, 0.85)
                    if q_up == None or q_dwn == None:
                        print ('[WARNING] Quantile estimation failed')
                        print (aux.shape)
                        print (q_up, q_dwn)
                        return
                    disp_est = 0.5*np.abs(q_up - q_dwn)
                    h.SetBinError(i, disp_est)
                else:
                    h.SetBinError(i, np.std(aux)/np.sqrt(aux.shape[0]))

    h.SetXTitle(axis_title[0])
    h.SetYTitle(axis_title[1])
    h.binning = binning
    return h

def create_TH2D(sample, name='h', title=None, binning=[None, None, None, None, None, None], weights=None, axis_title = ['','', '']):
    if title is None:
        title = name
    if (sample.shape[0] == 0):
        for i in range(len(binning)):
            if binning[i] == None:
                binning[i] = 1
    else:
        if binning[1] is None:
            binning[1] = min(sample[:,0])
        if binning[2] is None:
            binning[2] = max(sample[:,0])
        if binning[0] is None:
            bin_w = 4*(np.percentile(sample[:,0],75) - np.percentile(sample[:,0],25))/(len(sample[:,0]))**(1./3.)
            if bin_w == 0:
                bin_w = 0.5*np.std(sample[:,0])
            if bin_w == 0:
                bin_w = 1

            binning[0] = int((binning[2] - binning[1])/bin_w)

        if binning[4] is None:
            binning[4] = min(sample[:,1])
        if binning[5] == None:
            binning[5] = max(sample[:,1])
        if binning[3] == None:
            bin_w = 4*(np.percentile(sample[:,1],75) - np.percentile(sample[:,1],25))/(len(sample[:,1]))**(1./3.)
            if bin_w == 0:
                bin_w = 0.5*np.std(sample[:,1])
            if bin_w == 0:
                bin_w = 1
            binning[3] = int((binning[5] - binning[4])/bin_w)
    if len(binning)==6:
        h = rt.TH2D(name, title, binning[0], binning[1], binning[2], binning[3], binning[4], binning[5])
    else:
        h = rt.TH2D(name, title, binning[-2]-1, array('f',binning[:binning[-2]]), binning[-1]-1, array('f', binning[binning[-2]:-2]));



    #for i in range(len(sample)):
#	if weights is None:
#	    h.Fill(sample[i,0],sample[i,1])
#	else:
#	    h.Fill(sample[i,0],sample[i,1],weights[i])
    rtnp.fill_hist(h, sample, weights=weights)
    h.SetXTitle(axis_title[0])
    h.SetYTitle(axis_title[1])
    h.SetZTitle(axis_title[2])
    h.binning = binning
    return h

def rootTH2_to_np(h, cut = None, Norm = False):
    nx = h.GetNbinsX()
    ny = h.GetNbinsY()

    arr = np.zeros((ny, nx))
    pos = np.zeros((ny, nx, 2))

    for ix in range(nx):
        for iy in range(ny):
            x = h.GetXaxis().GetBinCenter( ix+1 );
            y = h.GetYaxis().GetBinCenter( iy+1 );
            z = h.GetBinContent(h.GetBin(ix+1, iy+1))

            if cut == None:
                arr[iy, ix] = z
            else:
                arr[iy, ix] = z if z > cut else 0
            pos[iy, ix] = [x,y]
    return arr, pos

def make_ratio_pEff(h_list_in, title = "", label = "", fit = False, in_tags = None, ratio_bounds = [0.1, 4], ratio_index = 0, logy = False,draw_opt = ['hist','E1'], text = ""):
    h_list = []
    if in_tags == None:
        tag = []
    else:
        tag = in_tags
    for i, h in enumerate(h_list_in):
        h_list.append(h.Clone('h{}aux{}'.format(i, label)))
        if in_tags == None:
            tag.append(h.GetTitle())

    c_out = rt.TCanvas("c_out_ratio"+label, "c_out_ratio"+label, 800, 800)
    pad1 = rt.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0.03)
    pad1.SetLeftMargin(0.15)
    # pad1.SetGridx()
    if logy:
        pad1.SetLogy()

    pad1.Draw()




    pad1.cd()

    leg = rt.TLegend(0.68, 0.7, 0.9, 0.9)
    leg = rt.TLegend(0.2, 0.6, 0.5, 0.9)
    #leg = rt.TLegend(0.7, 0.2, 0.9, 0.4)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.045)
    leg.SetFillStyle(0)
    c_out.cd(1)

    for i, h in enumerate(h_list):
        if i == 0:
            h.Draw('AP')
        else:
            h.Draw("Psame")

        leg.AddEntry(h, tag[i], "lep")
    leg.Draw("same")
    c_out.Draw()
    #h_list[0].GetPaintedGraph().GetHistogram().GetXaxis().SetLabelSize(0)
    h_list[0].GetPaintedGraph().GetHistogram().GetXaxis().SetLabelSize(0)
    h_list[0].GetPaintedGraph().GetHistogram().GetXaxis().SetTitle("")
    h_list[0].GetPaintedGraph().GetHistogram().GetXaxis().SetLimits(h_list_in[0].GetCopyTotalHisto().GetXaxis().GetXmin(),h_list_in[0].GetCopyTotalHisto().GetXaxis().GetXmax())
    #h_list[0].GetPaintedGraph().GetHistogram().GetYaxis().SetRangeUser(0, 1.5*max(map(lambda x: x.GetPaintedGraph().GetHistogram().GetMaximum(), h_list)))
    h_list[0].GetPaintedGraph().GetHistogram().GetYaxis().SetRangeUser(0, 1.5)
    if logy:
        h_list[0].GetPaintedGraph().GetHistogram().GetYaxis().SetRangeUser(10e-7, 150*max(map(lambda x: x.GetPaintedGraph().GetHistogram().GetMaximum(), h_list)))
    h_list[0].GetPaintedGraph().GetHistogram().GetYaxis().SetTitleOffset(1.0)
    h_list[0].GetPaintedGraph().GetHistogram().GetYaxis().SetTitleSize(0.06)
    h_list[0].GetPaintedGraph().GetHistogram().GetYaxis().SetLabelSize(0.05)
    h_list[0].GetPaintedGraph().GetHistogram().SetTitle(title)
    #h_list[0].GetPaintedGraph().GetHistogram().DrawCopy('hist')
    h_list[0].GetPaintedGraph().GetHistogram().SetFillColor(h_list_in[0].GetLineColor())
    h_list[0].GetPaintedGraph().GetHistogram().SetFillStyle(3002)
    h_list[0].GetPaintedGraph().GetHistogram().SetLineColor(h_list_in[0].GetLineColor())
    h_list[0].GetPaintedGraph().GetHistogram().SetLineWidth(2)
    h_list[0].GetPaintedGraph().GetHistogram().SetMarkerColor(h_list_in[0].GetLineColor())
    h_list[0].GetPaintedGraph().GetHistogram().SetMarkerSize(2)


    c_out.cd()
    pad2 = rt.TPad("pad2", "pad2", 0, 0, 1, 0.3)
    pad2.SetTopMargin(0.03)
    pad2.SetBottomMargin(0.25)
    pad2.SetLeftMargin(0.15)
    # pad2.SetGrid()
    pad2.Draw()
    pad2.cd()
    band = h_list_in[ratio_index].GetCopyTotalHisto()
    for j in range(band.GetXaxis().GetNbins()):
        band.SetBinContent(j+1, 1.0)
        if h_list[0].GetEfficiency(j+1) == 0:
            band.SetBinError(j+1, 0.0)
        else:
            band.SetBinError(j+1, h_list_in[ratio_index].GetEfficiencyErrorUp(j+1)/h_list_in[ratio_index].GetEfficiency(j+1))
            #print(j, h_list_in[0].GetBinError(j+1)/h_list_in[0].GetBinContent(j+1))
    band.SetFillColor(h_list_in[ratio_index].GetLineColor())
    band.SetFillStyle(3002)
    band.SetLineColor(h_list_in[ratio_index].GetLineColor())
    band.GetYaxis().SetTitleOffset(0.6)
    band.GetYaxis().SetRangeUser(ratio_bounds[0], ratio_bounds[1])
    band.GetYaxis().SetTitleSize(0.1)
    band.GetYaxis().SetLabelSize(0.12)
    band.GetYaxis().SetNdivisions(506)
    band.GetXaxis().SetTitleOffset(0.95)
    band.GetXaxis().SetTitleSize(0.12)
    band.GetXaxis().SetLabelSize(0.12)
    band.GetXaxis().SetTickSize(0.07)
    band.SetYTitle('Ratio with {}'.format(tag[ratio_index]))
    #band.SetYTitle('Ratio with nominal')
    band.SetTitle("")
    band.DrawCopy('E2')
    ln = rt.TLine(band.GetXaxis().GetXmin(), 1, band.GetXaxis().GetXmax(), 1)
    ln.SetLineWidth(3)
    ln.SetLineColor(h_list_in[ratio_index].GetLineColor())
    ln.DrawLine(band.GetXaxis().GetXmin(), 1, band.GetXaxis().GetXmax(), 1)
    for i, h in enumerate(h_list):
        if i == ratio_index:
            continue
        else:
            nom = h.GetCopyPassedHisto()
            denom = h_list[ratio_index].GetCopyPassedHisto()
            nom.SetLineColor(h.GetLineColor())
            #set relative error of ratio to be the relative error of data
            for j in range(nom.GetXaxis().GetNbins()+1):
                nom.SetBinContent(j+1,h.GetEfficiency(j+1))
                denom.SetBinContent(j+1,h_list[ratio_index].GetEfficiency(j+1))
                nom.SetBinError(j+1,max(h.GetEfficiencyErrorLow(j+1), h.GetEfficiencyErrorUp(j+1)))
                denom.SetBinError(j+1,max(h_list[ratio_index].GetEfficiencyErrorLow(j+1), h_list[ratio_index].GetEfficiencyErrorUp(j+1)))
            nom.Divide(denom)
            nom.DrawCopy('same'+draw_opt[i])
            print(nom.GetBinContent(1),nom.GetBinError(1), nom.GetBinContent(2), nom.GetBinError(2))


    pad2.Update()



    c_out.pad1 = pad1
    c_out.pad2 = pad2
    c_out.h_list = h_list
    c_out.leg = leg
    return c_out
def make_ratio_plot(h_list_in, title = "", label = "", fit = False, in_tags = None, ratio_bounds = [0.1, 4], logy = False, ratio_index = 0, draw_opt = ['hist','E1'], text = ""):
    h_list = []
    if in_tags == None:
        tag = []
    else:
        tag = in_tags
    for i, h in enumerate(h_list_in):
        h_list.append(h.Clone('h{}aux{}'.format(i, label)))
        if in_tags == None:
            tag.append(h.GetTitle())

    c_out = rt.TCanvas("c_out_ratio"+label, "c_out_ratio"+label, 800, 800)
    pad1 = rt.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0.03)
    pad1.SetLeftMargin(0.15)
    pad1.SetRightMargin(0.04)# pad2.SetGrid()
    if logy:
        pad1.SetLogy()

    pad1.Draw()
    pad1.cd()

    leg = rt.TLegend(0.5, 0.65, 0.9, 0.92)
    leg = rt.TLegend(0.7, 0.65, 0.9, 0.92)

    #leg = rt.TLegend(0.2, 0.7, 0.5, 0.9)
    # leg = rt.TLegend(0.7, 0.2, 0.9, 0.4)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.045)
    leg.SetFillStyle(0)
    c_out.cd(1)

    for i, h in enumerate(h_list):
        if i == 0:
            h.GetXaxis().SetLabelSize(0)
            h.GetXaxis().SetTitle("")
            h.GetYaxis().SetRangeUser(0, 2.2*max(map(lambda x: x.GetMaximum(), h_list)))
            if logy:
                h.GetYaxis().SetRangeUser(10e-5, 2.5*max(map(lambda x: x.GetMaximum(), h_list)))
            h.GetYaxis().SetTitleOffset(1.0)
            h.GetYaxis().SetTitleSize(0.06)
            h.GetYaxis().SetLabelSize(0.05)
            h.SetTitle(title)
            if ratio_index == 0:h.DrawCopy("hist")
            h.SetFillColor(h_list_in[0].GetLineColor())
            h.SetFillStyle(3002)
            #h.SetStats(1)
            h.SetLineColor(h_list_in[0].GetLineColor())
            h.SetLineWidth(2)
            h.SetMarkerColor(h_list_in[0].GetLineColor())
            h.SetMarkerSize(2)
            # if ratio_index == 0:
            #     # h.DrawCopy("hist")
            #     h.DrawCopy(draw_opt[i]+'same')
            # else:h.DrawCopy(draw_opt[i])
            if ratio_index == 0:h.DrawCopy(draw_opt[i]+"same")
            else:h.DrawCopy(draw_opt[i])
            if len(text)>0:
                l = rt.TLatex()
                l.SetTextSize(0.045)
                if logy:l.DrawLatex((h.GetXaxis().GetXmax()-h.GetXaxis().GetXmin())*0.1+h.GetXaxis().GetXmin() , h.GetMaximum()/10, text)
                else:l.DrawLatex((h.GetXaxis().GetXmax()-h.GetXaxis().GetXmin())*0.1+h.GetXaxis().GetXmin() , h.GetMaximum()*0.8, text)
        else:
            h.DrawCopy(draw_opt[i]+"same")
            # h.DrawCopy("E1 same")

        leg.AddEntry(h, tag[i], "lep")
    leg.Draw("same")

    c_out.cd()
    pad2 = rt.TPad("pad2", "pad2", 0, 0, 1, 0.3)
    pad2.SetTopMargin(0.03)
    pad2.SetBottomMargin(0.25)
    pad2.SetLeftMargin(0.15)
    pad2.SetRightMargin(0.04)# pad2.SetGrid()
    pad2.Draw()
    pad2.cd()
    band = h_list_in[ratio_index].Clone('h_band')
    for j in range(band.GetXaxis().GetNbins()):
        band.SetBinContent(j+1, 1.0)
        if h_list[ratio_index].GetBinContent(j+1) == 0:
            band.SetBinError(j+1, 0.0)
        else:
            band.SetBinError(j+1, h_list_in[ratio_index].GetBinError(j+1)/h_list_in[ratio_index].GetBinContent(j+1))
            #print(j, h_list_in[0].GetBinError(j+1)/h_list_in[0].GetBinContent(j+1))
    band.SetFillColor(h_list_in[ratio_index].GetLineColor())

    band.SetFillStyle(3002)
    band.SetLineColor(h_list_in[ratio_index].GetLineColor())
    #band.SetFillColorAlpha(0,0)
    #band.SetLineColor(0)
    band.GetYaxis().SetTitleOffset(0.5)
    band.GetYaxis().SetRangeUser(ratio_bounds[0], ratio_bounds[1])
    band.GetYaxis().SetTitleSize(0.11)
    band.GetYaxis().SetLabelSize(0.12)
    band.GetYaxis().SetNdivisions(506)
    band.GetXaxis().SetTitleOffset(0.95)
    band.GetXaxis().SetTitleSize(0.12)
    band.GetXaxis().SetLabelSize(0.12)
    band.GetXaxis().SetTickSize(0.07)
    band.SetYTitle('Ratio with {}'.format(tag[ratio_index]))
    band.SetTitle("")
    band.DrawCopy('E2')
    ln = rt.TLine(h.GetXaxis().GetXmin(), 1, h.GetXaxis().GetXmax(), 1)
    ln.SetLineWidth(3)
    ln.SetLineColor(h_list_in[ratio_index].GetLineColor())
    ln.DrawLine(h.GetXaxis().GetXmin(), 1, h.GetXaxis().GetXmax(), 1)
    for i, h in enumerate(h_list):
        if i == ratio_index:
            continue
        else:
            if fit:h.GetFunction("expo")
            h.Divide(h_list[ratio_index])
            # h.GetYaxis().SetTitleOffset(0.6)
            # h.GetYaxis().SetRangeUser(ratio_bounds[0], ratio_bounds[1])
            # h.GetYaxis().SetTitleSize(0.12)
            # h.GetYaxis().SetLabelSize(0.12)
            # h.GetYaxis().SetNdivisions(506)
            # h.GetXaxis().SetTitleOffset(0.95)
            # h.GetXaxis().SetTitleSize(0.12)
            # h.GetXaxis().SetLabelSize(0.12)
            # h.GetXaxis().SetTickSize(0.07)
            # h.SetYTitle('Ratio with {}'.format(tag[0]))
            # h.SetTitle("")
            #set relative error of ratio to be the relative error of data
            for j in range(h.GetXaxis().GetNbins()):
                if h_list[i].GetBinContent(j+1) == 0:
                    h.SetBinError(j+1, 0.0)
                else:
                    h.SetBinError(j+1, h_list_in[i].GetBinError(j+1)/h_list_in[i].GetBinContent(j+1)*h.GetBinContent(j+1))
            h.DrawCopy('same'+draw_opt[i])

    pad2.Update()

    c_out.pad1 = pad1
    c_out.pad2 = pad2
    c_out.h_list = h_list
    c_out.leg = leg
    return c_out



def binning2d(histo2D,min_event,direc):#returns an appropriate binning in x/y direction with at least min_event points in each binning
    bins = [1]
    i=0
    if direc == 'x':
        nbins = histo2D.GetNbinsX()
    elif direc == 'y':
        nbins =  histo2D.GetNbinsY()
    else:
        return None
    while i < nbins:
        counter = 0
        while counter < min_event:
            if direc == 'x':
                h1 = histo2D.ProjectionY("h"+str(i),i+1,i+1)
            else:
                h1 = histo2D.ProjectionX("h"+str(i),i+1,i+1)
            counter += h1.Integral()
            i+=1
            if i >nbins:
                break
        bins.append(i)
    bins = bins[:len(bins)-2]+[bins[len(bins)-1]]
    if bins[1] == 1:
        bins.pop(1)
    return bins
def histo2D_projectionFit(histo2D, bins, gaus_thr, rebin, direc): #given the binning, plot the scale and resolution of the projection of 2D map
    proj = []
    if direc == 'x':
        bw = histo2D.GetXaxis().GetBinWidth(1)
        left_edge = histo2D.GetXaxis().GetBinLowEdge(1)
    elif direc == 'y':
        bw = histo2D.GetYaxis().GetBinWidth(1)
        left_edge = histo2D.GetYaxis().GetBinLowEdge(1)
    else:
        return None
    x_bins = [(x-1)*bw+left_edge for x in bins]
    res = rt.TH1F('res','res', len(bins)-1,array( 'f', x_bins))
    res_eff = rt.TH1F('res_eff','res_eff', len(bins)-1,array( 'f', x_bins))
    scale = rt.TH1F('scale','scale',len(bins)-1,array( 'f', x_bins))
    scale_eff = rt.TH1F('scale_eff','scale_eff',len(bins)-1,array( 'f', x_bins))
    for i in range(len(bins)-1):
        key = 'bin'+str(i)
        proj.append(histo2D.ProjectionX("h"+str(i),bins[i],bins[i+1]-1))
        if direc == 'x':
            y_low = histo2D.GetXaxis().GetBinLowEdge(bins[i])
            y_up = histo2D.GetXaxis().GetBinLowEdge(bins[i+1]-1)+histo2D.GetXaxis().GetBinWidth(1)
        else:
            y_low = histo2D.GetYaxis().GetBinLowEdge(bins[i])
            y_up = histo2D.GetYaxis().GetBinLowEdge(bins[i+1]-1)+histo2D.GetYaxis().GetBinWidth(1)

    for i in range(len(proj)):
        h1 = proj[i]
        hnew = h1.Clone("hnew")
        hnew = hnew.Rebin(rebin)
        SS = rt.TSpectrum()
        n_pks = SS.Search(hnew, 0.1, "", 0.5)
        x_pos = SS.GetPositionX()
        y_pos = SS.GetPositionY()
        pks = []
        if n_pks == 0:
            hnew.SetLineColor(4)
    #         hnew.Rebin(2)
            hnew.GetXaxis().SetRangeUser(-5,5)
            hnew.DrawCopy()
            print("npks == 0",i,hnew.Integral(),n_pks)
            break
        n_pk = hnew.FindBin(x_pos[0])
        thr = gaus_thr* hnew.GetBinContent(n_pk)
        n_low = n_pk
        while hnew.GetBinContent(n_low) > thr:
            n_low -= 1
        x_low = hnew.GetBinCenter(n_low)
        n_up = n_pk
        while hnew.GetBinContent(n_up) > thr:
            n_up += 1
        x_up = hnew.GetBinCenter(n_up)
        r = hnew.Fit('gaus', 'LRSQ+', '', x_low, x_up)
        r = r.Get()
        scale.SetBinContent(i+1,r.Parameter(1))
        scale.SetBinError(i+1,r.ParError(1))
        if abs(r.Parameter(1)-hnew.GetMean())>1:
            print("scale fit warning", i,r.Parameter(1),hnew.GetMean())
        n_pk = h1.FindBin(r.Parameter(1))
        thr = 0.68 * h1.Integral()
        counter = h1.GetBinContent(n_pk)*1.0
        n_low = n_pk
        n_up = n_pk
        flag = True
        while counter < thr:
            if flag:
                n_low -= 1
                counter += h1.GetBinContent(n_low)
            else:
                n_up += 1
                counter += h1.GetBinContent(n_up)
            flag = not flag
        sigma_eff = (n_up - n_low) *h1.GetBinWidth(1)
        res.SetBinContent(i+1,sigma_eff)
        res.SetBinError(i+1,h1.GetBinWidth(1))
    res_eff.SetBinContent(i+1,r.Parameter(2))
    res_eff.SetBinError(i+1,r.ParError(2))
    return scale, scale_eff, res, res_eff
def create_TGraph(x,y,ex=[],ey=[], axis_title = ['','']):
    x = array("d", x)
    y = array("d", y)
    ex = array("d", ex)
    ey = array("d", ey)
    if not len(x) == len(y):
        print("length of x and y are not equal!")
    if not len(ex)==len(ey):
        print("length of ex and ey are not equal!")
    if len(ex)>0 and not len(x)==len(ex):
        print("leng of ex and x are not equal!")

    if len(ex)==0:gr = rt.TGraph(len(x),x,y)
    else: gr = rt.TGraphErrors(len(x),x,y,ex,ey)
    if len(axis_title) == 2:
    	gr.GetXaxis().SetTitle(axis_title[0])
    	gr.GetYaxis().SetTitle(axis_title[1])
    return gr
