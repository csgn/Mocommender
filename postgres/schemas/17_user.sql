CREATE TABLE IF NOT EXISTS User (
	 id						SERIAL			NOT NULL
	,username				VARCHAR(32)		NOT NULL
	,is_active				BOOLEAN			NOT NULL
													DEFAULT FALSE
	
	,PRIMARY KEY (id)
);
