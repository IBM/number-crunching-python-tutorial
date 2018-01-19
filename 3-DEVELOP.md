# Developing a number-crunching application

## Generating a Swagger API documentation

1. Open the **`username`-python-app** repository in Visual Studio Code.
1. Open the `requirements.txt` file, perform the  modifications below and save your work.
    * Replace `Flask==0.10.1` by `flask==0.12.2` to update [**Flask**](http://flask.pocoo.org)
    * Add `flask-restplus==0.10.1` to install [**Flask-RESTPlus**](http://flask-restplus.readthedocs.io)
    ```Python
    flask==0.12.2
    flask-restplus==0.10.1
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

1. Go to <https://username-python-app.mybluemix.net/apidocs/>.
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