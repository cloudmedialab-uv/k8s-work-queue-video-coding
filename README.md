# k8s-work-queue-video-coding

This project deploys a distributed video encoding infrastructure capable of utilizing both GPU-supported and CPU-only clusters. Depending on the available resources, the deployment can be optimized for hardware with GPU capabilities or solely rely on CPU power.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Infrastructure](#running-the-infrastructure)
- [Testing](#testing)
- [Citing](#citing)

## Prerequisites

Before deploying the infrastructure, ensure that you have a Kubernetes cluster ready. For GPU encoding, the cluster must be equipped with an operational Nvidia operator.

## Installation

1. **Clone the repository**:

```
git clone git@github.com:cloudmedialab-uv/k8s-work-queue-video-coding.git
cd k8s-work-queue-video-coding
```

2. **Install Python dependencies**:
Ensure Python and necessary libraries are installed by running:

```
pip install -r ./test/requirements.txt
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


## Full example

```
minikube start
kubectl apply -f deploy/cpu/infraestructure.yaml
pip install -r test/requirements.txt
python3 test/cpu.py $(minikube ip)
kubectl exec -it deployment/upload-deployment --namespace cpu-video-coding -- /bin/sh
cd upload
ls
--- expected output ---
out.mp4     times.json
```

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