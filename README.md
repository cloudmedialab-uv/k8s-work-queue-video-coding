# k8s-work-queue-video-coding

This project deploys a distributed video encoding infrastructure capable of utilizing both GPU-supported and CPU-only clusters. Depending on the available resources, the deployment can be optimized for hardware with GPU capabilities or solely rely on CPU power.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Infrastructure](#running-the-infrastructure)
- [Testing](#testing)
- [Full Example](#full-example)
- [Citing](#citing)

## Prerequisites

Before deploying the infrastructure, ensure that you meet the following prerequisites:

- **Kubernetes**: You need a Kubernetes cluster ready for deployment. Ensure that your Kubernetes is at least version 1.21, as this is required to support newer APIs and stability improvements. [Install Kubernetes](https://kubernetes.io/docs/setup/).
- **Nvidia Operator**: For GPU encoding, ensure that your Kubernetes cluster is equipped with an operational Nvidia GPU operator. This operator simplifies the management of GPU resources in your Kubernetes cluster. Make sure you have at least version 1.8 of the Nvidia GPU operator installed. [Install Nvidia GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/getting-started.html).
- **Python**: The deployment scripts and test scripts require Python. Ensure that you have Python 3.8 or newer installed, as it includes improvements and features necessary for modern applications. [Install Python](https://www.python.org/downloads/).

It is recommended to verify the compatibility of your system and the required software before proceeding with the installation and deployment of the infrastructure.


## Installation

1. **Clone the repository**:

```
git clone git@github.com:cloudmedialab-uv/k8s-work-queue-video-coding.git
cd k8s-work-queue-video-coding
```

2. **Install Python dependencies**:
Ensure Python and necessary libraries are installed by running:

```
pip install -r test/requirements.txt
```

## Running the Infrastructure

Depending on your cluster's capabilities (GPU or CPU), apply the appropriate Kubernetes YAML files:

- **For GPU-supported clusters**:

```
kubectl apply -f /deploy/gpu/infrastructure.yaml
```

- **For CPU-only clusters**

```
kubectl apply -f /deploy/cpu/infrastructure.yaml
```

## Testing

After deploying the appropriate infrastructure, proceed with the following steps:

1. **Obtain the Kubernetes cluster IP**:
 Update the IP address in the testing scripts to point to your cluster.
 
2. **Run the test scripts**:
 - For GPU:
   ```
   python /test/gpu.py <kubernetes_cluster_ip>
   ```
 - For CPU:
   ```
   python /test/cpu.py <kubernetes_cluster_ip>
   ```

3. **Verify the output**:
 Check the upload container within the infrastructure to ensure that the video has been encoded and uploaded successfully.


## Full Example

This section provides a complete example of setting up and running the CPU-only video encoding infrastructure using Minikube.

### Prerequisites for this Example

Before proceeding with the example, ensure you have the following tools installed and configured:

- **Minikube**: Used to create a local Kubernetes cluster. [Install Minikube](https://minikube.sigs.k8s.io/docs/start/).
- **kubectl**: A command-line tool for interacting with Kubernetes clusters. [Install kubectl](https://kubernetes.io/docs/tasks/tools/).
- **Python**: Required to run the test scripts. Make sure Python is installed along with pip to handle package installations. [Install Python](https://www.python.org/downloads/).

1. **Start Minikube**:
This command starts your Minikube environment.
```
minikube start
```
2. **Deploy the infrastructure**:
Apply the CPU infrastructure YAML to set up the environment.
```
kubectl apply -f deploy/cpu/infrastructure.yaml
```
3. **Install Python dependencies**:
Install the required Python libraries needed for the test script.
```
pip install -r test/requirements.txt
```
4. **Run the test script**:
Execute the Python test script using the IP address of your Minikube cluster.
```
python3 test/cpu.py $(minikube ip)
```
5. **Access the upload container**:
Connect to the upload container where the encoded video is stored.
```
kubectl exec -it deployment/upload-deployment --namespace cpu-video-coding -- /bin/sh
```
6. **Check the output**:
Once inside the container, navigate to the upload directory and list the contents to verify the output.

```
cd upload
ls
```
--- Expected Output ---
```
out.mp4 times.json
```

This walkthrough guides you through starting the environment, running the encoding process, and verifying the results in the upload directory.



## Citing

If you use this infrastructure in your research or commercial project, please consider citing it:

```bib
@article{Moina2023-vqmtk,
authors={Wilmer Moina-Rivera and Juan Gutiérrez-Aguado and Miguel Garcia-Pineda},
journal={SoftwareX},
title={Video Quality Metrics Toolkit: An Open Source Software to Assess Video Quality},
volume = {23},
pages = {101427},
year = {2023},
issn = {2352-7110},
doi={10.1016/j.softx.2023.101427},
url={https://doi.org/10.1016/j.softx.2023.101427}
}
```