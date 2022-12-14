CREATE TABLE IF NOT EXISTS Metadata_Genre (
    metadata_id 	INTEGER 		NOT NULL
   ,genre_id 		INTEGER 		NOT NULL

   ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES Metadata (id)

	,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (genre_id)
    		REFERENCES Genre (Id)

   ,PRIMARY KEY (metadata_id, genre_id)
);
