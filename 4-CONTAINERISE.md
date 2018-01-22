# Containerising the Python application

## Create a platform API key

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. On the top right corner, click **Manage** then **Security** and **Platform API Keys**.
1. Click the **Create** button in the center of the screen.
1. Name it **Kubernetes**, describe it as **IBM Cloud Kubernetes API Key** and click **Create**.
1. In the next screen, click **Download** to keep a local copy of the API key.

## Add Kubernetes deployment to Continuous Delivery Pipeline

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-app** application under **CloudFoundry Apps**.
1. In the bottom right of the **Overview** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. In the next screen, click the gear icon in the **Deploy Stage** card and then **Configure Stage**.
1. Rename the **Deploy** job to **Deploy Application**.
1. Click the **Add Job** icon, choose **Deploy** and name it **Deploy Container**.
1. Under **Configuring Continuous Delivery Pipeline**, choose **Kubernetes**.
1. Under **API key**, choose **Add an existing API key** from the menu.
1. Open the `apiKey.json` file you downloaded before and copy the `apiKey` field.
1. Paste the API key into the text box and click **Save**.
1. The name of the API key and the Kubernetes cluster you created should automatically appear.