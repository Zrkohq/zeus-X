# ⚡ ZEUS-X

<p align="center">
  <strong>OSINT TOOLKIT · RECON · INTELLIGENCE</strong>
  <br>
  <sub>Un accès rapide à 90 ressources OSINT depuis une seule interface.</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-6d28ff?style=flat-square">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776ab?style=flat-square">
  <img src="https://img.shields.io/badge/Platform-Windows-0078d4?style=flat-square">
  <img src="https://img.shields.io/badge/Tools-90-8b5cf6?style=flat-square">
</p>

---

## Aperçu

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1541564968464285726/1546164572883255336/image.png?ex=6a9ec978&is=6a9d77f8&hm=6b8795d057e0cd57a051ca10cf20afd0b626e41dad0c2b3311073d04933cbca1&" alt="ZEUS-X">
</p>

---

## À propos

**ZEUS-X** est un toolkit OSINT conçu pour centraliser rapidement des ressources de recherche, de reconnaissance et d'analyse.

Au lieu de chercher chaque service séparément, ZEUS-X regroupe **90 outils et ressources** dans une interface terminal unique.

> **Trouver le bon outil, le plus rapidement possible.**

ZEUS-X est principalement optimisé pour **Windows**, avec navigation au clavier, support de la souris, animations terminal et ouverture automatique des ressources dans le navigateur.

---

## ✦ Fonctionnalités

* **90 ressources** regroupées dans 9 catégories
* interface terminal personnalisée
* navigation clavier et souris
* ouverture instantanée des ressources
* animation ASCII au lancement
* thème sombre violet / bleu
* pagination entre les catégories
* détection automatique de Windows
* gestion avancée de la console Windows
* restauration de la console à la fermeture
* système de vérification des mises à jour
* détection des nouvelles versions GitHub
* gestion des erreurs réseau
* notification lors de la fermeture

---

## 📂 Catégories

| Catégorie      | Ressources |
| :------------- | ---------: |
| `SEARCHERS`    |         10 |
| `SEARCHERS II` |         10 |
| `OSINT`        |         10 |
| `SOCIAL`       |         10 |
| `RECON`        |         10 |
| `RÉSEAU`       |         10 |
| `PERSONNES`    |         10 |
| `IMAGES`       |         10 |
| `OUTILS`       |         10 |
| **Total**      |     **90** |

### SEARCHERS

`BrixHub` · `MultiSearch` · `SeekNow` · `OSINT Industries` · `Epieos`
`Fingerprint` · `IntelX` · `Snusbase` · `LeakCheck` · `DeHashed`

### SEARCHERS II

`Revealer` · `OSINTsearch` · `Leak-Lookup` · `IntelX Tools` · `Phonebook.cz`
`Hunter.io` · `EmailRep` · `VoilaNorbert` · `Clearbit` · `FullContact`

### OSINT

`OSINT Framework` · `Bellingcat Toolkit` · `IntelTechniques` · `WhatsMyName` · `Sherlock`
`Maigret` · `Blackbird` · `PhoneInfoga` · `theHarvester` · `SpiderFoot`

### SOCIAL

`Namechk` · `Instant Username` · `UserSearch` · `KnowEm` · `Social Searcher`
`IDCrawl` · `Picuki` · `Dumpor` · `Nitter` · `Wayback Machine`

### RECON

`SecurityTrails` · `crt.sh` · `DNSdumpster` · `ViewDNS` · `Whois.com`
`DomainTools` · `BuiltWith` · `Wappalyzer` · `Netcraft` · `urlscan`

### RÉSEAU

`Shodan` · `Censys` · `FOFA` · `ZoomEye` · `LeakIX`
`IPinfo` · `AbuseIPDB` · `VirusTotal` · `GreyNoise` · `BGPView`

### PERSONNES

`TruePeopleSearch` · `FastPeopleSearch` · `Spokeo` · `Whitepages` · `BeenVerified`
`ThatsThem` · `FamilySearch` · `OpenStreetMap` · `Google Maps` · `Wikimapia`

### IMAGES

`Google Images` · `Yandex Images` · `TinEye` · `Bing Visual Search` · `PimEyes`
`FaceCheck ID` · `ExifTool Online` · `FotoForensics` · `ImgOps` · `InVID Verification`

### OUTILS

`CyberChef` · `Regex101` · `Base64 Decode` · `JWT.io` · `Hash Identifier`
`MXToolbox` · `DNSChecker` · `SimilarWeb` · `Archive.today` · `Pastebin`

---

## ⚙️ Installation

### Prérequis

* Windows 10 / 11 recommandé
* Python **3.10+**
* connexion internet

### 1. Cloner le projet

```bash
git clone https://github.com/Zrkohq/zeus-X.git
cd zeus-X
```

### 2. Installer les dépendances

```bash
pip install pystyle
```

### 3. Lancer ZEUS-X

```bash
python zeus-x.py
```

---

## 🎮 Navigation

|     Touche    | Action                |
| :-----------: | :-------------------- |
|   `1` → `9`   | ouvrir un outil       |
|      `0`      | ouvrir le 10ème outil |
|      `A`      | catégorie précédente  |
|      `E`      | catégorie suivante    |
|     `ESC`     | quitter               |
| `Clic gauche` | ouvrir un outil       |

> La navigation à la souris est principalement destinée à Windows.

---

## 🔄 Mise à jour

ZEUS-X vérifie automatiquement si une version plus récente est disponible sur GitHub.

Lorsqu'une nouvelle version est détectée, ZEUS-X affiche une confirmation avant d'ouvrir le dépôt.

```text
Version actuelle → 1.0.0
Nouvelle version → 1.1.0
```

Le système continue normalement si :

* aucune connexion n'est disponible
* GitHub est inaccessible
* la version distante est invalide
* aucune mise à jour n'est disponible

---

## 🖥️ Windows

ZEUS-X utilise certaines fonctionnalités natives de Windows afin d'améliorer l'expérience terminal.

Cela permet notamment :

* gestion des événements souris
* gestion des événements clavier
* modification du mode console
* désactivation du Quick Edit
* gestion du curseur
* changement du titre de la fenêtre
* restauration du mode console
* notification à la fermeture

---

## 🧩 Technologies

ZEUS-X repose principalement sur les modules natifs de Python :

```text
os
sys
time
math
shutil
threading
webbrowser
urllib
re
ctypes
```

Dépendance externe :

```text
pystyle
```

---

## 📁 Structure

```text
zeus-X/
│
├── zeus-x.py
├── version.txt
├── Dons.txt
└── README.md
```

---

# 💜 Soutenir ZEUS-X

Si ZEUS-X vous est utile et que vous souhaitez soutenir le développement du projet, vous pouvez effectuer un don.

Les dons en **cryptomonnaies** sont directement disponibles dans le fichier [`Dons.txt`](Dons.txt).

### 🪙 Cryptomonnaies acceptées

| Crypto  | Adresse                                        |
| :------ | :--------------------------------------------- |
| **LTC** | `LeNMihZGAp3EHnHeciMPBu3UfuCrwVhFfG`           |
| **BTC** | `bc1qlquheug3l39xzgutgujqvxqmsjfx34m5pqhq5c`   |
| **ETH** | `0x96c0EFc0f13201bF62be565A3B49277712D239A9`   |
| **SOL** | `5vRiGYLrdzmvAjLcJfcwwUDBH6e16ayKaDjLCFy8MVZb` |

### 💳 Autres moyens de paiement

Vous souhaitez faire un don avec **PaySafeCard**, ou avec un autre moyen de paiement ?

Contactez simplement **`5n8z` sur Discord** afin de voir les possibilités disponibles.

> Merci à toutes les personnes qui soutiennent ZEUS-X ❤️
> Chaque don contribue directement au temps consacré au développement et aux futures améliorations du projet.

---

## ⚠️ Utilisation responsable

ZEUS-X est un **launcher de ressources OSINT**.

Les services accessibles depuis le programme sont des services tiers et leurs conditions d'utilisation respectives s'appliquent.

Utilisez ZEUS-X uniquement dans un cadre légal et autorisé :

* recherche OSINT
* cybersécurité
* recherche académique
* veille
* investigation autorisée
* reconnaissance de vos propres infrastructures

**L'utilisateur est responsable de l'utilisation des ressources accessibles depuis ZEUS-X.**

---

## 🛠️ Roadmap

### `v1.0.0`

* [x] Interface terminal
* [x] 90 ressources
* [x] 9 catégories
* [x] Navigation clavier
* [x] Navigation souris Windows
* [x] Ouverture automatique des outils
* [x] Animation de démarrage
* [x] Gestion avancée de la console
* [x] Vérification des versions
* [x] Système de mise à jour

### À venir

* [ ] recherche interne
* [ ] favoris
* [ ] configuration personnalisable
* [ ] davantage de ressources
* [ ] système de plugins
* [ ] améliorations Linux
* [ ] nouvelles animations

---

## 🤝 Contribution

Les contributions sont les bienvenues.

Pour proposer une amélioration, une correction ou une nouvelle ressource :

1. Fork le projet
2. Crée une branche
3. Effectue tes modifications
4. Ouvre une Pull Request

Les nouvelles ressources doivent être pertinentes, accessibles publiquement et placées dans la catégorie appropriée.

---

## 👤 Auteur

**Zrko**

ZEUS-X est développé avec l'objectif de proposer un toolkit OSINT **simple, rapide et propre**, sans multiplier les fenêtres ou les recherches inutiles.

---

<p align="center">
  <strong>ZEUS-X</strong>
  <br>
  <sub>Search smarter. Investigate faster.</sub>
</p>
