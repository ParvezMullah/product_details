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

5.  To use API - Swagger
http://localhost:8000/docs