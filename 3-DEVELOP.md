# Developing a number-crunching application

## Generating a Swagger API documentation

1. Open the **`username`-python-app** in a Visual Studio Code window.
1. Open the `requirements.txt`, perform the  modifications below and save your work.
    * Replace `Flask==0.10.1` by `flask==0.12.2` to update [Flask](http://flask.pocoo.org)
    * Add `flask-restplus==0.10.1` to install [Flask-RESTPlus](http://flask-restplus.readthedocs.io)
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
1. Jump two blank lines and add the following code block
    ```Python
    @api.route('/double/<int:number>')
    @api.doc(params={'number': 'Number to be doubled.'}, description='This method doubles the input.')
    class DoubleNumber(Resource):
        def get(self, number):
            return jsonify(result=2 * number)
    ```
1. In the end, your file should look like [app/swagger-welcome.py](app/swagger-welcome.py).