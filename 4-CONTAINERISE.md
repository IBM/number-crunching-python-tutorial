# Containerising the Python application

## Setting up a private registry namespace

1. Open the **`username`-python-microservice** repository in Visual Studio Code.
1. Open the **Command Palette** and enter `bx login --sso`.
1. Click the **One Time Code** link and copy your new passcode into the terminal. Hit **Enter**.
1. Select your personal account, if necessary, following the on-screen instructions.
1. In the terminal enter `bx cr namespace-add username`, replacing `username` accordingly.
1. Verify with `bx cr namespaces`.

## Creating a platform API key

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. On the top right corner, click **Manage** then **Security** and **Platform API Keys**.
1. Click the **Create** button in the center of the screen.
1. Name it **Kubernetes**, describe it as **IBM Cloud Kubernetes API Key** and click **Create**.
1. In the next screen, click **Download** to keep a local copy of the API key.

## Building a container with Continuous Delivery Pipeline

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-microservice** application under **Apps**.
1. In the bottom right of the **Overview** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. In the next screen, click the gear icon in the **Build Stage** card and then **Configure Stage**.
1. Under **Builder type**, choose **Container Registry**.
1. Under **API key**, choose **Add an existing API key** from the menu.
1. Open the `apiKey.json` file you downloaded before and copy the `apiKey` field.
1. Paste the API key into the text box and click **Save**.
1. The name of the API key should automatically appear.
1. Under **Container Registry namespace**, input your `username` as previously defined.
1. Leave everything else untouched and **Save** your changes.

## Deploying a container with Continuous Delivery Pipeline

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-microservice** application under **Apps**.
1. In the bottom right of the **Overview** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. In the next screen, click the gear icon in the **Deploy Stage** card and then **Configure Stage**.
1. Under **Deployer type**, choose **Kubernetes**.
1. The name of the API key and the Kubernetes cluster should appear automatically.
1. Leave everything else untouched and **Save** your changes.

## Creating a `Dockerfile`

1. Open the **`username`-python-microservice** repository in Visual Studio Code.
1. Create a **New File** in the main repository directory named `Dockerfile` with the following content
    ```Dockerfile
    FROM python:3-slim
    EXPOSE 5000
    WORKDIR /usr/src/app
    COPY . .
    RUN pip install --no-cache-dir -r requirements.txt
    CMD [ "python", "welcome.py" ]
    ```
1. Save your work, commit and push your changes.

## Accessing the containerised application

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-microservice** application under **Apps**.
1. In the bottom right of the **Overview** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. Track the progress of your latest commit from the **Build Stage** to the **Deploy Stage**.
1. Click the **View logs and history** link in the **Deploy Stage** card.
1. After a successful deploy, at the very bottom of the page, you will find a link like <http://IP_ADRESS:PORT>.
1. Click the link and add `/apidocs/` to the URL in order to open the Swagger API documentation.