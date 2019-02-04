# Containerising the Python application

## Setting up a private registry namespace

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. In the top left corner, click the three horizontal lines to open the IBM Cloud console menu.
1. Select **Kubernetes** from the menu.
1. In the **Registry** tab, click the **Namespaces** card.
1. Hit the **Create namespace** button in the right side.
1. In the **Create namespace** screen, use your **`username`** as name.
1. Click the **Create** button.

## Removing the old Cloud Foundry-based toolchain

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. In the top left corner, click the three horizontal lines to open the IBM Cloud console menu.
1. Select **DevOps** from the menu to open the [Toolchains](https://console.bluemix.net/devops/toolchains?env_id=ibm%3Ayp%3Aus-south) page.
1. Make sure your **Location** is **Dallas**.
1. Locate the **`username`-python-microservice-cf** toolchain in the list.
1. Click the three vertical dots to the right and select **Delete** to remove the old toolchain.
1. Enter the name of the toolchain in the text box to enable the **Delete** button.
1. Click the **Delete** button to remove the Cloud Foundry-based toolchain.

## Creating a new Kubernetes-based toolchain

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-microservice** application under **Apps**.
1. In the **App details** tab, click **Deploy to Cloud** to enable the Continuous Delivery feature.
1. In the **Choose a deployment environment** page, pick **Deploy to Kubernetes** and hit **Next**.
1. In the **Configure toolchain** page, name the toolchain as **`username`-python-microservice-k8s** (where `k8s` refers to "Kubernetes") and click **Create**.
1. In the **App details** tab, click **View toolchain**.
1. Delete **Git** and **Eclipse Orion Web IDE** by clicking the three vertical dots in the top right corner of their cards.
1. On the top right, click **Add a Tool** and choose **GitHub Enterprise Whitewater** from the catalog.
1. Authorise access from IBM Cloud to your GitHub Enterprise account and check **"I understand"**.
1. Under **Repository type**, choose **Link** from the menu.
1. Select the **`username`-python-microservice** repository from the **Repository URL** menu.
1. Make sure the **Enable GitHub Issues** and **Track deployment of code changes** boxes are checked.
1. Click **Create Integration**.

## Building a container with Continuous Delivery Pipeline

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-microservice** application under **Apps**.
1. In the **App details** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. In the next screen, click the gear icon in the **Build Stage** card and then **Configure Stage**.
1. In the **Input** tab, choose the option in **Git repository** that leads to Github Enterprise as **Git URL**.
1. Leave everything else untouched and **Save** your changes.

## Deploying a container with Continuous Delivery Pipeline

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-microservice** application under **Apps**.
1. In the **App details** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. In the next screen, click the gear icon in the **Deploy Stage** card and then **Configure Stage**.
1. Verify that all fields are correctly populated.
1. Leave everything else untouched and **Save** your changes.

## Customizing the `Dockerfile`

1. Open the **`username`-python-microservice** repository in Visual Studio Code.
1. Edit the `Dockerfile` and perform the following change use Python 3.
    ```Dockerfile
    FROM python:3-alpine
    ```
1. Save your work, commit and push your changes.

## Accessing the containerised application

1. Go to [IBM Cloud console](https://console.bluemix.net/).
1. Login using your IBM credentials.
1. Click the profile icon in the top right corner and make sure you are using your own account.
1. Double-click the **`username`-python-microservice** application under **Apps**.
1. In the **App details** tab, click **View toolchain**.
1. In the toolchain **Overview** tab, click the **Delivery Pipeline** card.
1. Track the progress of your latest commit from the **Build Stage** to the **Deploy Stage**.
1. Click the **View logs and history** link in the **Deploy Stage** card.
1. After a successful deploy, at the very bottom of the page, you will find a link like <http://IP_ADRESS:PORT>.
1. Click the link and add `/apidocs/` to the URL in order to open the Swagger API documentation.

## Deploying a container manually using the command-line

1. Open **Visual Studio Code** and summon the **Command Palette** with
    * `Ctrl + Shift + P` in [Fedora](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
    * `Ctrl + Shift + P` in [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
    * `Cmd + Shift + P` in [macOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
1. Type `terminal` and choose **View: Toggle Integrated Terminal**.
1. In the terminal window, issue `ibmcloud login --sso` and follow the on-screen instructions to log into IBM Cloud.
1. Execute `ibmcloud cs init`, then `ibmcloud cr login`. If the second command fails, make sure **Docker** is running locally.
1. Configure your Kubernetes cluster by executing the `export` command that is output by the following command.
    ```Shell
    $ ibmcloud cs cluster-config <username>-cluster
    ```
1. Configure your `kubectl` environment by running the command below.
    ```Shell
    $ kubectl config set-context <username>-cluster --cluster=<username>-cluster --namespace=<username>
    ```
1. Export your image registry secrets by running both commands below.
    ```Shell
    $ kubectl get secret bluemix-default-secret-regional -n default -o yaml | sed 's/default/<username>/g' | kubectl create -f -
    $ kubectl get secret bluemix-default-secret-international -n default -o yaml | sed 's/default/<username>/g' | kubectl create -f -
    ```
1. Take note of the **Repository** URL and image **Tag** number in the output of `ibmcloud cr images`.
1. Create a **Pod** based on your image and expose it with a **NodePort** service.
    ```Shell
    $ kubectl run <username>-python-microservice --image=<repository>:<tag> --restart=Never --image-pull-policy=Always --overrides='{ "apiVersion": "v1", "spec": { "imagePullSecrets": [{"name": "bluemix-<username>-secret-regional"}] } }'
    $ kubectl expose pod <username>-python-microservice --port=3000 --type=NodePort --name=<username>-python-microservice
    ```
1. Take note of the **Public IP** from the output of `ibmcloud cs workers --cluster <username>-cluster`.
1. Take note of the secondary **Port** number (after the `:`) in the output of `kubectl get all`.
1. Open a browser window and access `<http://PUBLIC_IP:PORT/apidocs/>.
