# Developing a number-crunching application

## Generating a Swagger API documentation

1. Open the **`username`-python-app** repository in Visual Studio Code.
1. Open the `requirements.txt` file, perform the modifications below and save your work.
    * Replace `Flask==0.10.1` by `flask` to update [**Flask**](http://flask.pocoo.org) to its latest version
    * Add `flask-restplus` to install the latest [**Flask-RESTPlus**](https://flask-restplus.readthedocs.io)
    ```Python
    flask
    flask-restplus
    ```
1. Open the `welcome.py` file and erase all the `@app.route()` code blocks.
1. Add `from flask_restplus import Api, Resource` to the `import` list at the top of the file.
1. Add the following line just below `app = Flask(__name__)`
    ```Python
    api = Api(app, title='My first Python API', version='1.0', doc='/apidocs/',
          description='A number-crunching API')
    ```
1. Skip two blank lines, add the following code block and save your work.
    ```Python
    @api.route('/double/<int:number>')
    @api.doc(params={'number': 'Number to be doubled.'}, description='This method doubles the input.')
    class DoubleNumber(Resource):
        def get(self, number):
            return jsonify(result=2 * number)
    ```
1. In the end, your file should look like [`app/swagger-welcome.py`](app/swagger-welcome.py).
1. Commit your changes to the `requirements.txt` and `welcome.py` files.
1. Sync your commits with the GitHub Enterprise repository.
1. Track the deployment progress in the **Continuous Delivery Pipeline**.

## Exploring the Swagger API documentation

1. Go to <http://username-python-app.mybluemix.net/apidocs/>.
1. On the right hand side, click **Expand Operations**.
1. Observe how the header in the top reflects [lines 6-7 in `app/swagger-welcome.py`](app/swagger-welcome.py#L6-L7).
1. Observe how the blue card reflects [lines 10-14 in `app/swagger-welcome.py`](app/swagger-welcome.py#L10-L14).
1. Try to guess from the documentation the **purpose** and **data input format** of this method.
1. Click **Try it out!** and observe the response.
1. Try several values for the `required` field and observe the response.
    * A string: `word`
    * A symbol: `+`
    * A floating point number: `1.5`
    * An integer number: `42`
1. Go to <http://username-python-app.mybluemix.net/double/42> and observe the response.

## Creating number-crunching functions

1. Open the **`username`-python-app** repository in Visual Studio Code.
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

1. Open the **`username`-python-app** repository in Visual Studio Code.
1. Create a new file in the main repository directory named `runtime.txt` by clicking the **New File** button.
1. Check the latest Python buildpack version [available at IBM Cloud](https://console.bluemix.net/docs/runtimes/python/index.html#python_runtime).
1. Add `python-X.Y.Z` to `runtime.txt` reflecting the latest version `X.Y.Z` available.
    * *Example*: `python-3.6.2`
1. Open the `src/` folder, click the **New File** icon and name the new file `__init__.py`.
    * *Note*: there are two underscores (`_`) on each side of the word `init`.
1. Add the following content to `__init__.py` for defining the backend to `agg`.
    ```Python
    import matplotlib
    matplotlib.use('agg')
    ```