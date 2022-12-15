CREATE TABLE IF NOT EXISTS MCMetadataGenre (
    metadata_id 	INTEGER 		NOT NULL
   ,genre_id 		INTEGER 		NOT NULL

   ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES MCMetadata (id)

	,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (genre_id)
    		REFERENCES MCGenre (Id)

   ,PRIMARY KEY (metadata_id, genre_id)
);
