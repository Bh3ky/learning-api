# Developing the FastAPI Code

- In this chapter the focus is on building code to create a working API.


## FastAPI
- Python web framework that is designed for building APIs.
    - web framework = set of libraries that simplify common tasks for web applications. Other common web frameworks include Express, Flask, Django, and Ruby on Rails.
- FastAPI helps in simplifying several tasks such as handling HTTP traffic, requests/responses, and etc. It also automatically generates an OpenAPI specification file for the API (useful for integrating with other products). 


## HTTPX
- is a Python HTTP client which supports asynchronous calls. 

## Pydantic
- is a data validation library which is very effective and efficient.
- FastAPI uses Pydantic to generate JSON schema representations from Python code. 
    - JSON schema is a standard that ensures consistency in JSON data structures. 


## Uvicorn
- uvicorn is based on ASGI specification which provides support for both synchronous processes (which block the process while waiting for a tasks to be performed) and asychronous processes (which can allow another process to continue while they are waiting). 



# Creating Pydantic Schemas

- Pydantic classes define the structue of the data that the consumer will receive in their API responses. It uses a software design pattern called data transfer objects (DTO).
- in DTO, we define a format for transferring data between a producer and a consumer without the consumer needing to know the backend format. 

- FastAPI uses Pydantic to perform the serialization process which convert Python objects into JSON for the API response. 
- Pydantic takes the data from SQLAlchemy classes and provide it to the API users. 


* NOTE:  the schemas in the schemas.py file are used to form the responses to the API endpoints. The primary schemas are directly returned to the endpoints and the secondary schemas are returned as an attribute of the primary schema. 




# Creating FastAPI Controller

- 
