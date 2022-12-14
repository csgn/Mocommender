CREATE TABLE IF NOT EXISTS Metadata_Company (
     metadata_id 		INTEGER 		NOT NULL
    ,company_id 		INTEGER 		NOT NULL

    ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES Metadata (id)

    ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (company_id)
    		REFERENCES Company (id)

    ,PRIMARY KEY (metadata_id, company_id)
);
