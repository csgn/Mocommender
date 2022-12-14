CREATE TABLE IF NOT EXISTS MCast (
    id					VARCHAR(24) 	NOT NULL
	,actor_id			INTEGER 			NOT NULL
   ,name					VARCHAR(512) 	NOT NULL
   ,gender				SMALLINT 		NOT NULL
   ,cast_id				SMALLINT
   ,cast_character 	VARCHAR(512)
   ,cast_order 		SMALLINT
   ,profile_path 		VARCHAR(512)

   ,PRIMARY KEY (id)
);
