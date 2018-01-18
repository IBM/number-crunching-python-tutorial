# IBM Cloud tutorial

A tutorial for deploying Python applications to IBM Cloud.

## Scope

This tutorial illustrates typical work-flows and tools in cloud computing, addressing key concepts
and technologies.
By the end of this tutorial everyone should be able to deploy a Python application to IBM Cloud
and have some familiarity with

* IBM Cloud
* GitHub Enterprise
* Docker containers
* Visual Studio Code
* Kubernetes containers
* Continuous Integration
* CloudFoundry applications

## Instructions

1. Read [**Preparing DevOps tools and environments**](0-PREPARE.md) and follow the steps.
    1. [Setting up IBM Cloud environment](0-PREPARE.md#setting-up-ibm-cloud-environment)
    1. [Setting up GitHub Enterprise environment](0-PREPARE.md#setting-up-github-enterprise-environment)
    1. [Installing IBM Cloud CLI](0-PREPARE.md#installing-ibm-cloud-cli)
    1. [Installing Docker Community Edition](0-PREPARE.md#installing-docker-community-edition)
    1. [Installing Kubernetes client](0-PREPARE.md#installing-kubernetes-client)
    1. [Installing Visual Studio Code](0-PREPARE.md#installing-visual-studio-code)

### Creating a Python Starter Application

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Click **Create resource**.
1. Under **Boilerplate**, choose **Python Flask**.
1. Name it **`username`-python-app**, leaving everything else untouched and click **Create**.

### Creating Git repository

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-app** application under **CloudFoundry Apps**.
1. In the bottom right of the **Overview** tab, click **Enable** for the Continuous Delivery feature.
1. In the bottom of the page, copy the contents of **Source Repository URL** and click **Create**.
1. Delete **Git** by clicking the three vertical dots in the top right corner of the card.
1. On the top right, click **Add a Tool** and choose **GitHub Enterprise Whitewater** from the menu.
1. Authorise access from IBM Cloud to your GitHub Enterprise account and check **I understand**.
1. Under **Repository type**, choose "Clone" from the menu.
1. Paste the URL you copied to **Source Repository URL**.
1. Choose your own username as **Owner** and name the repository as **`username`-python-app**.
1. Check the **Enable GitHub Issues** and **Track deployment of code changes** boxes.
1. Click **Create Integration**.

### Configuring Continuous Delivery Pipeline

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-app** application under **CloudFoundry Apps**.
1. In the bottom right of the **Overview** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. In the next screen, click the gear icon in the **Build Stage** card and then **Configure Stage**.
1. In the **Input** tab, choose the option in **Git repository** that leads to GHE as **Git URL**.
1. Save your work and run this stage by clicking the "Play" icon.