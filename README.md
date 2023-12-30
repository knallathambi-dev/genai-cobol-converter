# COBOL to Python conversion using GenAI

![Process Diagram](docs/assets/GenAI%20COBOL%20Converter.png)

## Project setup

* Create python virtual environment and activate
    ```
    > python -m venv .venv
    # windows
    > .venv\Scripts\activate.bat            
    # linux/mac 
    > source .venv/bin/activate             
    ```

* Install Python packages
    ```
    (.venv) > pip install -r requirements.txt
    ```

* Create .env file and copy contents from [.env_local](.env_local). Add OpenAI and Google API key

## Run Conversion pipeline

[playbook.yml](prompts.yml) provides GenAI provider settings and source COBOL artifacts.

Execute the below command to start the execution
```
> python -m cob2py_app.main playbook.yml
```