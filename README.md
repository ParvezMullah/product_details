# product_details

This project was generated via [manage-fastapi](https://ycd.github.io/manage-fastapi/)! :tada:

## License

This project is licensed under the terms of the Apache license.
# product_details

#Steps to Run project
1. Run Application
    ```
    docker-compose up 
    ```

2. Run unittests
    ```
    docker-compose run app pytest
    ```

3. Create Database
    ```
    #Ignore if you get any error in the below command.
    docker-compose run app alembic revision --autogenerate -m "Added initial table"

    docker-compose run app alembic upgrade head
    ``` 

4. Scrape Product Details
    ```
    docker-compose run app python product_scraper/main.py https://www.urparts.com/index.cfm/page/catalogue
    ```


5. Additional Info:
    1.  To login into the database
        ``` 
        docker exec -it product_details_db_1  psql -h localhost -U postgres -d product_db
        ```
    2. Reference for search keys
        ```
        SELECT 
            prod.id,
            manu.name AS manufacturer,
            cat.name AS category,
            model.name AS model,
            part_category.name AS part_category,
            prod.part_number
        FROM
            product AS prod
                JOIN
            category AS cat ON cat.id = prod.category_id
                JOIN
            model ON model.id = prod.model_id
                JOIN
            manufacturer AS manu ON manu.id = prod.manufacturer_id
                JOIN
            part_category ON part_category.id = prod.part_category_id
        ORDER BY prod.id DESC
        LIMIT 20;
        ```

6.  To use API - Swagger
http://localhost:8000/docs


#To Do
1. We can use Queue base approach and have multiple workers consuming the queue.
2. We can know more about required fields in the search api
and based on that we can make indexes.
3. We can add upserts for bulk create or update.
4. Add more unit tests.