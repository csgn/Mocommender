CREATE TABLE IF NOT EXISTS MCMetadataCountry (
     metadata_id 		INTEGER 			NOT NULL
    ,country_id 		VARCHAR(2) 		NOT NULL

    ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES MCMetadata (id)

    ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (country_id)
    		REFERENCES MCCountry (Id)

    ,PRIMARY KEY (metadata_id, country_id)
);
