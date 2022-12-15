CREATE TABLE IF NOT EXISTS MCMetadataKeyword (
     metadata_id 	INTEGER 	NOT NULL
    ,keyword_id 	INTEGER 	NOT NULL

    ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES MCMetadata (id)

    ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (Keyword_id)
    		REFERENCES MCKeyword (id)

    ,PRIMARY KEY (metadata_id, keyword_id)
);
