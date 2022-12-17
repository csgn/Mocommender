CREATE TABLE IF NOT EXISTS MCUserMovie (
	 id						SERIAL			NOT NULL
	,user_id					INTEGER			NOT NULL
	,movie_id				INTEGER			NOT NULL
	,is_played				BOOLEAN			NOT NULL
													DEFAULT FALSE
	,is_recommended		BOOLEAN			NOT NULL
													DEFAULT FALSE
	,is_liked				BOOLEAN			NOT NULL
													DEFAULT FALSE
	,is_saved				BOOLEAN			NOT NULL
													DEFAULT FALSE
	,play_runtime			FLOAT				NOT NULL
													DEFAULT 0.0
	,play_date				DATE				NOT NULL


	,CONSTRAINT fk_ref_user
		FOREIGN KEY (user_id)
			REFERENCES MCUser (id)
				ON UPDATE CASCADE
				ON DELETE CASCADE

	,CONSTRAINT fk_ref_movie
		FOREIGN KEY (movie_id)
			REFERENCES MCMetadata (id)
				ON UPDATE CASCADE
				ON DELETE CASCADE
	
	,PRIMARY KEY (id)
);
