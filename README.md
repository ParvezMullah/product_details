# product_details

This project was generated via [manage-fastapi](https://ycd.github.io/manage-fastapi/)! :tada:

## License

This project is licensed under the terms of the Apache license.
# product_details

#Steps to Run project
# product_details#Create Database
docker-compose run app alembic revision --autogenerate -m "Added initial table"
docker-compose run app alembic upgrade head
##Scrape Product Details
docker-compose run app python product-scraper/main.py https://www.urparts.com/index.cfm/page/catalogue
#Run Application and Database
docker-compose up 

##Additional Info:
###To login into the database
docker exec -it product_details_db_1  psql -h localhost -U postgres -d product_db

#To use API - Swagger
http://localhost:8000/docs