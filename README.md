# 🛡️ Scanner de Ports Réseau Interactif (Python)

Ce projet est un script Python interactif conçu pour auditer la sécurité d'une machine ou d'un domaine en scannant ses ports réseau les plus courants.

## 🚀 Fonctionnalités
- **Saisie Interactive** : Permet à l'utilisateur de spécifier une cible (Nom de domaine ou IP).
- **Résolution DNS automatique** : Convertit les noms de domaine (ex: ynov.com) en adresses IPv4 brutes via le module `socket`.
- **Audit Multi-ports** : Analyse l'état (Ouvert/Fermé) des ports standards (FTP, SSH, HTTP, HTTPS...).
- **Robustesse** : Gestion des interruptions utilisateur (`Ctrl+C`) pour une fermeture propre du script sans plantage.

## 🛠️ Technologies & Notions clés
- **Python 3** (Module natif `socket` pour les connexions TCP, `sys`)
- **Réseau** : Protocoles TCP/IP, Résolution DNS, Ports et Services.
- **Git & GitHub** pour le versioning.

## 📈 Objectif pédagogique
Ce projet permet de comprendre les mécanismes fondamentaux de la communication réseau (Three-way handshake TCP) et d'appréhender la première phase d'un audit de sécurité (Reconnaissance / Gathering d'informations).