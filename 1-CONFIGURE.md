# Configuring DevOps tools

## Creating a Python Starter Kit

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Click **Create resource**.
1. Under **Starter Kits**, choose **Python Microservice with Flask** and **Create app**.
1. Name it **`username`-python-microservice**, leaving everything else untouched and hit **Create**.

## Creating GitHub Enterprise repository

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-microservice** application under **Apps**.
1. In the **App details** tab, click **Deploy to Cloud** to enable the Continuous Delivery feature.
1. In the **Choose a deployment environment** page, pick **Deploy to Cloud Foundry** and hit **Next**.
1. In the **Configure toolchain** page, name the toolchain as **`username`-python-microservice-cf** (where `cf` refers to "Cloud Foundry") and click **Create**.
1. Copy the Git URL in the **Deployment details** box and click the **View toolchain** button.
1. Delete **Git** and **Eclipse Orion Web IDE** by clicking the three vertical dots in the top right corner of their cards.
1. On the top right, click **Add a Tool** and choose **GitHub Enterprise Whitewater** from the catalog.
1. Authorise access from IBM Cloud to your GitHub Enterprise account and check **"I understand"**.
1. Under **Repository type**, choose **Clone** from the menu.
1. Paste the URL you copied to **Source repository URL**.
1. Choose your own username as **Owner** and name the repository as **`username`-python-microservice**.
1. Make sure the **Enable GitHub Issues** and **Track deployment of code changes** boxes are checked.
1. Click **Create Integration**.

## Configuring Continuous Delivery Pipeline

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-microservice** application under **Apps**.
1. In the **App details** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. In the next screen, click the gear icon in the **Build Stage** card and then **Configure Stage**.
1. In the **Input** tab, choose the option in **Git repository** that leads to Github Enterprise as **Git URL**.
1. Save your work and run this stage by clicking the **"Play"** icon.
1. Watch as the **Build Stage** completes and triggers the **Deploy Stage** and **Health Stage**.