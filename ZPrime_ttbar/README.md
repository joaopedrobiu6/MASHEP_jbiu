# Projeto para a cadeira de Métodos de Análise e Simulação em Física de Altas Energias (P4 - 2023/2024)

## Z Prime search (Z' -> ttbar) 

Por:
- David Dias - 100297
- João Biu - 100335
- Manuel Ratola - 100339

Alunos do Mestrado em Engenharia Física Tecnológica no Instituto Superior Técnico

## Organização do Projeto
Os ficheiros estão organizados da seguinte forma:

- "/Output_ZPrimeBoostedAnalysis/" - Contém os ficheiros csv com os dados obtidos para a análise de dados utilizado o AtlasOpenFramework;
- "dataframe.csv" - Ficheiro csv com os eventos Monte Carlo gerados para a análise de dados. Contém os eventos de sinal e de background 
                  sendo que os dados de sinal possuem a 'label' 1, e os dados de background possuem a 'label' 0. A coluna 'scaleweight'
                  contém o peso de cada evento. Criada a partir dos ficheiros csv presentes na pasta "/Output_ZPrimeBoostedAnalysis/", e o código
                  presente no ficheiro "Dataframe_for_ML.ipynb";

- "DataExploration.ipynb" - Notebook com a análise exploratória dos dados onde são criados os histogramas dos dados, que depois são guardados na pasta "/Histograms_of_Variables/";
- "Dataframe_for_ML.ipynb" - Notebook com a criação do dataframe para a análise de dados. A partir dos ficheiros csv presentes na pasta "/Output_ZPrimeBoostedAnalysis/" é criado o
                             ficheiro "dataframe.csv".
- "DNN_upperlimit.ipynb" - Notebook com a análise de dados utilizando uma Deep Neural Network. Neste ficheiro é também realizada a obtenção do valor limite para o 
                            parâmetro mu (upper limit). Todos os resultados são guardados na pasta "/DNN_upperlimit/";
- "RF_upperlimit.ipynb" - Notebook com a análise de dados utilizando um Random Forest. Neste ficheiro é também realizada a obtenção do valor limite para o 
                            parâmetro mu (upper limit). Todos os resultados são guardados na pasta "/RF_upperlimit/".



