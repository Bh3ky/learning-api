# Chapter 5 Cont.


## Adding Details to the OAS info Object

    - the OAS info field contains information about the entire API.

Example Code

```python
# FastAPI constructor with additional details added for OpenAPI Specification. 
app = FastAPI(
    description=api_description,
    title="Sports World Central (SWC) Fantasy Football API",
    version="0.1",
) 
```
    - `api_description` variable with a description of the API. the api_description is then passed to the application constructor. 
    - app title and version are also included.


## Adding Tags to Categorize Your Paths

    - tags are general-purpose attributes that are used for a variety of purposes. 
    - also we add information about individual endpoints contained in the `paths` field. 
        1. Summary
            - summarizes the path and will be displayed on the operation title by Swagger UI.

        2. Description
            - gives additional details about the path and will be displayed below the title by Swagger UI.

        3. Description to the 200 response
            - replaces the default "Successful response" with a clearer description. Note: used when the HTTP 200 successful message occurs. 
        
        4. Modify the operationID
            - this standardises the operationID value which will be used by a variety of tools that are using the OAS file. 