
//
// The following lines show an example of how to use the ROOT TMath class to calculate the Poisson 
// probability for observing k events when lambda are expected.
// It also shows how to fill a histogram with a Poisson distribution.
//  
//  Documentation: https://root.cern.ch/root/html524/TMath.html#TMath:Poisson
//
//  Root version: gcc63/root/6.24.06 

void MASHEP_1stHomework(){

// Poisson probability calculation:
   int k=5, lambda =4;
   float p = TMath::Poisson(k, lambda);

   std::cout << "The Poisson probability of k=" << k << "; lambda =" << lambda << " is equal to " << p 
	     << std::endl;

   TH1F *hPois = new TH1F("hPois", "Poisson probability distribution", 25, -0.5,24.5);
   hPois->SetXTitle("k");
   hPois->SetYTitle("P(k|#lambda)");
   hPois->SetLineColor(kBlue);
   hPois->SetLineWidth(2);
   hPois->SetMarkerColor(kBlue);

   TF1 *Poisson2 = new TF1("Poisson2","TMath::Poisson(x,2)",0,25.);
   TF1 *Poisson4 = new TF1("Poisson4","TMath::Poisson(x,4)",0,25.);
   TF1 *Poisson10 = new TF1("Poisson10","TMath::Poisson(x,10)",0,25.);

   hPois->FillRandom("Poisson4",10000);

   TH1F* hPois2 = (TH1F*) hPois->Clone();
   hPois2->Reset();
   hPois2->FillRandom("Poisson2",10000);
   hPois2->SetLineColor(kRed);

   TH1F* hPois10 = (TH1F*) hPois->Clone();
   hPois10->Reset();
   hPois10->FillRandom("Poisson10",10000);
   hPois10->SetLineColor(kBlack);

   TCanvas* c1 = TCanvas::MakeDefCanvas();
   hPois2->Draw();
   hPois->Draw("same");
   hPois10->Draw("same");

   c1->SaveAs("Poissons.png");
}


//
//       PREAMBLE
//       ---------
//
//Consider a HEP experiment measuring an observable distributed in a 3-bin histogram.
//Monte-Carlo methods were used to simulate this observable for signal and background processes and 
//theory was used to predict the total number of events expected for both, yielding:
//
//* Expected signal:  𝑆𝑖={34,67,42} 
//* Expected background:  𝐵𝑖={404,376,198} 
//
//The real data measurement was:
//* Real data measurement:  𝑁𝑖={489,541,302} 
//
//
//Exercise 1: Likelihood model
//------------------------------
//
//Consider the likelihood model for the statistical analysis of the experiment above, consisting of:
//* A three-bin distribution of the observations
//* Two expected samples: a signal sample and a background sample
//* A normalization scaling factor 𝜇, the signal strength, for the signal sample.
//The only parameter of interest in this likelihood model is 𝜇 and there are no additional nuisance parameters.
//
// 1a) Likelihood function
//
// Define a python function to compute the likelihood model described above.
//





//1b) Likelihood value for the observations
//
//Use the function defined in line 1a) to calculate the likelihood for the observations described in 
//the preamble, given the theoretical expectations for the signal and the background also described 
//there (i.e. assuming that the normalisation of the simulation is correct).
//




// Exercise 2: Best-fit signal strength  𝜇̂ 
// ----------------------------------------
//
// Consider the experiment and results described in the preamble.
//
// 2a)  𝜇̂>1  or  𝜇̂<1  ?
//
// Qualitatively, do you expect the best-fit value  𝜇̂  to be larger or smaller than 1? 
// 



// 2b) Log-likelihood as a function of  𝜇 
//
// Draw the log-likelihood as a function of the parameter  𝜇 .



// 2c) Best-fit signal strength  𝜇̂ 
//
// Find the approximate best-fit value of  𝜇̂ .
//


// 
// 2d) Uncertainty on  𝜇̂ 
//
// Find the approximate value for the uncertainty on  𝜇̂ .
//


// 
// Exercise 3: Significance calculation
//
// Assuming the expression for a counting experiment, calculate the expected and observed signal significance taking into account the total number of signal, background or observed events (as needed).
//
//3a) Expected significance
//
//



// 
// 3b) Observed significance
//




