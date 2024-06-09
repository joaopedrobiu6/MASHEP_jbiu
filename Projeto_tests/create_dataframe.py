import pandas as pd
import numpy as np

# import data from CSV
data = pd.read_csv("Output_ZPrimeBoostedAnalysis/data.csv", delimiter=" ")

ttbar_lep = pd.read_csv("Output_ZPrimeBoostedAnalysis/ttbar_lep.csv", delimiter=" ")
ttbar_lep["scale"] =0.0924183

ZPrime1000 = pd.read_csv("Output_ZPrimeBoostedAnalysis/ZPrime1000_tt.csv", delimiter=" ")
ZPrime1000["scale"] =0.0567221

Wenu_PTV70_140_BFilter = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wenu_PTV70_140_BFilter.csv", delimiter=" ")
Wenu_PTV70_140_BFilter["scale"] =0.239882
Wenu_PTV140_280_BFilter = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wenu_PTV140_280_BFilter.csv", delimiter=" ")
Wenu_PTV140_280_BFilter["scale"] =0.0493328
Wenu_PTV140_280_CFilterBVeto = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wenu_PTV140_280_CFilterBVeto.csv", delimiter=" ")
Wenu_PTV140_280_CFilterBVeto["scale"] =0.184095
Wenu_PTV280_500_BFilter = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wenu_PTV280_500_BFilter.csv", delimiter=" ")
Wenu_PTV280_500_BFilter["scale"] =0.0340269
Wenu_PTV280_500_CFilterBVeto = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wenu_PTV280_500_CFilterBVeto.csv", delimiter=" ")
Wenu_PTV280_500_CFilterBVeto["scale"] =0.0810218
Wenu_PTV280_500_CVetoBVeto = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wenu_PTV280_500_CVetoBVeto.csv", delimiter=" ")
Wenu_PTV280_500_CVetoBVeto["scale"] =0.0894775
Wenu_PTV500_1000 = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wenu_PTV500_1000.csv", delimiter=" ")
Wenu_PTV500_1000["scale"] =0.0244734
Wenu_PTV1000 = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wenu_PTV1000.csv", delimiter=" ")
Wenu_PTV1000["scale"] =0.00295733

Wmunu_PTV70_140_BFilter = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wmunu_PTV70_140_BFilter.csv", delimiter=" ")
Wmunu_PTV70_140_BFilter["scale"] =0.0959952
Wmunu_PTV70_140_CVetoBVeto = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wmunu_PTV70_140_CVetoBVeto.csv", delimiter=" ")
Wmunu_PTV70_140_CVetoBVeto["scale"] =1.14682
Wmunu_PTV140_280_BFilter = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wmunu_PTV140_280_BFilter.csv", delimiter=" ")
Wmunu_PTV140_280_BFilter["scale"] =0.0503071
Wmunu_PTV280_500_BFilter = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wmunu_PTV280_500_BFilter.csv", delimiter=" ")
Wmunu_PTV280_500_BFilter["scale"] =0.0311186
Wmunu_PTV280_500_CFilterBVeto = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wmunu_PTV280_500_CFilterBVeto.csv", delimiter=" ")
Wmunu_PTV280_500_CFilterBVeto["scale"] =0.0809599
Wmunu_PTV280_500_CVetoBVeto = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wmunu_PTV280_500_CVetoBVeto.csv", delimiter=" ")
Wmunu_PTV280_500_CVetoBVeto["scale"] =0.0891154
Wmunu_PTV500_1000 = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wmunu_PTV500_1000.csv", delimiter=" ")
Wmunu_PTV500_1000 ["scale"] =0.0246596
Wmunu_PTV1000 = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wmunu_PTV1000.csv", delimiter=" ")
Wmunu_PTV1000["scale"] =0.00296378

Wtaunu_PTV140_280_BFilter = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wtaunu_PTV140_280_BFilter.csv", delimiter=" ")
Wtaunu_PTV140_280_BFilter["scale"] =0.0478101
Wtaunu_PTV280_500_BFilter = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wtaunu_PTV280_500_BFilter.csv", delimiter=" ")
Wtaunu_PTV280_500_BFilter["scale"] =0.0337471
Wtaunu_PTV280_500_CFilterBVeto = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wtaunu_PTV280_500_CFilterBVeto.csv", delimiter=" ")
Wtaunu_PTV280_500_CFilterBVeto["scale"] =0.0808387
Wtaunu_PTV280_500_CVetoBVeto = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wtaunu_PTV280_500_CVetoBVeto.csv", delimiter=" ")
Wtaunu_PTV280_500_CVetoBVeto["scale"] =0.0892594
Wtaunu_PTV500_1000 = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wtaunu_PTV500_1000.csv", delimiter=" ")
Wtaunu_PTV500_1000["scale"] =0.0247725
Wtaunu_PTV1000 = pd.read_csv("Output_ZPrimeBoostedAnalysis/Wtaunu_PTV1000.csv", delimiter=" ")
Wtaunu_PTV1000["scale"] =0.00296979

Zee = pd.read_csv("Output_ZPrimeBoostedAnalysis/Zee.csv", delimiter=" ")
Zee["scale"] =0.000130626
Zmumu = pd.read_csv("Output_ZPrimeBoostedAnalysis/Zmumu.csv", delimiter=" ")
Zmumu["scale"] =0.000133242
Ztautau = pd.read_csv("Output_ZPrimeBoostedAnalysis/Ztautau.csv", delimiter=" ")
Ztautau["scale"] =0.000349485

single_top_schan = pd.read_csv("Output_ZPrimeBoostedAnalysis/single_top_schan.csv", delimiter=" ")
single_top_schan["scale"] =0.0207898
single_top_tchan = pd.read_csv("Output_ZPrimeBoostedAnalysis/single_top_tchan.csv", delimiter=" ")
single_top_tchan["scale"] =0.0891151
single_top_wtchan = pd.read_csv("Output_ZPrimeBoostedAnalysis/single_top_wtchan.csv", delimiter=" ")
single_top_wtchan["scale"] =0.0741397
single_antitop_schan = pd.read_csv("Output_ZPrimeBoostedAnalysis/single_antitop_schan.csv", delimiter=" ")
single_antitop_schan["scale"] =0.013029
single_antitop_tchan = pd.read_csv("Output_ZPrimeBoostedAnalysis/single_antitop_tchan.csv", delimiter=" ")
single_antitop_tchan["scale"] =0.0529964
single_antitop_wtchan = pd.read_csv("Output_ZPrimeBoostedAnalysis/single_antitop_wtchan.csv", delimiter=" ")
single_antitop_wtchan["scale"] =0.0729005

lllv = pd.read_csv("Output_ZPrimeBoostedAnalysis/lllv.csv", delimiter=" ")
lllv["scale"] =0.00851676
llvv = pd.read_csv("Output_ZPrimeBoostedAnalysis/llvv.csv", delimiter=" ")
llvv["scale"] =0.0248961
lvvv = pd.read_csv("Output_ZPrimeBoostedAnalysis/lvvv.csv", delimiter=" ")
lvvv["scale"] =0.0188037

bkg_Vjets = pd.concat([Wenu_PTV70_140_BFilter,Wenu_PTV140_280_BFilter,Wenu_PTV140_280_CFilterBVeto,Wenu_PTV280_500_BFilter,Wenu_PTV280_500_CFilterBVeto,Wenu_PTV280_500_CVetoBVeto,Wenu_PTV500_1000,Wenu_PTV1000,Wmunu_PTV70_140_BFilter,Wmunu_PTV70_140_CVetoBVeto,Wmunu_PTV140_280_BFilter,Wmunu_PTV280_500_BFilter,Wmunu_PTV280_500_CFilterBVeto,Wmunu_PTV280_500_CVetoBVeto,Wmunu_PTV500_1000,Wmunu_PTV1000,Wtaunu_PTV140_280_BFilter,Wtaunu_PTV280_500_BFilter,Wtaunu_PTV280_500_CFilterBVeto,Wtaunu_PTV280_500_CVetoBVeto,Wtaunu_PTV500_1000,Wtaunu_PTV1000,Zee,Zmumu,Ztautau],ignore_index=True)
bkg_singletop = pd.concat([single_top_schan, single_top_wtchan, single_top_wtchan,single_antitop_schan,single_antitop_tchan,single_antitop_wtchan],ignore_index=True)
bkg_lv = pd.concat([lllv,llvv,lvvv],ignore_index=True)

bkg_singletop.insert(0, "ID", "single_top_bkg")
bkg_Vjets.insert(0, "ID", "V_jets_bkg")
ttbar_lep.insert(0, "ID", "ttbar_bkg") 
bkg_lv.insert(0, "ID", "lepton_bkg") 
data.insert(0, "ID", "data")
ZPrime1000.insert(0, "ID", "signal") 

ttbar_lep["label"] = 0
bkg_singletop["label"] = 0
bkg_lv["label"] = 0
bkg_Vjets["label"] = 0
ZPrime1000["label"] = 1

bkg_dataframe=pd.concat([bkg_singletop,bkg_Vjets,ttbar_lep,bkg_lv],ignore_index=True)
dataframe = pd.concat([ZPrime1000,bkg_dataframe],ignore_index=True)

dataframe["scaleweight"] = dataframe["weight"]*dataframe["scale"]
dataframe.to_csv("dataframe.csv")