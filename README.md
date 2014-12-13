# Projet de Python avancé (2014)

_par Peter Naylor & Guillaume Demonet, encadré par Xavier Dupré._

## __Remerciements adressés à__ 

Bache, K. & Lichman, M. (2013). [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science

## Problématique générale

> Le projet informatique sera centré sur la résolution d’un problème de machine learning. Il s’agit d’expérimenter deux (ou trois) modèles sur un même jeu de données, d’interpréter les résultats et de les présenter.

## Introduction

### Jeu de données

Nous avons choisi de réaliser ce projet à partir du jeu de données "[_Musk (Version 2) Data Set_](https://archive.ics.uci.edu/ml/datasets/Musk+%28Version+2%29)", obtenu sur le site de l'_UCI Machine Learning Repository_.

Voici une liste non-exhaustive d'informations importantes concernant ce _dataset_ :

* Nombre d'observations : __6598__
* Nombre de variables : __168__
* Type des variables : __Entier numérique__
* Problème associé au jeu de données : __Classification binaire__
* Date du jeu de données : __12/09/1994__

Pour éclaircir les esprits de chacun, le terme __musc__ désigne :

> _a class of aromatic substances commonly used as base notes in perfumery_.
> ([Wikipedia](http://en.wikipedia.org/wiki/Musk))

Cette table décrit un ensemble de 102 molécules, dont 39 ont été labellées par des experts humains comme __muscs__ et les 63 restantes comme __non-muscs__. L'objectif est de prédire si de nouvelles molécules sont des muscs ou non.

Les 6598 observations correspondent aux différents _[conformères](http://fr.wikipedia.org/wiki/Conform%C3%A9rie)_ de chaque molécule, musc ou non. La particularité de ce _dataset_ est que plusieurs observations (_= conformations_) correspondent à une seule molécule ; on parle alors de "[multiple instance learning](http://en.wikipedia.org/wiki/Multiple-instance_learning)" ou __MIL__, ce qui correspond dans notre cas à une __classification binaire__ de _"paquets" d'observations_, classés non-muscs si toutes leurs observations sont elles-mêmes non-muscs, classés muscs sinon.

__En pratique__, nos données sont fournies au format [C4.5](http://www2.cs.uregina.ca/~dbd/cs831/notes/ml/dtrees/c4.5/c4.5.html), avec un fichier `clean2.data` et un fichier `clean2.names`. Pour plus de détails sur ce format de base de données, une description simplifiée est disponible [ici](http://www.cs.washington.edu/dm/vfml/appendixes/c45.htm). L'absence de fichier `clean2.test` implique l'obligation d'utiliser des méthodes de [Cross-validation](http://en.wikipedia.org/wiki/Cross-validation_(statistics)).
