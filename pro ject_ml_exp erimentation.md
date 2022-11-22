#### SER594: Machine Learning Evaluation
#### TODO Hazardous Asteroid Prediction
#### TODO Mayank Mathur
#### TODO November 21, 2022

## Explainable Records
### Record 1
**Raw Data:** 3.4,939.4,0.09,2458600.5,0.0760090265983052,414267106.23553926,382779066.73887926,10.59406719506626,80.30553090445737,73.59769469844186,77.37209751948711,445755145.7321993,0.2138852265918273,2458238.7541293176,1683.145702657688,238579088.0,1,0,0,0,0,0,0,0,1,0,0,0,0




Prediction Explanation:** Prediction Made:0, Actual Class: 0, That means that the given asteroid is not Potentially Hazardous.This makes sense based on scientefic knowledge aswell. The asteroid is a main belt class asteroids which are located in the asteroid belt between Mars and Jupiter. These asteroids are pretty far away from earth and have extremely stable orbits due to Jupiters high gravitational pull. 

### Record 2
**Raw Data:**  4.2,545.0,0.101,2459000.5,0.2299722588646258,414966678.65704536,319535854.2127334,34.83293159121413,173.0247412488342,310.2023924446679,144.9756754788195,510397503.1013574,0.213344586343708,2458320.9623657744,1687.410991624711,184649784.00000003,1,0,0,0,0,0,0,0,1,0,0,0,0

Prediction Explanation:** Prediction Made:0, Actual Class: 0, That means that the given asteroid is not Potentially Hazardous.This makes sense based on scientefic knowledge aswell. The asteroid is a main belt class asteroids which are located in the asteroid belt between Mars and Jupiter. These asteroids are pretty far away from earth and have extremely stable orbits due to Jupiters high gravitational pull. 

## Interesting Features
### Feature A
**Feature:** NEO_Y

**Justification:** This is interesting feature as it tells whether the asteroid is a near earth object. If yes it makes it more likely to be potentially hazardous. 

### Feature B
**Feature:** Class_APO

**Justification:** This is class of Near Earth objects which have the orbit radius almost equal to earth. Hence these are extremely close to us and keeps intersecting with earths orbit. Belonging to this category will greatly increase the chances of asteroid being potentially hazardous. 

## Experiments 
### Varying A
**Prediction Trend Seen:** It can be seen that if NEO is set to 0, all the predictions made are 0. That is if the asteroid is not near earth, it is not potentially hazardous. 

### Varying B
**Prediction Trend Seen:** It can be seen that if class_APO is set to 0, all the predictions made are 0. That is if the asteroid is not in this orbit class, it is not potentially hazardous. 

### Varying A and B together
**Prediction Trend Seen:** For an asteroid to be class_APO, it needs to be NEO aswell. This was observed during testing, No records exsit of an asteroid which isnt NEO but is class_AP0.Which makese sense as APO class orbit is extremely close to earth. When both these features are true, Model gave the highest percentage of potentially hazardous prediction when compared to any other combinatation of values.
