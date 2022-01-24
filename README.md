# product_details

This project was generated via [manage-fastapi](https://ycd.github.io/manage-fastapi/)! :tada:

## License

This project is licensed under the terms of the Apache license.
# product_details

#Steps to Run project
#Create Database
docker-compose run app alembic revision --autogenerate -m "Added initial table"
docker-compose run app alembic upgrade head
#Run Project