CREATE TABLE IF NOT EXISTS MCMetadataLanguage (
     metadata_id 		INTEGER 			NOT NULL
    ,language_id 		VARCHAR(2) 		NOT NULL

    ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES MCMetadata (id)

    ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (language_id)
    		REFERENCES MCLanguage (id)

    ,PRIMARY KEY (metadata_id, language_id)
);
