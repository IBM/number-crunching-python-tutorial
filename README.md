# IBM Cloud tutorial

A tutorial for deploying Python applications to IBM Cloud.

## Scope

This tutorial illustrates typical work-flows and tools in cloud computing, addressing key concepts
and technologies.
By the end of this tutorial everyone should be able to deploy a Python application to IBM Cloud
and have some familiarity with

1. IBM Cloud
1. GitHub Enterprise
1. Visual Studio Code
1. Docker containers
1. Kubernetes containers
1. Continuous Integration
1. CloudFoundry applications

## Prepare tools and environments

### Set up your IBM Cloud environment

1. Go to [IBM Cloud Console](https://console.bluemix.net/dashboard/apps).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Hit **Create resource**.
1. Under **Infrastructure**, go to **Containers** and choose **Containers in Kubernetes Clusters**.
1. Hit **Create** in the next page.
1. In the **Create new cluster** page, pick **US South**, **Lite plan**, name your cluster as
    **`username`-cluster** and hit **Create Cluster** in the panel on the right.
1. In the **Overview** tab, click the three vertical dots icon on the top right corner and choose **Update version**.
1. Choose the latest version from the menu and click **Update**.

### Set up your GitHub Enterprise environment

1. Go to [IBM GitHub Enterprise](http://github.ibm.com/).
1. Login using your IBM credentials.
1. Update your [profile page](https://github.ibm.com/settings/profile).
1. Install a Git client
    * macOS and Windows: Download [GitHub Desktop Client](https://desktop.github.com).
    * Fedora: `sudo dnf install git`.
1. (macOS and Windows) Open GitHub Desktop and click **Install Command Line Tool...**.
1. In a terminal window, enter `git --version` to check the installation.

### Install IBM Cloud CLI

1. Go to the [IBM Cloud CLI download page](https://console.bluemix.net/docs/cli/reference/bluemix_cli/get_started.html).
1. Choose the installer according to your operational system and follow the instructions.
1. Install IBM Cloud CLI plugins.
    * IBM Cloud Developer Tools: `bx plugin install dev -r Bluemix`.
    * IBM Cloud Container Service: `bx plugin install container-service -r Bluemix`.
    * IBM Cloud Container Registry: `bx plugin install container-registry -r Bluemix`
1. In a terminal window, enter `bx --version` to check the installation.
1. In a terminal window, enter `bx plugin list` to check the plugins.

### Install Docker Community Edition

1. Go to the Docker Store and follow the instructions according to your operational system
    * Fedora 25, 26, 27: [Get Docker CE for Fedora](https://store.docker.com/editions/community/docker-ce-server-fedora).
    * macOS 10.10.3 or above: [Get Docker CE for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac).
    * Windows 10: [Get Docker CE for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows).
    * macOS (older): [Install Docker Toolbox on macOS](https://docs.docker.com/toolbox/toolbox_install_mac/).
    * Windows (older): [Install Docker Toolbox on Windows](https://docs.docker.com/toolbox/toolbox_install_windows/).
1. In a terminal window, enter `docker --version` to check the installation.

### Install Kubernetes client

1. Go to the [Install and Set Up Up `kubectl` page](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-via-curl).
1. Follow the instructions appropriate to your operational system.
1. In a terminal window, enter `kubectl version` to check the installation.

### Install Visual Studio Code

1. Go to [Visual Studio Code download page](https://code.visualstudio.com/Download).
1. Choose the installer according to your operational system and follow the instructions.
1. Open VS Code and install extensions
    * Python: [click "Install"](https://marketplace.visualstudio.com/items?itemName=ms-python.python) or hit `Ctrl+P` and enter `ext install ms-python.python`.
    * IBM Developer Tools: [click "Install"](https://marketplace.visualstudio.com/items?itemName=IBM.ibm-developer) or hit `Ctrl+P` and enter `ext install IBM.ibm-developer`.
    * Output Colorizer: [click "Install"](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer) or hit `Ctrl+P` and enter `ext install IBM.output-colorizer`.
    * Docker: [click "Install"](https://marketplace.visualstudio.com/items?itemName=PeterJausovec.vscode-docker) or hit `Ctrl+P` and enter `ext install PeterJausovec.vscode-docker`.
    * Kubernetes: [click "Install"](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools) or hit `Ctrl+P` and enter `ext install ms-kubernetes-tools.vscode-kubernetes-tools`.