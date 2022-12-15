CREATE TABLE IF NOT EXISTS MCCrew (
     id 					VARCHAR(24) 		NOT NULL
	 ,employee_id		INTEGER 				NOT NULL
    ,department 		VARCHAR(512) 		NOT NULL
    ,job 				VARCHAR(512) 		NOT NULL
    ,name 				VARCHAR(512) 		NOT NULL
    ,gender 			SMALLINT 			NOT NULL
    ,profile_path 	VARCHAR(512)

    ,PRIMARY KEY (id)
);
