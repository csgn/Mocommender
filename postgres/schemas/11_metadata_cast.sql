CREATE TABLE IF NOT EXISTS MCMetadataCast (
    metadata_id 	INTEGER 			NOT NULL
   ,cast_id 		VARCHAR(24) 	NOT NULL

   ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES MCMetadata (id)

   ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (cast_id)
    		REFERENCES MCCast (id)

   ,PRIMARY KEY (metadata_id, cast_id)
);
