## Projet de Python Avancé

Projet co-mené par Peter Naylor et Guillaume Demonet, encadré par Xavier Dupré, dans le cadre du cours de Python avancé de l'ENSAE.

### __Données utilisées__

Nous travaillons sur _"Musk (Version 2) Data Set"_, obtenue sur l'[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Musk+(Version+2)).

__Description du dataset__

This dataset describes a set of __102__ molecules of which 39 are judged by human experts to be musks and the remaining 63 molecules are judged to be non-musks. The goal is to learn to predict whether new molecules will be musks or non-musks. However, the __166 features__ that describe these molecules depend upon the exact shape, or conformation, of the molecule. Because bonds can rotate, a single molecule can adopt many different shapes. To generate this data set, all the low-energy conformations of the molecules were generated to produce __6,598 conformations__. Then, a feature vector was extracted that describes each conformation. 

This many-to-one relationship between feature vectors and molecules is called the __"multiple instance problem"__. When learning a classifier for this data, the classifier should classify a molecule as "musk" if ANY of its conformations is classified as a musk. A molecule should be classified as "non-musk" if NONE of its conformations is classified as a musk.

__Sources intéressantes sur le sujet__

[A comparison of dynamic reposing and tangent distance for drug activity prediction. Advances in Neural Information Processing Systems](http://rexa.info/paper/88e450c2c458d9ae8eaa9b556d2831b9801c1bfe)
_Dietterich, T. G., Jain, A., Lathrop, R., Lozano-Perez, T. (1994)._

[Compass: A shape-based machine learning tool for drug design. Computer-Aided Molecular Design.](http://rexa.info/paper/b6bbc5cefb7152095b94bf0f1d4dc2c0616b96fd)
_Jain, A. N., Dietterich, T. G., Lathrop, R. H., Chapman, D., Critchlow, R. E., Bauer, B. E., Webster, T. A., Lozano-Perez, T._

[Solving the multiple-instance problem with axis-parallel rectangles. Artificial Intelligence](http://rexa.info/paper/a0753191808f5c6345777b4ffef7cd74e210bfef)
_Dietterich, T. G., Lathrop, R. H., Lozano-Perez, T._
