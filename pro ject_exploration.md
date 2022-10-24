#### SERX94: Exploratory Data Munging and Visualization
#### Hazardous Asteroid Prediction
#### Mayank Mathur
#### October 22,2022
 
## Basic Questions
**Dataset Author(s):** Nasa Jet Propulsion Laboratory
 
**Dataset Construction Date:** Updates every day.Downloaded on October 23,2022.
 
**Dataset Record Count:** 958524
 
**Dataset Field Meanings:**
 
   SPK-ID: identifier in the JPL Small-Body Database
   Object ID: Object internal database ID
   Object fullname: Object full name/designation
   pdes: Object primary designation
   name: Object IAU name
   NEO: Near-Earth Object (NEO) flag
   PHA: Potentially Hazardous Asteroid (PHA) flag
   H: Absolute magnitude parameter.The visual magnitude an observer would record if the asteroid were placed 1 Astronomical Unit (au) away, and 1 au from the Sun and at a zero phase angle. The value is reverse logrithmic.
   Diameter: object diameter (from equivalent sphere) Km Unit
   Albedo: Geometric albedo
   Diameter_sigma: 1-sigma uncertainty in object diameter Km Unit
   Orbit_id: Orbit solution ID
   Epoch: Epoch of osculation in modified Julian day form
   Equinox: Equinox of reference frame
   e: Eccentricity of orbit
   a: Semi-major axis of orbit
   q: perihelion distance
   i: inclination; angle with respect to x-y ecliptic plane
   tp: Time of perihelion passage
   moid: Earth Minimum Orbit Intersection Distance
   class: Orbit class of the asteroid.
   per:Time period of 1 orbit in days
   Ad: Aphelion Distance
   ma:Mean Anomaly
   W: Argument of Perihelion
   om:Longitude of ascending node
   
Any column with sigma prefix is 1-sigma uncertainty in the measure of non prefix column value.
   Any column with ld as a suffix is the same measurement in Lunar Distance.
 
**Dataset File Hash(es):** 
md5sum dataset.csv
3e7d6562e4aee1430560c020a3311a46  dataset.csv
 
## Interpretable Records(after pre process)
### Record 1
**Raw Data:** 0,N,N,3.4,939.4,0.09,2458600.5,0.0760090265983052,414267106.23553926,382779066.73887926,10.59406719506626,80.30553090445737,73.59769469844186,77.37209751948711,445755145.7321993,0.2138852265918273,2458238.7541293176,1683.145702657688,238579088.0,MBA
 
Interpretation:** N for NEO means that the asteroid is not near to earth. N for PHA means the asteroid is not potentially hazardous to earth. The asteroid has a diameter of 939.4 Km and its albedo(fraction of light it reflects) is 0.09. The eccentricity of the orbit of the asteroid is 0.07, ‘a’ value represents the length of the semi-major axis of the orbit which is 41425…Km. Its shortest distance from the sun q=38277… Km and the furthest distance from the sun ,ad=4457…Km. It has an angle of inclination of 10 degrees. It comes under Main belt asteroid(MBA) orbit class. The asteroid takes 1683.14 days to finish its orbit. (rest of the columns are extremely difficult to explain in plain english)
### Record 2
**Raw Data:** N,N,4.2,545.0,0.101,2459000.5,0.2299722588646258,414966678.65704536,319535854.2127334,34.83293159121413,173.0247412488342,310.2023924446679,144.9756754788195,510397503.1013574,0.213344586343708,2458320.9623657744,1687.410991624711,184649784.00000003,MBA
 
**Interpretation:**
N for NEO means that the asteroid is not near to earth. N for PHA means the asteroid is not potentially hazardous to earth. The asteroid has a diameter of 545 Km and its albedo(fraction of light it reflects) is 0.101. The eccentricity of the orbit of the asteroid is 0.22, ‘a’ value represents the length of the semi-major axis of the orbit which is 4149…Km. Its shortest distance from the sun is q=319… Km and the furthest distance from the sun is ad=510…Km. It has an angle of inclination of 34.8 degrees. It comes under Main belt asteroid(MBA) orbit class. The asteroid takes 1687.41 days to finish its orbit. (rest of the columns are extremely difficult to explain in plain english)
 
 
## Data Sources
### Transformation 1
**Description:** Columns with Ids,sigma prefix and ld suffix were dropped as they don't contribute much towards finding potential hazardous asteroids or are the same values in a different unit.
### Transformation 2
**Description:** Unit conversion was done to standardize the units
 
**Soundness Justification:** Some columns had data in the Astronomical unit which was converted to Killo-Meter.
*Note* for not removing outliers from a: While the outlier value skews graphs, the outliers are still real,observable and might be important for making predictions so I chose not to remove them.
## Visualization
### Visual 1 (diameter vs H)
**Analysis:** As it can be seen from the graph the value of H(absolute magnitude) decreases exponentially as the diameter increases.This makes sense logically as the light should increase as the size of the asteroid increases(H is reverse logarithmic and hence the value goes down as size increases)
 
### Visual 2 (diameter vs a)
**Analysis:** As it can be seen from the graph the value of a(length of semi major axis) does not change with respect to the diameter of the asteroid. This also makes sense realistically as the orbit of an object does not depend on its size. But most of the asteroids with small diameters also have less “a” value.
 
### Visual 3 (H vs a)
**Analysis:** As it can be seen from the plot ‘a’ value of an asteroid does not change with respect to H value. This also makes sense as the absolute magnitude is a standardized measure which would not depend on the orbital properties of the asteroid.
### Visual 4 (NEO)
**Analysis:** There is a massive class imbalance between the 2 categories(Yes and No). This aligns with known knowledge that not alot of objects are near earth.
### Visual 4 (class)
**Analysis:** MBA(Main Belt Asteroid) has majority of the asteroids. Since the asteroid belt between Jupiter and Mars has majority of all the asteroids in the solar system, it makes sense for most of the asteroids to be in this class.

