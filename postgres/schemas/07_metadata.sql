CREATE TABLE IF NOT EXISTS Metadata (
     id 					INTEGER 				NOT NULL
	 ,imdb_id 			VARCHAR(9) 			NOT NULL
	 ,title 				VARCHAR(255) 		NOT NULL
	 ,overview 			VARCHAR
	 ,popularity 		FLOAT 				NOT NULL
	 ,release_date 	DATE 					NOT NULL
	 ,runtime 			FLOAT 				NOT NULL
	 ,vote_average 	FLOAT 				NOT NULL
	 ,vote_count 		INTEGER 				NOT NULL

    ,PRIMARY KEY (id)
);
