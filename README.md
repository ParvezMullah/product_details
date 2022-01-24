# product_details

This project was generated via [manage-fastapi](https://ycd.github.io/manage-fastapi/)! :tada:

## License

This project is licensed under the terms of the Apache license.
# product_details

#Steps to Run project
1. Create Database
    1. docker-compose run app alembic revision --autogenerate -m "Added initial table"

    2. docker-compose run app alembic upgrade head

2. Scrape Product Details
    1. docker-compose run app python product_scraper/main.py https://www.urparts.com/index.cfm/page/catalogue

3. Run Application and Database
    1. docker-compose up 

4. Additional Info:
    1.  To login into the database
        1. docker exec -it product_details_db_1  psql -h localhost -U postgres -d product_db
        2. Reference for search
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

5.  To use API - Swagger
http://localhost:8000/docs