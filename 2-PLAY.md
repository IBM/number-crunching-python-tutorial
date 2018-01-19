# Playing with your Python application

## Cloning the repository

1. Go to [IBM GitHub Enterprise](https://github.ibm.com/).
1. Login using your IBM credentials.
1. Choose **`username`-python-app** from the **Your repositories** menu on the right.
1. Click the green button **Clone or download** and copy the address starting with `git@github.ibm.com`.
1. Open **Visual Studio Code** and summon the **Command Palette** with
    * `Ctrl + Shift + P` in [Fedora](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
    * `Ctrl + Shift + P` in [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
    * `Cmd + Shift + P` in [macOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
1. Type `clone` and select **Git: Clone** from the list.
1. Paste the `git@github.ibm.com` address you copied before and provide the destination as required.
1. Open the newly cloned repository.

## Testing the example implementation

1. Open the **`username`-python-app** repository in Visual Studio Code.
1. Open the `welcome.py` file.
1. Read the `@app.route('/')` code block in lines 20-22.
1. Go to <http://username-python-app.mybluemix.net/> and observe the response.
1. Read the `@app.route('/myapp')` code block in lines 24-26.
1. Go to <http://username-python-app.mybluemix.net/myapp> and observe the response.
1. Read the `@app.route('/api/people')` code block in lines 28-34.
1. Go to <http://username-python-app.mybluemix.net/api/people> and observe the response.
1. Read the `@app.route('/api/people/<name>')` code block in lines 36-41.
1. Go to <http://username-python-app.mybluemix.net/api/people/World> and observe the response.
1. Go to <http://username-python-app.mybluemix.net/api/people/DouglasAdams> and observe the response.

## Customizing the example implementation

1. Open the **`username`-python-app** repository in Visual Studio Code.
1. Open the `welcome.py` file.
1. Anywhere between lines 19 and 42, add the following code block and save the modifications.
    ```Python
    @app.route('/answer/')
    def AnswerToLifeTheUniverseAndEverything():
        content = 'The Answer to Life the Universe and Everything = 42'
        return jsonify(message=content)
    ```
1. Open the **Source Control** panel in the left corner.
1. Click the `+` icon next to `welcome.py` to **Stage Changes**.
1. Write a meaningful commit message, such as `Created '/answer/' endpoint` and click the `√` icon.
1. On the bottom left corner, click the arrows to **Synchronize Changes**.
1. Track the deployment progress in the **Continuous Delivery Pipeline**.
1. Go to <http://username-python-app.mybluemix.net/answer/> and observe the response.

## Customizing the example implementation again

1. Open the **`username`-python-app** repository in Visual Studio Code.
1. Open the `welcome.py` file.
1. Add the following code block to `welcome.py` and save the modifications.
    ```Python
    @app.route('/check/answer/<number>')
    def CheckAnswerToLifeTheUniverseAndEverything(number):
        content = {
            'statement': 'The Answer to Life the Universe and Everything is ' + number + '.',
            'check': 'The statement is ' + str(number == '42') + '!'
        }
        return jsonify(message=content)
    ```
1. Open the **Source Control** panel in the left corner.
1. Click the `+` icon next to `welcome.py` to **Stage Changes**.
1. Write a meaningful commit message, such as `Created '/check/answer/<number>' endpoint` and click the `√` icon.
1. On the bottom left corner, click the arrows to **Synchronize Changes**.
1. Track the deployment progress in the **Continuous Delivery Pipeline**.
1. Go to <http://username-python-app.mybluemix.net/check/answer/24> and observe the response.
1. Go to <http://username-python-app.mybluemix.net/check/answer/42> and observe the response.
