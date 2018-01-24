# Installing developer tools and environments

## Setting up IBM Cloud environment

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Click **Create resource**.
1. Under **Infrastructure**, go to **Containers** and choose **Containers in Kubernetes Clusters**.
1. Click **Create** in the next page.
1. In the **Create new cluster** page, pick **US South**, **Free / Lite plan**, name your cluster as **`username`-cluster** and click **Create Cluster** in the panel on the right.
1. In the **Overview** tab, click the three vertical dots icon on the top right corner and choose **Update version**.
1. Choose the latest version, in case your cluster is not up-to-date already, from the menu and click **Update**.

## Setting up GitHub Enterprise environment

1. Go to [IBM GitHub Enterprise](https://github.ibm.com/).
1. Login using your IBM credentials.
1. Update your [profile page](https://github.ibm.com/settings/profile).
1. Install a Git client
    * macOS: Download [GitHub Desktop Client](https://desktop.github.com) or `brew cask install github`.
    * Windows: Download [GitHub Desktop Client](https://desktop.github.com).
    * Fedora: `sudo dnf install git`.
1. Choose **Sign in to you GitHub Enterprise Server** and fill the text box with <https://github.ibm.com>.
1. Click the **Sign in with your browser** button, and **Authorize** the application in the new window.
    * *Note to Windows users*: In case Firefox cannot handle the operation, copy and paste the URL into Internet Explorer.
1. Define your Git identification credentials
    * macOS and Windows: Under **Preferences / Options**, go to the **Git** tab and fill in your **Name** and **Email** address.
    * Fedora: Open a terminal and enter
        ```Shell
        git config --global user.name "Your Name"
        git config --global user.email "username@br.ibm.com"
        ```
1. (macOS) Open GitHub Desktop and click **Install Command Line Tool...**.

## Installing IBM Cloud CLI

1. Go to the [IBM Cloud CLI download page](https://console.bluemix.net/docs/cli/reference/bluemix_cli/get_started.html).
1. Choose the installer according to your operational system and follow the instructions.
    * *Note to macOS users*: Homebrew used to have this package, but `caskroom/cask/bluemix-cli` has been outdated for months.
    * *Note to Windows users*: A reboot is required after installing IBM Cloud CLI.
1. Install IBM Cloud CLI plugins.
    * IBM Cloud Developer Tools: `bx plugin install dev -r Bluemix`.
    * IBM Cloud Container Service: `bx plugin install container-service -r Bluemix`.
    * IBM Cloud Container Registry: `bx plugin install container-registry -r Bluemix`
1. In a terminal window, enter `bx --version` to check the installation.
1. In a terminal window, enter `bx plugin list` to check the plugins.

## Installing Docker Community Edition

1. Go to the Docker Store and follow the instructions according to your operational system
    * Fedora 25, 26, 27: [Get Docker CE for Fedora](https://store.docker.com/editions/community/docker-ce-server-fedora).
    * macOS 10.10.3 or above: [Get Docker CE for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac) or `brew cask install docker`.
    * Windows 10: [Get Docker CE for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows).
    * macOS (older): [Install Docker Toolbox on macOS](https://docs.docker.com/toolbox/toolbox_install_mac/) or `brew cask install docker-toolbox`.
    * Windows (older): [Install Docker Toolbox on Windows](https://docs.docker.com/toolbox/toolbox_install_windows/).
1. Windows: Virtualisation must be enabled in the BIOS. Go to **Security**, then **Virtualization** and enable both.
1. In a terminal window, enter `docker --version` to check the installation.

## Installing Kubernetes client

1. Go to the [Install and Set Up Up `kubectl` page](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-via-curl).
    * *Note to macOS users*: You can also try `brew install kubernetes-cli`.
    * *Note to Fedora users*: You can also try `sudo dnf install kubernetes`.
    * *Note to Windows users*: To add the folder containing `kubectl.exe` to the system `PATH`, follow [this command-line](https://www.windows-commandline.com/set-path-command-line/) or [this graphical interface](http://www.itprotoday.com/management-mobility/how-can-i-add-new-folder-my-system-path) instructions.
1. Follow the instructions appropriate to your operational system.
1. In a terminal window, enter `kubectl version` to check the installation.

## Installing Visual Studio Code

1. Go to [Visual Studio Code download page](https://code.visualstudio.com/Download).
1. Choose the installer according to your operational system and follow the instructions.
    * *Note to macOS users*: You can also do `brew cask install visual-studio-code`.
1. Open VS Code and install extensions
    * Python: [click "Install"](https://marketplace.visualstudio.com/items?itemName=ms-python.python) or hit `Ctrl + P` and enter `ext install ms-python.python`.
    * IBM Developer Tools: [click "Install"](https://marketplace.visualstudio.com/items?itemName=IBM.ibm-developer) or hit `Ctrl + P` and enter `ext install IBM.ibm-developer`.
    * Output Colorizer: [click "Install"](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer) or hit `Ctrl + P` and enter `ext install IBM.output-colorizer`.
    * Docker: [click "Install"](https://marketplace.visualstudio.com/items?itemName=PeterJausovec.vscode-docker) or hit `Ctrl + P` and enter `ext install PeterJausovec.vscode-docker`.
    * Kubernetes: [click "Install"](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools) or hit `Ctrl + P` and enter `ext install ms-kubernetes-tools.vscode-kubernetes-tools`.
