# Specification du projet Video.AI

## 1. Étude des concurrents existants

### 1.1 Concurrents existants

- **Fliki**
- Génération de vidéos à partir de texte avec synthèse vocale avancée.
- Large bibliothèque de vidéos et images libres de droits.
- Personnalisation limitée des animations et visuels.

- **Synthesia**
- Génération de vidéos avec avatars IA et voix réalistes.
- Multilingue avec support des sous-titres.
- Moins adapté aux vidéos créatives et narration libre.

- **Pictory**
- Conversion de scripts texte en vidéos illustrées automatiquement.
- Bon choix de modèles et personnalisation de sous-titres.
- Limitations sur les voix et le style visuel des vidéos.

### 1.2 Différenciation de Video.AI
- Personnalisation avancée des animations et effets.
- Synthèse vocale améliorée avec ajustements dynamiques.
- Génération de vidéos optimisées pour le marketing et l’e-learning.

---

## 2. Besoins fonctionnels


### 2.1 Entrée utilisateur
- **Saisie de texte** : Interface permettant aux utilisateurs d’entrer du texte ou d’importer un script.
- **Choix de la voix** : Sélection de voix IA (genre, accent, vitesse).
- **Personnalisation des styles** : Ajustement du ton et du rythme de la voix.

### 2.2 Génération de vidéo
- **Transformation du texte en narration vocale**.
- **Ajout automatique d’images et de vidéos libres de droits** basés sur le texte.
- **Insertion de sous-titres automatiques synchronisés**.
- **Choix de thèmes et animations personnalisées**.

### 2.3 Édition et personnalisation
- **Modification manuelle des visuels et de l’audio**.
- **Ajout de musique de fond et effets sonores**.
- **Ajustement des transitions et animations**.

### 2.4 Exportation et partage
- **Génération de vidéos en haute résolution (HD, 4K)**.
- **Exportation aux formats MP4, MOV**.
- **Partage direct sur les réseaux sociaux**.

---

## 3. Besoins non fonctionnels

### 3.1 UI/UX
- **Interface intuitive et moderne** basée sur React.js.
- **Expérience utilisateur fluide et optimisée pour mobile et desktop**.
- **Accessibilité pour tous types d’utilisateurs**.

### 3.2 Performance
- **Traitement rapide des requêtes IA** grâce à une architecture optimisée.
- **Support pour un grand volume de données multimédias**.
- **Scalabilité pour gérer un grand nombre d’utilisateurs simultanés**.

---

## 4. Spécifications techniques


### 4.1 Backend
- **Technologie** : Python (Flask/FastAPI)
- **Fonctionnalités** :
- RESTful API pour la gestion des requêtes utilisateur.
- Intégration avec des modèles IA pour la génération vocale et vidéo.

### 4.2 Frontend
- **Technologie** : React.js (avec TypeScript pour plus de robustesse).
- **Principales fonctionnalités** :
- Interface utilisateur dynamique et réactive.
- Aperçu en temps réel des vidéos générées.

### 4.3 Base de données
- **Technologie** : PostgreSQL
- **Caractéristiques** :
- Stockage des métadonnées des vidéos générées.
- Indexation pour optimiser la recherche et le filtrage.
## 5. Diagrammes 
### 5.1 Diagramme des cas d'utilisation
![Diagramme des cas d'utilisation](<Diagramme des cas d'utilisation.png>)
- Donner un Feedback
-Partage sur Réseaux Sociaux
-Enregistrement des Créations
-Aperçu des Créations
-Personnalisation de la Vidéo
-Sélection de la Durée
-Sélection de la Résolution
-Entrée de Texte
### 5.2  Diagramme d'activité
-L'utilisateur crée et personnalise une vidéo en choisissant des options comme le texte, la résolution et la durée, puis génère, prévisualise et partage la vidéo. La vidéo contient des propriétés (texte, résolution, durée, personnalisation) et des méthodes pour la génération, la prévisualisation, l'enregistrement et le partage.
-La vidéo comprend des propriétés telles que le texte, la résolution, la durée et la personnalisation. Elle offre des méthodes pour générer, prévisualiser, enregistrer et partager la vidéo créée.
![Diagramme d'activité](<Diagramme d'activité.png>)
### 5.3 Diagramme de séquence
 **Utilisateur** : L'utilisateur interagit avec l'interface pour entrer du texte, choisir des paramètres, personnaliser et enregistrer la vidéo.

 **UI** : L'interface utilisateur (UI) transmet les actions de l'utilisateur (texte, paramètres, personnalisation) au **VideoController** pour traitement et affichage.

 **VideoController** : Le contrôleur vidéo gère les actions de l'utilisateur, envoie les demandes au **VideoGenerator**, et contrôle l'affichage des vidéos dans l'UI.

 **VideoGenerator** : Le générateur de vidéo analyse le texte, génère la vidéo, applique les personnalisations et retourne la vidéo traitée au **VideoController**.

 **Database** : La base de données enregistre la vidéo générée et retourne une confirmation au **VideoController** après l'enregistrement.
![Diagramme de séquence](<Diagramme de séquence.png>)


## 6. Déploiement

### 6.1 Infrastructure
Le projet sera déployé sur un serveur **Linux Ubuntu**, avec les technologies suivantes :
- **Python 3.12** pour le backend.
- **Node.js 22 LTS** pour le frontend.
- **PostgreSQL 16 Server** pour le stockage.

### 6.2 Hébergement et cloud
- **Stockage des vidéos sur un serveur cloud (AWS S3 ou équivalent)**.
- **Utilisation de serveurs GPU pour le rendu IA rapide**.

## 7. Conclusion

Video.AI vise à révolutionner la création de vidéos en automatisant le processus de génération à partir de texte, grâce à l'intelligence artificielle. L'étude des concurrents a mis en évidence des opportunités d'amélioration, notamment en matière de personnalisation, de qualité vocale et de flexibilité des animations.

Grâce à une architecture moderne basée sur **React.js, Flask/FastAPI et PostgreSQL**, l'application garantira une **expérience utilisateur fluide**, une **génération rapide de vidéos**, et une **scalabilité optimale**.
