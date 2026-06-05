
I am refactoring an existing Python script that handles scientific polymer crystallinity calculations. 
Please decouple the analytical logic from the rest of the application and place it into an isolated module at core/polymer_logic.py to serve as pure business logic. 
Then, wrap this logic inside a modern, high-performance web service layer using the FastAPI framework in app.py. 
The application should expose a POST endpoint at /calculate that parses input via a structured Pydantic model and handles validation errors gracefully.
