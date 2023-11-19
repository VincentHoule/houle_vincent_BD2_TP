/*
 * Vincent Houle
 * 
 * script de création de base de données et de tables
 * 
 */
DROP DATABASE IF EXISTS tp_livre;
CREATE DATABASE IF NOT EXISTS tp_livre;

USE tp_livre;

CREATE TABLE IF NOT EXISTS chapitre (
	id INT PRIMARY KEY AUTO_INCREMENT,
	no_chapitre INT,
	texte TEXT
);

CREATE TABLE IF NOT EXISTS personnage (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(55),
	objet_speciaux TEXT,
	repas TEXT,
	equipement TEXT,
	argent INT,
	habilite INT,
	endurance INT,
	chapitre INT,
	FOREIGN KEY (chapitre) REFERENCES chapitre(id)
);

CREATE TABLE IF NOT EXISTS arme (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(55)
);

CREATE TABLE IF NOT EXISTS discipline (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(55),
	description TEXT
);

CREATE TABLE IF NOT EXISTS arme_personnage (
	id_arme INT,
	id_personnage INT,
	num_arme INT,
	PRIMARY KEY (id_arme, id_personnage, num_arme),
	FOREIGN KEY (id_arme) REFERENCES arme(id),
	FOREIGN KEY (id_personnage) REFERENCES personnage(id)
);

CREATE TABLE IF NOT EXISTS discipline_personnage (
	id_discipline INT,
	id_personnage INT,
	num_discipline INT,
	PRIMARY KEY (id_discipline, id_personnage, num_discipline),
	FOREIGN KEY (id_discipline) REFERENCES discipline(id),
	FOREIGN KEY (id_personnage) REFERENCES personnage(id)
);

CREATE TABLE IF NOT EXISTS livre (
	id INT PRIMARY KEY AUTO_INCREMENT,
	titre VARCHAR(55),
	auteur VARCHAR(55)
);


CREATE TABLE IF NOT EXISTS chapitre_livre (
	id_livre INT,
	id_chapitre INT,
	PRIMARY KEY (id_livre, id_chapitre),
	FOREIGN KEY (id_livre) REFERENCES livre(id),
	FOREIGN KEY (id_chapitre) REFERENCES chapitre(id)
);

CREATE TABLE IF NOT EXISTS lien_chapitre (
	id_chapitre_origine INT,
	id_chapitre_destination INT,
	PRIMARY KEY (id_chapitre_origine, id_chapitre_destination),
	FOREIGN KEY (id_chapitre_origine) REFERENCES chapitre(id),
	FOREIGN KEY (id_chapitre_destination) REFERENCES chapitre(id)
);

CREATE TABLE IF NOT EXISTS prologue (
	id INT PRIMARY KEY AUTO_INCREMENT,
	titre VARCHAR(55),
	id_livre INT,
	texte TEXT,
	FOREIGN KEY (id_livre) REFERENCES livre(id)
);