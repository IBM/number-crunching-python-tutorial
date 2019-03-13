# Configuring DevOps tools

## Creating a Python Starter Kit

1. Log into [IBM Cloud](https://cloud.ibm.com/).
1. Click **Create resource** in the top right corner.
1. Under **Starter Kits**, choose **Python Microservice with Flask** and click **Create app** in the next page.
1. Name it **`username`-python-microservice**, leaving everything else untouched and hit **Create**.

## Creating GitHub repository

1. Log into [IBM Cloud](https://cloud.ibm.com/).
1. Click **`username`-python-microservice** in the **Apps** panel on the left.
1. In the **App details** tab, click **Deploy to Cloud** to enable the Continuous Delivery feature.
1. In the **Choose a deployment environment** panel, pick **Deploy to Cloud Foundry** and hit **Next**.
1. In the **Configure toolchain** panel, name the toolchain as **`username`-python-microservice-cf** (where `cf` refers to "Cloud Foundry") and click **Create**.
1. Copy the Git URL in the **Deployment details** box and click the **View toolchain** button.
    * *Note*: You might need to refresh the browser window in case the Git URL does not show up.
1. Delete **Git** and **Eclipse Orion Web IDE** by clicking the three vertical dots in the top right corner of their cards.
1. On the top right, click **Add a Tool** and choose **GitHub** from the catalog.
1. Authorise access from IBM Cloud to your GitHub account by clicking the **Authorize** button.
1. Under **Repository type**, choose **Clone** from the menu.
1. Paste the URL you copied to **Source repository URL**.
1. Choose your own username as **Owner** and name the repository as **`username`-python-microservice**.
1. Make sure the **Enable GitHub Issues** and **Track deployment of code changes** boxes are checked.
1. Click **Create Integration**.

## Configuring Continuous Delivery Pipeline

1. Log into [IBM Cloud](https://cloud.ibm.com/).
1. Click **`username`-python-microservice** in the **Apps** panel on the left.
1. In the **App details** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. In the next screen, click the gear icon in the **Build Stage** card and then **Configure Stage**.
1. In the **Input** tab, choose the option in **Git repository** that leads to Github as **Git URL**.
1. Save your work and run the **Build Stage** by clicking the :arrow_forward: icon.
1. Watch as the **Build Stage** completes and triggers the **Deploy Stage** and **Health Stage**.