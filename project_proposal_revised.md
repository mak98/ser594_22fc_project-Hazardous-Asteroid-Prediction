#### SER594: Project Proposal
#### Hazardous Asteroid Prediction
#### Mayank Mathur
#### October 29,2022
#### Keywords
Hazardous Asteroids, NASA Jet Propulsion , Classifier,
#### Description
For this project, I will be using JPL Small-Body Database Search Engine which is maintained by Nasa Jet Propulsion Lab. I will use their search engine to get a dataset of asteroids and then analyze it. Classification models will be trained to then try to classify asteroids into potentially hazardous asteroids. This can be done as JPL Small-Body Dataset has a column marking asteroids as potentially hazardous. I will use this data to train on a subset of the dataset hosted and then run predictions on a validation set.
#### Research Questions
<ol>
   <li>
       RO1: To describe the trends within data on how the diameter of an asteroid changes its absolute magnitude(luminosity).
   </li>
   <li>
       RO2:To predict if an asteroid is hazardous based on its orbital properties and size.
   </li>
   <li>
       RO3: To defend the model for performing the prediction of potentially hazardous asteroids using correct accuracy metrics and validation.
   </li>
   <li>
       RO4: To evaluate causal relationships implied by the RO2 model regarding what attributes have effect on an asteroid being potentially hazardous or not.
   </li>
</ol>
#### Intellectual Merit
Creating a hazardous asteroid prediction model can help scientists classify any potential new asteroids that get discovered or if any old one deviates from its original behavior.This will give information about what attributes of the asteroid can make it potentially hazardous to Earth and allow us to better classify newly discovered asteroids. While classification models already exist for this problem, the papers I found only focused on implementing deep learning models without any explanation as to why they chose this approach. Deep learning models being black box models won't give any insight into what attributes contribute towards making an asteroid potentially hazardous. This is why I want to implement multiple classification algorithms (including deep learning) to get a better understanding of the data and also make a powerful classifier.
#### Data Sourcing
The data will be sourced from JPL Small-Body Database Search Engine(https://ssd.jpl.nasa.gov/tools/sbdb_query.html). The data is publicly available and can be exported as CSV. The data is reliable but has empty values therefore some cleaning needs to be done.
#### Related Work:
Few research papers I have found useful for this problem:
[1] R. N. Ranaweera and T. Fernando, "Prediction of Potentially Hazardous Asteroids using Deep Learning," 2022 2nd International Conference on Advanced     Research in Computing (ICARC), 2022, pp. 31-36, doi: 10.1109/ICARC54489.2022.9753945,
[2] Upender, K., Krishna, T.S., Pothanna, N., Kumar, P.V.S. (2022). Predicting the Potentially Hazardous Asteroid to Earth Using Machine Learning. In: Reddy, A.B., Kiranmayee, B., Mukkamala, R.R., Srujan Raju, K. (eds) Proceedings of Second International Conference on Advances in Computer Engineering and Communication Systems. Algorithms for Intelligent Systems. Springer, Singapore. https://doi.org/10.1007/978-981-16-7389-4_34
[3] Davide Perna, Maria Antonietta Barucci. GRASPING THE NATURE OF POTENTIALLY HAZARDOUS ASTEROIDS. D. Perna et al 2016 AJ 151 11
[4]Pasko, V. (2018). Prediction of Orbital Parameters for Undiscovered Potentially Hazardous Asteroids Using Machine Learning. In: Vasile, M., Minisci, E., Summerer, L., McGinty, P. (eds) Stardust Final Conference. Astrophysics and Space Science Proceedings, vol 52. Springer, Cham. https://doi.org/10.1007/978-3-319-69956-1_3
[5] Petrov, Nikita & Sokolov, Leonid & Polyakhova, Elena & Oskina, K.. (2018). Predictions of asteroid hazard to the Earth for the 21st century. AIP Conference Proceedings. 1959. 040012. 10.1063/1.5034615.
 
 
 
 

