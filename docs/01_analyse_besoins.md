# Analyse des besoins

## 1. Contexte du projet

Le projet consiste à concevoir et développer un chatbot, ou agent conversationnel, dédié à l’apprentissage et à la sensibilisation à la cybersécurité.

L’objectif est de proposer un outil accessible permettant à un utilisateur de poser des questions liées à la sécurité informatique, d’obtenir des conseils compréhensibles et d’être guidé dans l’application de bonnes pratiques numériques.

Le chatbot devra notamment traiter des sujets comme les mots de passe, le phishing, la sécurité Wi-Fi, la messagerie chiffrée, les VPN, les mises à jour, les sauvegardes et la sécurité des réseaux.

## 2. Objectifs du projet

L’objectif principal est de créer un agent conversationnel capable d’aider les utilisateurs à mieux comprendre les risques liés à la cybersécurité et à adopter de meilleurs comportements.

Le chatbot devra :

- fournir des informations fiables sur différents aspects de la cybersécurité ;
- guider les utilisateurs dans la mise en place de bonnes pratiques ;
- répondre à certaines questions liées aux actions de l’UPHF dans le domaine de la sécurité des systèmes d’information ;
- gérer des conversations multi-tours ;
- être accessible depuis une application utilisable sur PC ou mobile ;
- suivre une architecture agentique ;
- être contenu dans un environnement Docker ;
- être versionné avec Git.

## 3. Public cible

Le chatbot s’adresse principalement :

- aux étudiants ;
- au personnel universitaire ;
- aux utilisateurs non spécialistes de la cybersécurité ;
- aux personnes souhaitant améliorer leurs pratiques numériques quotidiennes.

Le niveau de langage devra donc rester pédagogique, clair et accessible.

## 4. Besoins fonctionnels

Les besoins fonctionnels correspondent aux actions que le système doit permettre.

Le chatbot devra permettre à l’utilisateur de :

- poser une question en langage naturel ;
- obtenir une réponse claire et structurée ;
- demander des conseils sur les mots de passe ;
- comprendre les risques liés au phishing ;
- obtenir des recommandations pour sécuriser un réseau Wi-Fi ;
- recevoir des conseils sur l’utilisation d’un VPN ;
- être guidé sur les bonnes pratiques de messagerie et de navigation ;
- poser des questions liées à la sécurité informatique à l’UPHF ;
- poursuivre une conversation déjà commencée ;
- demander des précisions sur une réponse précédente ;
- utiliser une interface simple depuis un PC ou un appareil mobile.

## 5. Besoins non fonctionnels

Les besoins non fonctionnels décrivent les qualités attendues du système.

Le chatbot devra être :

- simple à utiliser ;
- compréhensible pour un utilisateur débutant ;
- suffisamment rapide dans ses réponses ;
- stable lors de la démonstration ;
- maintenable par l’équipe projet ;
- extensible pour ajouter de nouveaux agents ou de nouveaux thèmes ;
- sécurisé dans la gestion des échanges utilisateur ;
- exécutable dans un conteneur Docker ;
- documenté pour faciliter l’installation et l’utilisation.

## 6. Contraintes du projet

Plusieurs contraintes doivent être prises en compte :

- le projet est réalisé sur une durée limitée ;
- l’équipe est composée de 4 à 5 étudiants ;
- le projet doit donner lieu à plusieurs rendus intermédiaires ;
- l’application doit être démontrable lors de la soutenance finale ;
- l’utilisation d’outils payants doit être évitée autant que possible ;
- le code source doit être versionné avec Git ;
- l’application doit être contenue dans un Docker ;
- le chatbot doit respecter une architecture agentique.

## 7. Analyse des risques

| Risque | Impact | Solution prévue |
|---|---|---|
| Choix d’une technologie trop complexe | Retard dans le développement | Choisir une solution simple et maîtrisable |
| Modèle IA difficile à intégrer | Chatbot non fonctionnel | Prévoir une base de connaissances simple en secours |
| Mauvaise gestion du multi-tours | Réponses incohérentes | Ajouter un historique de conversation |
| Docker non fonctionnel | Problème lors de la démo | Tester Docker régulièrement |
| Manque de temps | Fonctionnalités incomplètes | Prioriser une version minimale fonctionnelle |
| Réponses cybersécurité dangereuses | Risque éthique | Limiter les réponses aux usages défensifs |

## 8. Périmètre du projet

Dans le cadre de ce projet, la version minimale attendue comprend :

- une interface de discussion ;
- un chatbot texte ;
- plusieurs agents spécialisés ;
- une base de connaissances cybersécurité ;
- une mémoire de conversation ;
- une partie liée aux actions de l’UPHF ;
- une application dockerisée ;
- des tests fonctionnels.

Certaines fonctionnalités pourront être ajoutées en bonus si le temps le permet :

- commande vocale ;
- quiz de sensibilisation ;
- recherche dans des documents ;
- amélioration graphique de l’interface ;
- historique sauvegardé des conversations.

## 9. Conclusion

Cette analyse montre que le projet ne se limite pas à un simple chatbot. Il s’agit d’une application complète combinant une interface utilisateur, un moteur conversationnel, une architecture agentique, une base de connaissances et une gestion du dialogue multi-tours.

La priorité sera donc de développer une version simple, stable et démontrable, répondant aux exigences principales du cahier des charges.