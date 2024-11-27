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
("Cash 'n' Guns", "party", "Some description", "", 3, 8, 6, 10, 70, 12),
("Klask", "party", "Some description", "", 3, 8, 6, 10, 70, 12),
("Catan", "party", "Some description", "", 3, 8, 6, 10, 70, 12),
("Monopoly", "party", "Some description", "", 3, 8, 6, 10, 70, 12);
