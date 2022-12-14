CREATE TABLE IF NOT EXISTS Metadata_Crew (
     metadata_id 		INTEGER 			NOT NULL
    ,crew_id 			VARCHAR(24) 	NOT NULL

    ,CONSTRAINT fk_ref_metadata
		FOREIGN KEY (metadata_id)
    		REFERENCES Metadata (id)

    ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (crew_id)
    		REFERENCES Crew (id)

    ,PRIMARY KEY (metadata_id, crew_id)
);
