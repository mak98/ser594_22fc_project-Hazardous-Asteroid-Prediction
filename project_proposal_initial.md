#### SER594: Project Proposal
#### Creating and Analysing Asteroid Dataset and Hazardous Asteroid Prediction
#### Mayank Mathur
#### September 25,2022

Keywords: Data Classification, Machine Learning, Data Scraping , Neural Networks,Deep Learning. 

Description: For this project, I will be using JPL Small-Body Database Search Engine which is maintained by Nasa Jet Propulsion Lab. I will use their search engine to create my own dataset of astroids and then analyze it. Classification models will be trained to then try to classify asteroids into potentially hazardous asteroids. This can be done as JPL Small-Body Dataset has a column marking astroids as potentially hazardous. I will use this data to train on a subset of the dataset hosted and then run predictions on a validation set.

Intellectual Merit: Creating a hazardous asteroid prediction model can help scientists classify any potential new asteroids that get discovered or if any old one deviates from its original behavior. While classification models already exist for this problem, the papers I found only focused on implementing deep learning models without any explanation as to why they chose this approach. This is why I want to implement multiple classification algorithms and compare them to get a better understanding. 

Data Sourcing: The data will be source from JPL Small-Body Database Search Engine(https://ssd.jpl.nasa.gov/tools/sbdb_query.html). The data is publicly available and can be exported as CSV. The data is reliable but has empty values therefore some cleaning needs to done.

Related Work: Few research papers I have found useful for this problem:  
[1] R. N. Ranaweera and T. Fernando, "Prediction of Potentially Hazardous Asteroids using Deep Learning," 2022 2nd International Conference on Advanced     Research in Computing (ICARC), 2022, pp. 31-36, doi: 10.1109/ICARC54489.2022.9753945,
[2] Upender, K., Krishna, T.S., Pothanna, N., Kumar, P.V.S. (2022). Predicting the Potentially Hazardous Asteroid to Earth Using Machine Learning. In: Reddy, A.B., Kiranmayee, B., Mukkamala, R.R., Srujan Raju, K. (eds) Proceedings of Second International Conference on Advances in Computer Engineering and Communication Systems. Algorithms for Intelligent Systems. Springer, Singapore. https://doi.org/10.1007/978-981-16-7389-4_34