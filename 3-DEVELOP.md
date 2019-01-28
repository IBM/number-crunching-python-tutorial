# Developing a number-crunching application

## Generating a Swagger API documentation

1. Open the **`username`-python-microservice** repository in Visual Studio Code.
1. Install the latest [**Flask-RESTPlus**](https://flask-restplus.readthedocs.io) by
    * Adding `flask-restplus` to the bottom of `requirements.txt`.
    * Adding `flask-restplus = "*"` to the bottom of `Pipfile`.
1. Open the `server/__init__.py` file, perform the following modifications and save your work.
    * Add `from flask_restplus import Api` to the `import` list at the top of the file.
    * Add the following line below the definition of the `app` object in line 6.
        ```Python
        api = Api(app, title='My first Python API', version='1.0', doc='/apidocs/', description='A number-crunching API')
        ```
1. Create a new `double.py` file in `server/routes/` with the code shown below.
    ```Python
    from server import api
    from flask import jsonify
    from flask_restplus import Resource

    @api.route('/double/<int:number>')
    @api.doc(params={'number': 'Number to be doubled.'}, description='This method doubles the input.')
    class DoubleNumber(Resource):
        def get(self, number):
            return jsonify(result=2 * number)
    ```
1. Commit your changes to the `requirements.txt`, `Pipfile`, `server/__init__.py` and `double.py` files.
1. Sync your commits with the GitHub Enterprise repository.
1. Track the deployment progress in the **Continuous Delivery Pipeline**.

## Exploring the Swagger API documentation

1. Go to <http://username-python-microservice.mybluemix.net/apidocs/>.
1. Observe how the header in the top reflects the line recently added to `server/__init__.py`.
1. Click on the **Default namespace** and the `/double/{number}` endpoint.
1. Observe how the blue card reflects the `@api.route()` code block (lines 6-10) added to `double.py`.
1. Try to guess from the documentation the **purpose** and **data input format** of this method.
1. Click **Try it out**, enter an input in the text box and hit **Execute**.
1. Try several values for the `required` field and observe the response.
    * A string: `word`
    * A symbol: `+`
    * A floating point number: `1.5`
    * An integer number: `42`
1. Go to <http://username-python-microservice.mybluemix.net/double/42> and observe the response.

## Creating number-crunching functions

1. Open the **`username`-python-microservice** repository in Visual Studio Code.
1. Open the `requirements.txt` file, perform the modifications below and save your work.
    * Add `matplotlib` to install the latest [Matplotlib](https://matplotlib.org).
    * Add `numpy` to install the latest [NumPy](http://www.numpy.org)
    ```Python
    flask
    flask-restplus
    matplotlib
    numpy
    ```
1. Press the **New Folder** icon and the new folder `src`.
1. While inside `src/`, click the **New File** icon and name the new file `functions.py`.
1. Start `function.py` by importing the Python modules you have just added to `requirements.txt`.
    ```Python
    from matplotlib import pyplot as plt
    import numpy as np
    ```
1. Implement a function that converts a string with comma-separated integer values to a Python list of integers.
    * *Hint*: copy `csv_to_list()` from [lines 5-22 in `app/functions.py`](app/functions.py#L5-L22).
1. Implement a function that converts a list of integer values to an integer NumPy array.
    * *Hint*: copy `list_to_array()` from [lines 25-41 in `app/functions.py`](app/functions.py#L25-L41).
1. Implement a function that calculates the mean of a list of integer values.
    * *Hint*: copy `calculate_mean()` from [lines 44-61 in `app/functions.py`](app/functions.py#L44-L61).
1. Implement a function that plots the histogram of a list of integer values.
    * *Hint*: copy `plot_histogram()` from [lines 64-85 in `app/functions.py`](app/functions.py#L64-L85).
1. In the end, your file should look like [`app/functions.py`](app/functions.py).

## Configuring Python deployment environment

1. Open the **`username`-python-microservice** repository in Visual Studio Code.
1. Create a new file in the main repository directory named `runtime.txt` by clicking the **New File** button.
1. Check the latest Python buildpack version [available at IBM Cloud](https://console.bluemix.net/docs/runtimes/python/index.html).
1. Add `python-X.Y.Z` to `runtime.txt` reflecting the latest version `X.Y.Z` available.
    * *Example*: `python-3.6.2`
1. Open the `src/` folder, click the **New File** icon and name the new file `__init__.py`.
    * *Note*: there are two underscores (`_`) on each side of the word `init`.
1. Add the following content to `__init__.py` for defining the backend to `agg`.
    ```Python
    import matplotlib
    matplotlib.use('agg')
    ```

## Linking number-crunching functions to API methods

1. Open the **`username`-python-microservice** repository in Visual Studio Code.
1. Open `welcome.py` and remove the `@api.route('/double/<int:number>')` code block in lines 10-14.
1. Add `from src import functions` to the import list at the top of the file.
1. Add below `my_list = list()` to create an empty Python list.
1. Create an API method that **prints** the content of the list.
    * *Hint*: copy [lines 14-18 in `app/number-welcome.py`](app/number-welcome.py#L14-L18).
1. Create an API method that **resets** the content of the list.
    * *Hint*: copy [lines 21-26 in `app/number-welcome.py`](app/number-welcome.py#L21-L26).
1. Create an API method that **reverses** the content of the list.
    * *Hint*: copy [lines 29-34 in `app/number-welcome.py`](app/number-welcome.py#L29-L34).
1. Create an API method that **sorts** the content of the list.
    * *Hint*: copy [lines 37-42 in `app/number-welcome.py`](app/number-welcome.py#L37-L42).
1. Create an API method that **extends** the content of the list.
    * *Hint*: copy [lines 45-51 in `app/number-welcome.py`](app/number-welcome.py#L45-L51).
1. Create an API method that **replaces** the content of the list.
    * *Hint*: copy [lines 54-61 in `app/number-welcome.py`](app/number-welcome.py#L54-L61).
1. Create an API method that **calculates the mean** of the content of the list.
    * *Hint*: copy [lines 64-69 in `app/number-welcome.py`](app/number-welcome.py#L64-L69).
1. Create an API method that **plots the histogram** of the content of the list.
    * *Hint*: copy [lines 72-77 in `app/number-welcome.py`](app/number-welcome.py#L72-L77).
1. Place your mouse cursor on `csv_to_list()`, `calculate_mean()` and `plot_histogram()` and observe the response.
1. In the end, your file should look like [`app/number-welcome.py`](app/number-welcome.py).