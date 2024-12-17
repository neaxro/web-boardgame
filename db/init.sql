USE boardgame_web;

CREATE TABLE boardgame(
	id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    description LONGTEXT,
    tags TEXT,
    min_players INT NOT NULL,
    max_players INT NOT NULL,
    best_players INT,
    min_age INT NOT NULL,
    avg_time INT NOT NULL,
    played_count INT,
    PRIMARY KEY (id)
);

INSERT INTO boardgame (title, category, description, tags, min_players, max_players, best_players, min_age, avg_time, played_count) VALUES
("Cash 'n' Guns", "party", "Néhány leírás", "fegyverek,party,western", 3, 8, 6, 10, 70, 12),
("Klask", "party", "Néhány leírás", "labda,pingpong,valami szoveg", 3, 8, 6, 10, 70, 12),
("Catan", "stratégia", "Népszerű társasjáték, ahol a játékosok erőforrásokat gyűjtenek és településeket építenek.", "telepesek,erőforrások,kereskedelem,település", 3, 4, 4, 10, 90, 150),
("Monopoly", "családi", "Klasszikus játék ingatlanok vásárlásával és kereskedelmével.", "pénz,ingatlan,gazdaság", 2, 6, 4, 8, 60, 200),
("Scrabble", "szó", "Szójáték, ahol a játékosok betűtömböket használnak szavak alkotására.", "szavak,betűk,tábla", 2, 4, 3, 10, 45, 100),
("Codenames", "party", "Szórakoztató szóasszociációs játék.", "szavak,party,ügynök", 4, 8, 6, 14, 30, 80),
("Pandemic", "kooperatív", "A játékosok együtt dolgoznak a globális járvány megfékezésén.", "kooperatív,járvány,csapatmunka", 2, 4, 4, 8, 45, 75),
("Ticket to Ride", "stratégia", "Vasúti témájú társasjáték, ahol a játékosok versenyeznek a legjobb útvonalak kiépítéséért.", "vasút,utazás,városok", 2, 5, 4, 8, 60, 95),
("Uno", "kártya", "Klasszikus kártyajáték egyszerű szabályokkal és izgalmas fordulatokkal.", "kártyák,család,gyors", 2, 10, 6, 7, 20, 250),
("Jenga", "ügyességi", "Rakd és vedd le a fa darabokat anélkül, hogy ledőlnél a toronyból.", "torony,blokkok,party,ügyesség", 2, 6, 4, 5, 20, 120);

