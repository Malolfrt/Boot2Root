Boot2Root - Projet de cybersécurité (École 42)

Projet de groupe réalisé avec [Valentin mondor](https://github.com/vmondor)

🚀 Introduction

Boot2Root est un projet de l’école 42 qui consiste à exploiter une machine virtuelle vulnérable afin d’obtenir un accès root. L’objectif est de mettre en pratique des compétences en sécurité offensive, en analyse de vulnérabilités et en exploitation.

Ce projet s’inscrit dans le cursus sécurité de 42, en suivant une approche similaire à des défis de type CTF.

🎯 Objectifs pédagogiques

Approfondir les bases de la cybersécurité offensive

Identifier et exploiter des failles systèmes ou applicatives

Comprendre les mécanismes de privilège et d’escalade

Apprendre à manipuler des outils de reconnaissance et d’exploitation

🔍 Environnement

VM vulnérable fournie

Structure en plusieurs niveaux, nécessitant de passer de compte en compte (ssh, ftp, phpmyadmin...)

Objectif final : obtenir un shell root

🛠 Méthodologie (générale)

Le parcours complet inclut :

Reconnaissance avec des outils comme nmap ou dirbuster

Analyse de binaires et exploitation de buffer overflow

Exploitation de vulnérabilités connues, comme la faille Dirty COW (CVE-2016-5195)

Recherche de vecteurs dans des configurations faibles ou binaires SUID

📚 Outils utilisés

nmap

dirbuster

exploit-db

📁 Organisation du repo

Ce dépôt contient :

Des write-ups complet décrivant l’exécution des différentes étapes

Les exploits ou scripts nécessaires à la progression

Des binaires ou extraits utiles
