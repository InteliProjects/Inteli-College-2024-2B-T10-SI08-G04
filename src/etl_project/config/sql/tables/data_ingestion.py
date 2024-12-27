data_ingestion = '''                   
            CREATE TABLE IF NOT EXISTS grupo4.data_ingestion ( 
                data_ingest DateTime DEFAULT now(),
                data_content String NOT NULL,
                data_path String NOT NULL, 
                data_tag String NOT NULL,
                id String NOT NULL
            ) ENGINE = ReplacingMergeTree()
            ORDER BY id;
        '''