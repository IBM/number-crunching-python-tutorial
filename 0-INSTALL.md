# Installing developer tools and environments

## Setting up IBM Cloud environment

1. Log into [IBM Cloud](https://cloud.ibm.com/).
    * *Note*: If you do not have an account, [Create an IBM Cloud account](https://cloud.ibm.com/registration) using your IBM email address.
1. Click **Create resource** in the top right.
1. Under **Containers**, choose **Kubernetes Service**.
1. Click **Create** in the next page.
1. In the **Create new cluster** page, pick the **default** Resource Group, **Dallas** as Location, **Free** as Cluster Type.
1. Name your cluster as **`username`-cluster** and click **Create Cluster**.
1. In the **Overview** tab, watch as your cluster is deployed. It may take _several minutes_...
1. Once it reaches **Normal** status, click the three vertical dots icon on the top right corner and choose **Update version**.
1. Choose the latest version from the menu, in case your cluster is not up-to-date already, and click **Update**. It may take _several tens of minutes_...
1. Once the **Kubernetes version** reflects the update as completed, go to the **Worker Nodes** tab, click all the checkboxes and then **Update Kubernetes**.

## Setting up GitHub Enterprise environment

1. Log into [IBM GitHub Enterprise](https://github.ibm.com/).
1. Update your [profile page](https://github.ibm.com/settings/profile).
1. Install a Git client
    * macOS: Download [GitHub Desktop Client](https://desktop.github.com) or `brew cask install github`.
    * Windows: Download [GitHub Desktop Client](https://desktop.github.com).
    * Fedora: `sudo dnf install git`.
1. (macOS and Windows): Follow the [instructions](https://help.github.com/desktop/guides/getting-started-with-github-desktop/authenticating-to-github/) and setup GitHub Desktop to use <https://github.ibm.com> as GitHub Enterprise server.
    * *Note to Windows users*: In case Firefox cannot handle the operation, copy and paste the URL into a different browser.
1. Define your Git identification credentials according to your [profile page](https://github.ibm.com/settings/profile).
    * macOS and Windows: Under **Preferences / Options**, go to the **Git** tab and fill in your **Name** and **Email** address.
    * Fedora: Open a terminal and enter
        ```Shell
        git config --global user.name "Your Name"
        git config --global user.email "username@br.ibm.com"
        ```
1. (macOS) Click the **GitHub Desktop** menu and select **Install Command Line Tool...**.

## Installing IBM Cloud CLI

1. Go to the [IBM Cloud CLI download page](https://cloud.ibm.com/docs/cli/reference/ibmcloud/download_cli.html#shell_install).
1. Choose the install command according to your operational system and follow the instructions.
    * *Note to macOS users*: You can also do `brew cask install ibm-cloud-cli`.
    * *Note to Windows users*: A reboot may be required after installing IBM Cloud CLI.
1. Install IBM Cloud CLI plugins.
    * IBM Cloud Developer Tools: `ibmcloud plugin install dev`.
    * IBM Cloud Container Service: `ibmcloud plugin install container-service`.
    * IBM Cloud Container Registry: `ibmcloud plugin install container-registry`.
1. In a terminal window, enter `ibmcloud --version` to check the installation.
1. In a terminal window, enter `ibmcloud plugin list` to check the plugins.

## Installing Docker Community Edition

1. Go to the Docker Store and follow the instructions according to your operational system
    * Fedora: [Get Docker CE for Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/).
    * Windows: [Install Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/install/).
    * macOS: [Install Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/install/) or `brew cask install docker`.
1. (Windows) [Virtualisation](https://docs.docker.com/docker-for-windows/troubleshoot/#virtualization-must-be-enabled) must be enabled in the BIOS. Go to **Security**, then **Virtualization** and enable both.
1. In a terminal window, enter `docker --version` to check the installation.

## Installing Kubernetes client

1. Go to the [Install and Set Up `kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/) page.
    * *Note to macOS users*: You can also do `brew install kubernetes-cli`.
    * *Note to Fedora users*: You can also do `sudo dnf install kubernetes`.
    * *Note to Windows users*: To add the folder containing [`kubectl.exe`](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-using-curl) to the system `PATH`, follow these [command-line](https://www.windows-commandline.com/set-path-command-line/) or [graphical interface](http://www.itprotoday.com/management-mobility/how-can-i-add-new-folder-my-system-path) instructions.
1. Follow the instructions appropriate to your operational system.
1. In a terminal window, enter `kubectl version` to check the installation.

## Installing Visual Studio Code

1. Go to [Visual Studio Code download page](https://code.visualstudio.com/Download).
1. Choose the installer according to your operational system and follow the instructions.
    * *Note to macOS users*: You can also do `brew cask install visual-studio-code`.
    * *Note to Fedora users*: You can find detailed instructions [here](https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions).
1. Open VS Code and install extensions
    * Python: [click "Install"](https://marketplace.visualstudio.com/items?itemName=ms-python.python) or hit `Ctrl + P` and enter `ext install ms-python.python`.
    * IBM Developer Tools: [click "Install"](https://marketplace.visualstudio.com/items?itemName=IBM.ibm-developer) or hit `Ctrl + P` and enter `ext install IBM.ibm-developer`.
    * Output Colorizer: [click "Install"](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer) or hit `Ctrl + P` and enter `ext install IBM.output-colorizer`.
    * Docker: [click "Install"](https://marketplace.visualstudio.com/items?itemName=PeterJausovec.vscode-docker) or hit `Ctrl + P` and enter `ext install PeterJausovec.vscode-docker`.
    * Kubernetes: [click "Install"](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools) or hit `Ctrl + P` and enter `ext install ms-kubernetes-tools.vscode-kubernetes-tools`.
