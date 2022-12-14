CREATE TABLE IF NOT EXISTS Metadata_Cast (
    metadata_id 	INTEGER 			NOT NULL
   ,cast_id 		VARCHAR(24) 	NOT NULL

   ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES Metadata (id)

   ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (cast_id)
    		REFERENCES MCast (id)

   ,PRIMARY KEY (metadata_id, cast_id)
);
