/*
 * Vincent Houle
 * 
 * script pour les users et les fonctions et procédures et triggers
 * 
 */

USE tp_livre;


DELIMITER $$

CREATE TRIGGER IF NOT EXISTS insertDonneeNonVide
	BEFORE INSERT
	ON personnage FOR EACH ROW 
	BEGIN
		
		IF NEW.nom IS NULL OR NEW.nom = "" THEN 
			SET NEW.nom = "nomVide";
		END IF;
	
		IF NEW.argent IS NULL THEN 
			SET NEW.argent = 0;
		END IF;
		
		IF NEW.habilite IS NULL THEN 
			SET NEW.habilite = 0;
		END IF;
	
		IF NEW.endurance IS NULL THEN 
			SET NEW.endurance = 0;
		END IF;
		
		IF NEW.objet_speciaux IS NULL OR NEW.objet_speciaux = "" THEN 
			SET NEW.objet_speciaux = "pas d'objet";
		END IF;
	
		IF NEW.repas IS NULL OR NEW.repas = "" THEN 
			SET NEW.repas = "pas de nourriture";
		END IF;
	
		IF NEW.equipement IS NULL OR NEW.equipement = "" THEN 
			SET NEW.equipement = "pas d'équipement";
		END IF;
	END $$
	
CREATE TRIGGER IF NOT EXISTS updateDonneesNonVide
	BEFORE UPDATE 
	ON personnage FOR EACH ROW 
	BEGIN
		
		IF NEW.nom IS NULL OR NEW.nom = "" THEN 
			SET NEW.nom = "nomVide";
		END IF;
	
		IF NEW.argent IS NULL THEN 
			SET NEW.argent = 0;
		END IF;
		
		IF NEW.habilite IS NULL THEN 
			SET NEW.habilite = 0;
		END IF;
	
		IF NEW.endurance IS NULL THEN 
			SET NEW.endurance = 0;
		END IF;
		
		IF NEW.objet_speciaux IS NULL OR NEW.objet_speciaux = "" THEN 
			SET NEW.objet_speciaux = "pas d'objet";
		END IF;
	
		IF NEW.repas IS NULL OR NEW.repas = "" THEN 
			SET NEW.repas = "pas de nourriture";
		END IF;
	
		IF NEW.equipement IS NULL OR NEW.equipement = "" THEN 
			SET NEW.equipement = "pas d'équipement";
		END IF;
	END $$

DELIMITER ;
	
CREATE USER IF NOT EXISTS 'aventurier'@'%' IDENTIFIED BY 'dnd';

GRANT SELECT
ON tp_livre.*
TO aventurier;

GRANT INSERT, UPDATE, DELETE
ON tp_livre.personnage
TO aventurier;

GRANT INSERT, UPDATE, DELETE
ON tp_livre.arme_personnage 
TO aventurier;

GRANT INSERT, UPDATE, DELETE
ON tp_livre.discipline_personnage 
TO aventurier;


	
	