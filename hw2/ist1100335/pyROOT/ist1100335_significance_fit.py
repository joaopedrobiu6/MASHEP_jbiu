# PyROOT: https://root.cern/manual/python/
# execution:
# python significance_fit.py -b


# 𝐻→𝑊𝑊  search using the ATLAS Open Data
# ---------------------------------------------------------------------
# In this exercise, you are given a file containing an analysis TTree with selected event data from the search 
# for a Higgs boson decaying to WW pairs, where both W bosons decay leptonically.

# The TTree contains several observables, such as:

#  mLL: invariant mass of the dilepton pair
#  ptLL: transverse momentum of the dilepton pair
#  dPhi_LL: angular separation in azimuthal angle between the two charged leptons of the event
#  dPhiLLmet: angular separation in azimuthal angle between missing transverse energy and the dilepton pair
#  MET: missing transverse energy
#  mT: transverse mass (i.e. invariant mass calculated with the transverse components of missing ET and 
#  the two leptons)
#  goodjet_n: number of jets in the event (after quality criteria)
#  goodbjet_n: number of b jets in the event (after quality criteria)
#  For each of the leptons: transverse momentum pT, eta (pseudorapidity), energy E, azimuthal angle phi and charge
#  process: label indicating the kind of background taken into account
#  label: 0 for background, 1 for signal (valid only in MC simulation, for real data is -1)
#  weight: correction factors to take into account differences in reconstruction between data and MC simulation 
#  scale_weight: total event weight (including the MC correction weight above) used to normalise each event to 
#  its physical expectation, such that the sum of scale_weight yields the total number of expected events for the process


# The goals of this exercise are:

## 1) Make histograms of a few variables for the signal and background in the same plot (pTLL, dPhiLLmet, dPhi_LL, MET, mT). 
#     (Tip: you may first explore the TTree using the TBrowser to check the limits of the distributions)
## 2) Choose two variables for the signal selection optimisation. Justify your choice. 
## 3) Optimize the signal selection criteria using these two variables.
## 4) Draw the mT (transverse invariant mass of the WW pair) distribution after applying your selection conditions for the signal and the backgrounds with data and MC.
## 5) Build a test-statistics for signal discovery and use the data to perform a maximum-likelihood fit 
# to compute the observed and signal strength in the data sample, using mT as observable. 
# Based on the results of the test statistics, which one of the two hypotheses is more likely (background only or signal+background)? 
# Explain the reasoning behind your answer.

import ROOT
import math
print('Hello!')

# Open simulation file with TTree located in the folder: ../data/
MCfile = ROOT.TFile("../data/MC.root", "READ")
MCtree = MCfile.Get("hWWAna")

# Inspect TTree
#MCtree.Print()

## Example on how to make histograms
# Get signal and bkg histogram
histname = "mLL"
sighist = ROOT.TH1F(histname + "sig", "", 9, 0., 60.)
MCtree.Draw(histname + ">>" + histname + "sig", "scale_weight*(label==1)")
bkghist = ROOT.TH1F(histname + "bkg", "", 9, 0., 60.)
MCtree.Draw(histname + ">>" + histname + "bkg", "scale_weight*(label==0)")

print('\n\n++ Statistics before my optimised selection')
print(f'    signal histogram entries {sighist.GetEntries():.0f} expected events {sighist.Integral():.1f}')
print(f'background histogram entries {bkghist.GetEntries():.0f} expected events {bkghist.Integral():.1f}')
print(f'Total S/sqrt(S+B) {sighist.Integral() / math.sqrt(sighist.Integral() + bkghist.Integral()):.2f}')

# Plot signal vs background histograms
c = ROOT.TCanvas()

# Aesthetics and legend
sighist.SetLineColor(2)  #red
sighist.SetLineWidth(2)
bkghist.SetLineColor(8)  # green
bkghist.SetLineWidth(2)
bkghist.GetXaxis().SetTitle("mLL [GeV]")

legend = ROOT.TLegend()
bkghist.Draw("hist")
bkghist.SetMinimum(0)
sighist.Draw("histsame")
legend.AddEntry(sighist, "HWW signal")
legend.AddEntry(bkghist, "background")
legend.Draw()
c.Print(f"{histname}.png")

## Example on how to obtain a histogram after the selection cuts
sighistSEL = ROOT.TH1F(histname + "sigSEL", "", 10, 0., 60.)
MCtree.Draw(histname + ">>mLLsigSEL", "scale_weight*(label==1 && MET<80 && dPhiLLmet>1.8)")
bkghistSEL = ROOT.TH1F(histname + "bkgSEL", "", 10, 0., 60.)
MCtree.Draw(histname + ">>mLLbkgSEL", "scale_weight*(label==0 && MET<80 && dPhiLLmet>1.8)")
print('\n\n++ Statistics after my optimised selection')
print(f'    signal histogram entries {sighistSEL.GetEntries():.0f} expected events {sighistSEL.Integral():.1f}')
print(f'background histogram entries {bkghistSEL.GetEntries():.0f} expected events {bkghistSEL.Integral():.1f}')
print(
    f'Total S/sqrt(S+B) improved from {sighist.Integral() / math.sqrt(sighist.Integral() + bkghist.Integral()):.2f} to {sighistSEL.Integral() / math.sqrt(sighistSEL.Integral() + bkghistSEL.Integral()):.2f}')

# Use real data to perform the discovery fit and the test statistics
# datafile = ROOT.TFile("../data/data.root", "READ")
# datatree = datafile.Get("hWWAna")
# datahist = ROOT.TH1F(histname + "data", "", 9, 0., 60.)
# datatree.Draw(histname + ">>" + histname + "data", "")

############################################################################################
######################################## HOMEWORK 2 ########################################
########################################  JOÃO BIU  ########################################
######################################## ist1100335 ########################################
############################################################################################

######################################## QUESTION 1 ########################################
print('\n\n++ QUESTION 1')
# 1) Make histograms of a few variables for the signal and background in the same plot (pTLL, dPhiLLmet, dPhi_LL,
# MET, mT).

nbins = 200
variable_dict = {"ptLL": ["ptLL", nbins, 0., 200.], "dPhiLLmet": ["dPhiLLmet", nbins, 0., 3.5],
                 "dPhi_LL": ["dPhi_LL", nbins, 0., 3.2],
                 "MET": ["MET", nbins, 0., 300.], "mt": ["mt", nbins, 0., 300.]}
c = ROOT.TCanvas("c1", "", 1080, 1920)
c.Divide(2, 3)
# initialize a emptuy dictionary to append the entries in the loop
histograms = {}
legends = []

for var in variable_dict:
    c.cd(list(variable_dict.keys()).index(var) + 1)
    sighist = ROOT.TH1F(var + "sig", "", variable_dict[var][1], variable_dict[var][2], variable_dict[var][3])
    MCtree.Draw(variable_dict[var][0] + ">>" + var + "sig", "scale_weight*(label==1)")
    bkghist = ROOT.TH1F(var + "bkg", "", variable_dict[var][1], variable_dict[var][2], variable_dict[var][3])
    MCtree.Draw(variable_dict[var][0] + ">>" + var + "bkg", "scale_weight*(label==0)")

    # Aesthetics and legend
    sighist.SetLineColor(2)  #red
    sighist.SetLineWidth(2)
    bkghist.SetLineColor(8)  # green
    bkghist.SetLineWidth(2)
    bkghist.GetXaxis().SetTitle(f"{var} [GeV]")

    legend = ROOT.TLegend()
    ROOT.gStyle.SetOptStat(0)
    bkghist.Draw("hist")
    bkghist.SetMinimum(0)
    sighist.Draw("histsame")
    legend.AddEntry(sighist, "HWW signal")
    legend.AddEntry(bkghist, "background")
    histograms[variable_dict[var][0]] = [sighist, bkghist]
    legends.append(legend)
    legend.Draw()

c.Print(f"Exercise1.png")
c.Clear()

######################################## QUESTION 2 ########################################
print('\n\n++ QUESTION 2')
# 2) Choose two variables for the signal selection optimisation. Justify your choice.

""" 
I will choose the variables ptLL and MET for the signal selection optimisation.
These two variables have a better separation between the signal and background distributions.
Since we want to optimize the signal selection to better separate the signal from the background, we need to choose
the variables that have the best separation between the signal and background distributions to use to apply the best possible cuts.
"""
# Print the text above
print(
    'I will choose the variables ptLL and MET for the signal selection optimisation. These two variables have a better separation between the signal and background distributions.')
print("Since we want to optimize the signal selection to better separate the signal from the background, we need to choose the variables that have the best separation between the signal and background distributions to use to apply the best possible cuts.")


######################################## QUESTION 3 ########################################
print('\n\n++ QUESTION 3')
# 3) Optimize the signal selection criteria using these two variables.
# Calculate the significance of the signal and background histograms

def significance(S, B):
    if B == 0:
        return 0
    else:
        return math.sqrt(2*(S+B)*math.log(1+S/B) - 2*S)

# Define the variables to be used for the optimisation
best_variables = ["ptLL", "MET"]
print(histograms["MET"])

for var in best_variables:
    S_right, B_right = 0, 0
    S_left, B_left = 0, 0
    histograms[var].append(histograms[var][0].Clone())  # significance histogram from left to right
    histograms[var].append(histograms[var][0].Clone())  # significance histogram from right to left

    for i in range(1, histograms[var][0].GetNbinsX()+1):
        S_right = S_right + histograms[var][0].GetBinContent(i)
        B_right = B_right + histograms[var][1].GetBinContent(i)
        histograms[var][2].SetBinContent(i, significance(S_right, B_right))

        backwards_index = histograms[var][0].GetNbinsX() - i + 1
        S_left = S_left + histograms[var][0].GetBinContent(backwards_index)
        B_left = B_left + histograms[var][1].GetBinContent(backwards_index)
        histograms[var][3].SetBinContent(backwards_index, significance(S_left, B_left))


    cut_significance_right = histograms[var][2].GetXaxis().GetBinCenter(histograms[var][2].GetMaximumBin())
    cut_significance_left = histograms[var][3].GetXaxis().GetBinCenter(histograms[var][3].GetMaximumBin())
    histograms[var].append(cut_significance_right)
    histograms[var].append(cut_significance_left)
    # Plot the significance histograms
    c.Divide(2, 1)
    c.cd(1)
    histograms[var][2].SetTitle(f"Significance {var} from left to right")
    histograms[var][2].SetStats(0)
    histograms[var][2].GetXaxis().SetTitle(f"{var} [GeV]")
    histograms[var][2].GetYaxis().SetTitle("Significance (from left to right)")
    histograms[var][2].Draw("hist")

    c.cd(2)
    histograms[var][3].SetTitle(f"Significance {var} from right to left")
    histograms[var][3].SetStats(0)
    histograms[var][3].GetXaxis().SetTitle(f"{var} [GeV]")
    histograms[var][3].GetYaxis().SetTitle("Significance (right to left)")
    histograms[var][3].Draw("hist")

    c.Print(f"Exercise3_significance_{var}.png")
    c.Clear()
print(f'\nThe cuts that maximise the significance are:')
print(f'For {best_variables[0]}:\n Left: {histograms[best_variables[0]][5]}\n Right: {histograms[best_variables[0]][4]}\n')
print(f'For {best_variables[1]}:\n Left: {histograms[best_variables[1]][5]}\n Right: {histograms[best_variables[1]][4]}\n')

######################################## QUESTION 4 ########################################

print('\n\n++ QUESTION 4')
# 4) Draw the mT (transverse invariant mass of the WW pair) distribution after applying your selection conditions for the signal and the backgrounds with data and MC.

# Apply cut

hist = "mt"

sighistSEL_mT = ROOT.TH1F(hist + "sigSEL", "", variable_dict[hist][1], variable_dict[hist][2], variable_dict[hist][3])
MCtree.Draw(hist + ">>mtsigSEL",f"scale_weight*(label==1 && {best_variables[0]}<{histograms[best_variables[0]][4]} && {best_variables[1]}<{histograms[best_variables[1]][4]})")
bkghistSEL_mT = ROOT.TH1F(hist + "bkgSEL", "", variable_dict[hist][1], variable_dict[hist][2], variable_dict[hist][3])
MCtree.Draw(hist +">>mtbkgSEL",f"scale_weight*(label==0 && {best_variables[0]}<{histograms[best_variables[0]][4]} && {best_variables[1]}<{histograms[best_variables[1]][4]})")

c = ROOT.TCanvas()

# Aesthetics and legend
sighistSEL_mT.SetLineColor(2) #red
sighistSEL_mT.SetLineWidth(2)
bkghistSEL_mT.SetLineColor(8) # green
bkghistSEL_mT.SetLineWidth(2)
bkghistSEL_mT.GetXaxis().SetTitle("mT [GeV]")
# title
bkghistSEL_mT.SetTitle("mT distribution post-optimization")
legendmt = ROOT.TLegend()
bkghistSEL_mT.Draw("hist")
bkghistSEL_mT.SetMinimum(0)
sighistSEL_mT.Draw("histsame")
legendmt.AddEntry(sighistSEL_mT, "HWW signal")
legendmt.AddEntry(bkghistSEL_mT, "background")
legendmt.Draw()
c.Print(f"Exercise4_{hist}_SEL.png")
c.Clear()

sighist_mT = histograms[hist][0]
bkghist_mT = histograms[hist][1]

print('\n\n++ Statistics after my optimised selection')
print(f'signal histogram entries {sighistSEL_mT.GetEntries():.0f} expected events {sighistSEL_mT.Integral():.1f}')
print(f'background histogram entries {bkghistSEL_mT.GetEntries():.0f} expected events {bkghistSEL_mT.Integral():.1f}')
print(f'Total S/sqrt(S+B) improved from {sighist_mT.Integral() / math.sqrt(sighist_mT.Integral() + bkghist_mT.Integral()):.2f} to {sighistSEL_mT.Integral() / math.sqrt(sighistSEL_mT.Integral() + bkghistSEL_mT.Integral()):.2f}')


######################################## QUESTION 5 ########################################
print('\n\n++ QUESTION 5')
# 5) Build a test-statistics for signal discovery and use the data to perform a maximum-likelihood fit to compute the observed and signal strength in the data sample, using mT as observable.
datafile = ROOT.TFile("../data/data.root","READ")
datatree = datafile.Get("hWWAna")
datahist = ROOT.TH1F(hist+"data","", variable_dict[hist][1], variable_dict[hist][2], variable_dict[hist][3])
datatree.Draw(hist+">>"+hist+"data","")

def log_likelihood(mu, S, B, data):
    likelihood_result = []
    for i in range(S.GetNbinsX()):
        expected = mu*S.GetBinContent(i) + B.GetBinContent(i)
        datavalue = data.GetBinContent(i)
        if expected == 0:
            likelihood_result.append(0)
        else:
            likelihood_result.append(math.log(ROOT.Math.poisson_pdf(int(datavalue), expected)))
    return sum(likelihood_result)

likelikhood_hist = ROOT.TH1F("log_likelihood","", 800, 0., 8.)

for i in range(1, 801):
    mu = 0.01 * i
    log_like_values = log_likelihood(mu, sighistSEL_mT, bkghistSEL_mT, datahist)
    likelikhood_hist.SetBinContent(i, log_like_values)

# Plot the log likelihood
c = ROOT.TCanvas()
likelikhood_hist.SetTitle("Log likelihood")
likelikhood_hist.SetStats(0)
likelikhood_hist.GetXaxis().SetTitle("#mu")
likelikhood_hist.GetYaxis().SetTitle("log likelihood")
likelikhood_hist.Draw("hist")
c.Print("Exercise5_log_likelihood.png")
c.Clear()

mu_hat = likelikhood_hist.GetXaxis().GetBinCenter(likelikhood_hist.GetMaximumBin())
print(f"\nmu_hat = {mu_hat}")


q0 = -2*(log_likelihood(0, sighistSEL_mT, bkghistSEL_mT, datahist) - log_likelihood(mu_hat, sighistSEL_mT, bkghistSEL_mT, datahist))

print(f"q0 = {q0}")

print(f"\nWe obtained a value for mu-hat that is > 1 and a very large q0, therefore the background + signal hypothesis is the most likely.")
print(f"Mu-hat is the Maximum-likelihood estimate for mu and it measures the signal strength - in this case we obtained a large strenght for the signal, {mu_hat}.")
print(f"The q0 is a test statistic that measures the compatibility of the data with the background-only and background + signal hypothesis. The larger the q0, the more likely the background + signal hypothesis is true.")
# Close files in the end
MCfile.Close()
datafile.Close()
