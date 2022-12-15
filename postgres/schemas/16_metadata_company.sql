CREATE TABLE IF NOT EXISTS MCMetadataCompany (
     metadata_id 		INTEGER 		NOT NULL
    ,company_id 		INTEGER 		NOT NULL

    ,CONSTRAINT fk_ref_metadata
    	FOREIGN KEY (metadata_id)
    		REFERENCES MCMetadata (id)

    ,CONSTRAINT fk_ref_genre
    	FOREIGN KEY (company_id)
    		REFERENCES MCCompany (id)

    ,PRIMARY KEY (metadata_id, company_id)
);
