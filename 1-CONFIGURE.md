# Configuring DevOps tools

## Creating a Python Starter Application

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Click **Create resource**.
1. Under **Boilerplates**, choose **Python Flask**.
1. Name it **`username`-python-app**, leaving everything else untouched and click **Create**.

## Creating GitHub Enterprise repository

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-app** application under **CloudFoundry Apps**.
1. In the bottom right of the **Overview** tab, click **Enable** for the Continuous Delivery feature.
1. In the bottom of the page, copy the contents of **Source Repository URL** and click **Create**.
1. Delete **Git** and **Eclipse Orion Web IDE** by clicking the three vertical dots in the top right corner of their cards.
1. On the top right, click **Add a Tool** and choose **GitHub Enterprise Whitewater** from the menu.
1. Authorise access from IBM Cloud to your GitHub Enterprise account and check **"I understand"**.
1. Under **Repository type**, choose **Clone** from the menu.
1. Paste the URL you copied to **Source Repository URL**.
1. Choose your own username as **Owner** and name the repository as **`username`-python-app**.
1. Check the **Enable GitHub Issues** and **Track deployment of code changes** boxes.
1. Click **Create Integration**.

## Configuring Continuous Delivery Pipeline

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-app** application under **CloudFoundry Apps**.
1. In the bottom right of the **Overview** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. In the next screen, click the gear icon in the **Build Stage** card and then **Configure Stage**.
1. In the **Input** tab, choose the option in **Git repository** that leads to GHE as **Git URL**.
1. Save your work and run this stage by clicking the **"Play"** icon.