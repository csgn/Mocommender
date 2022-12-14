CREATE TABLE IF NOT EXISTS Metadata_Language (
     metadata_id 		INTEGER 			NOT NULL
    ,language_id 		VARCHAR(2) 		NOT NULL

    ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES Metadata (id)

    ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (language_id)
    		REFERENCES Language (id)

    ,PRIMARY KEY (metadata_id, language_id)
);
