CREATE TABLE IF NOT EXISTS Metadata_Country (
     metadata_id 		INTEGER 			NOT NULL
    ,country_id 		VARCHAR(2) 		NOT NULL

    ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES Metadata (id)

    ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (country_id)
    		REFERENCES Country (Id)

    ,PRIMARY KEY (metadata_id, country_id)
);
