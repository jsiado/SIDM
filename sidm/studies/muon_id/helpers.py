import matplotlib.pyplot as plt

from collections import OrderedDict
from sidm.tools import utilities

fmulxy1 = ["4Mu_200GeV_0p25GeV_0p01mm",   "4Mu_200GeV_0p25GeV_0p1mm",       "4Mu_200GeV_0p25GeV_1p0mm",    "4Mu_200GeV_0p25GeV_5p0mm",    "4Mu_200GeV_0p25GeV_10p0mm"]
fmulxy2 = ["4Mu_200GeV_1p2GeV_0p048mm",   "4Mu_200GeV_1p2GeV_0p48mm",       "4Mu_200GeV_1p2GeV_4p8mm",     "4Mu_200GeV_1p2GeV_24p0mm",    "4Mu_200GeV_1p2GeV_48p0mm"]    
fmulxy3 = ["4Mu_200GeV_5p0GeV_0p2mm",     "4Mu_200GeV_5p0GeV_2p0mm",        "4Mu_200GeV_5p0GeV_20p0mm",    "4Mu_200GeV_5p0GeV_100p0mm",   "4Mu_200GeV_5p0GeV_200p0mm"]

fmulxy4 = ["4Mu_500GeV_0p25GeV_0p004mm",  "4Mu_500GeV_0p25GeV_0p04mm",      "4Mu_500GeV_0p25GeV_0p4mm",    "4Mu_500GeV_0p25GeV_2p0mm",    "4Mu_500GeV_0p25GeV_4p0mm"]
fmulxy5 = ["4Mu_500GeV_1p2GeV_0p019mm",   "4Mu_500GeV_1p2GeV_0p19mm",       "4Mu_500GeV_1p2GeV_1p9mm",     "4Mu_500GeV_1p2GeV_9p6mm",     "4Mu_500GeV_1p2GeV_19p0mm"]
fmulxy6 = ["4Mu_500GeV_5p0GeV_0p08mm",    "4Mu_500GeV_5p0GeV_0p8mm",        "4Mu_500GeV_5p0GeV_8p0mm",     "4Mu_500GeV_5p0GeV_40p0mm",    "4Mu_500GeV_5p0GeV_80p0mm"]

fmulxy7 = ["4Mu_800GeV_0p25GeV_0p0025mm",  "4Mu_800GeV_0p25GeV_0p025mm",    "4Mu_800GeV_0p25GeV_0p25mm",   "4Mu_800GeV_0p25GeV_1p2mm",    "4Mu_800GeV_0p25GeV_2p5mm",]
fmulxy8 = ["4Mu_800GeV_1p2GeV_0p012mm",    "4Mu_800GeV_1p2GeV_0p12mm",      "4Mu_800GeV_1p2GeV_1p2mm",     "4Mu_800GeV_1p2GeV_6p0mm",     "4Mu_800GeV_1p2GeV_12p0mm",]
fmulxy9 = ["4Mu_800GeV_5p0GeV_0p05mm",     "4Mu_800GeV_5p0GeV_0p5mm",       "4Mu_800GeV_5p0GeV_5p0mm",     "4Mu_800GeV_5p0GeV_25p0mm",    "4Mu_800GeV_5p0GeV_50p0mm",]

fmulxy0 = ["4Mu_1000GeV_0p25GeV_0p002mm",  "4Mu_1000GeV_0p25GeV_0p02mm",    "4Mu_1000GeV_0p25GeV_0p2mm",   "4Mu_1000GeV_0p25GeV_1p0mm",   "4Mu_1000GeV_0p25GeV_2p0mm",]
fmulxyi = ["4Mu_1000GeV_1p2GeV_0p0096mm",  "4Mu_1000GeV_1p2GeV_0p096mm",    "4Mu_1000GeV_1p2GeV_0p96mm",   "4Mu_1000GeV_1p2GeV_4p8mm",    "4Mu_1000GeV_1p2GeV_9p6mm",]
fmulxyx = ["4Mu_1000GeV_5p0GeV_0p04mm",    "4Mu_1000GeV_5p0GeV_0p4mm",      "4Mu_1000GeV_5p0GeV_4p0mm",    "4Mu_1000GeV_5p0GeV_20p0mm",   "4Mu_1000GeV_5p0GeV_40p0mm",]

fmusam = [fmulxy5, fmulxy6, fmulxy7, fmulxy8, fmulxy9, fmulxy0, fmulxyi, fmulxyx, fmulxy1, fmulxy2, fmulxy3, fmulxy4,]

tmulxy1 = ["2Mu2E_200GeV_0p25GeV_0p01mm",  "2Mu2E_200GeV_0p25GeV_0p1mm",    "2Mu2E_200GeV_0p25GeV_1p0mm",  "2Mu2E_200GeV_0p25GeV_5p0mm",  "2Mu2E_200GeV_0p25GeV_10p0mm",]
tmulxy2 = ["2Mu2E_200GeV_1p2GeV_0p048mm",  "2Mu2E_200GeV_1p2GeV_0p48mm",    "2Mu2E_200GeV_1p2GeV_4p8mm",   "2Mu2E_200GeV_1p2GeV_24p0mm",  "2Mu2E_200GeV_1p2GeV_48p0mm",]
tmulxy3 = ["2Mu2E_200GeV_5p0GeV_0p2mm",    "2Mu2E_200GeV_5p0GeV_2p0mm",     "2Mu2E_200GeV_5p0GeV_20p0mm",  "2Mu2E_200GeV_5p0GeV_100p0mm", "2Mu2E_200GeV_5p0GeV_200p0mm",]

tmulxy4 = ["2Mu2E_500GeV_0p25GeV_0p004mm",  "2Mu2E_500GeV_0p25GeV_0p04mm",  "2Mu2E_500GeV_0p25GeV_0p4mm",  "2Mu2E_500GeV_0p25GeV_2p0mm",  "2Mu2E_500GeV_0p25GeV_4p0mm",]
tmulxy5 = ["2Mu2E_500GeV_1p2GeV_0p019mm",   "2Mu2E_500GeV_1p2GeV_0p19mm",   "2Mu2E_500GeV_1p2GeV_1p9mm",   "2Mu2E_500GeV_1p2GeV_9p6mm",   "2Mu2E_500GeV_1p2GeV_19p0mm",]
tmulxy6 = ["2Mu2E_500GeV_5p0GeV_0p08mm",    "2Mu2E_500GeV_5p0GeV_0p8mm",   "2Mu2E_500GeV_5p0GeV_8p0mm",   "2Mu2E_500GeV_5p0GeV_40p0mm",  "2Mu2E_500GeV_5p0GeV_80p0mm",]

tmulxy7 = ["2Mu2E_800GeV_0p25GeV_0p0025mm", "2Mu2E_800GeV_0p25GeV_0p025mm", "2Mu2E_800GeV_0p25GeV_0p25mm", "2Mu2E_800GeV_0p25GeV_1p2mm",  "2Mu2E_800GeV_0p25GeV_2p5mm",]
tmulxy8 = ["2Mu2E_800GeV_1p2GeV_0p012mm",   "2Mu2E_800GeV_1p2GeV_0p12mm",   "2Mu2E_800GeV_1p2GeV_1p2mm",   "2Mu2E_800GeV_1p2GeV_6p0mm",   "2Mu2E_800GeV_1p2GeV_12p0mm",]    
tmulxy9 = ["2Mu2E_800GeV_5p0GeV_0p05mm",    "2Mu2E_800GeV_5p0GeV_0p5mm",    "2Mu2E_800GeV_5p0GeV_5p0mm",   "2Mu2E_800GeV_5p0GeV_25p0mm",  "2Mu2E_800GeV_5p0GeV_50p0mm",]

tmulxy0 = ["2Mu2E_1000GeV_0p25GeV_0p002mm", "2Mu2E_1000GeV_0p25GeV_0p02mm", "2Mu2E_1000GeV_0p25GeV_0p2mm", "2Mu2E_1000GeV_0p25GeV_1p0mm", "2Mu2E_1000GeV_0p25GeV_2p0mm",]
tmulxyi = ["2Mu2E_1000GeV_1p2GeV_0p0096mm", "2Mu2E_1000GeV_1p2GeV_0p096mm", "2Mu2E_1000GeV_1p2GeV_0p96mm", "2Mu2E_1000GeV_1p2GeV_4p8mm",  "2Mu2E_1000GeV_1p2GeV_9p6mm",]
tmulxyx = ["2Mu2E_1000GeV_5p0GeV_0p04mm",   "2Mu2E_1000GeV_5p0GeV_0p4mm",   "2Mu2E_1000GeV_5p0GeV_4p0mm",  "2Mu2E_1000GeV_5p0GeV_20p0mm", "2Mu2E_1000GeV_5p0GeV_40p0mm"]




bkgttj = ["TTJets"]
bkgdyj1 = ["DYJetsToMuMu_M10to50",]
bkgdyj2 = ["DYJetsToMuMu_M50",]
bkgqcd1 = ["QCD_Pt15To20",]
bkgqcd2 = ["QCD_Pt20To30"]
bkgqcd3 = ["QCD_Pt30To50",]
bkgqcd4 = ["QCD_Pt50To80"]
bkgqcd5 = ["QCD_Pt80To120"]
bkgqcd6 = ["QCD_Pt120To170"]
bkgqcd7 = ["QCD_Pt170To300",]
bkgqcd8 = ["QCD_Pt300To470"]
bkgqcd9 = ["QCD_Pt470To600"]
bkgqcd0 = ["QCD_Pt600To800"]
bkgqcdi = ["QCD_Pt800To1000",] 
bkgqcdx = ["QCD_Pt1000"]



# Combine hist for DYJ and QCD


def merge_bkg(output, samples, histname, channel, rebin=None):
    if rebin is None: merged = output[samples[0]]["hists"][histname][channel, :].copy()
    else:             merged = output[samples[0]]["hists"][histname][channel, ::rebin].copy()

    for sample in samples[1:]:
        if rebin is None: merged += output[sample]["hists"][histname][channel, :]
        else:             merged += output[sample]["hists"][histname][channel, ::rebin]
    return merged

#combine cutflows for samples
def merge_cutflows(output, samples, channel):
    merged = OrderedDict()

    for sample in samples:
        cf = output[sample]["cutflow"][channel].rows

        for cut, vals in cf.items():
            print(cut)
            if cut not in merged:
                merged[cut] = {"raw": 0, "weighted": 0.0}

            merged[cut]["raw"] += vals["raw"]
            merged[cut]["weighted"] += vals["weighted"]

    return merged

# plotter made simple
def plotter(output, samples, labels, legend_title, file_tag, htplot, htname, ch, vr, wch, xnames, svd = True):
    """
    Parameters
    ----------
    output : dict
        Coffea output dictionary.
    samples : list - List of sample names.
    labels : list- Labels for the legend.
    legend_title : str
        Title of the legend shown on the plot.
    file_tag : str
        Short tag used when saving the figure.
    htplot : list
        Histogram names.
    htname : list,         Plot titles.
    ch1 : str,         Analysis channel.
    vr : str,         Version string.
    """

    for ik, ht in enumerate(htplot):
        fig, ax = plt.subplots(figsize=(12, 10))
        for ij, sample in enumerate(samples):
            utilities.plot(output[sample]["hists"][ht][ch, :], label=labels[ij])

        ax.set_title(htname[ik])
        ax.set_ylabel("Events")
        ax.set_yscale("log")
        ax.set_xlabel(xnames[ik])
        ax.legend(title=f"{wch}: {legend_title}", alignment="left", loc=0,)

        plt.tight_layout()
        if svd ==True:
            plt.savefig(f"clean_plots/GenReco_{vr}_{wch}_{file_tag}_{ht}.pdf", bbox_inches="tight", dpi=300,)
            print(f"clean_plots/GenReco_{vr}_{wch}_{file_tag}_{ht}",)
            # plt.close(fig)

def chunking(fileset):
    for ds, files in fileset.items():
        print(ds)
        print("chunks", len(files["files"]))

# def plt_bkg(htp):
#     TTJ = merge_bkg(output, bkgttj, htp, ch1)
#     utilities.plot(TTJ, label = "TTJets")
#     DYJ = merge_bkg(output, bkgdyj, "lj0_mass", ch1)
#     utilities.plot(DYJ, label = "DYJets")
#     QCD = merge_bkg(output, bkgqcd, "lj0_mass", ch1)
#     utilities.plot(DYJ, label = "DYJets")
    