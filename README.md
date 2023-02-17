# k8s-gateway-api example

This repository is an example to use gateway api in GKE. If you want yo read more about it:

- [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/).
- [GKE Gateway API](https://cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)

In a nutshell Gateway API is an open source that was created by the [SIG-NETWORK](https://github.com/kubernetes/community/tree/master/sig-network) community. The gateway API bring some resources that interact with Kubernetes service networking through expressive, extensible, and role-oriented interfaces.

## Gateway API Structure

[![Foo](https://gateway-api.sigs.k8s.io/images/api-model.png)](https://gateway-api.sigs.k8s.io/)

## GKE Gateway API Resources

[![Foo](https://cloud.google.com/static/kubernetes-engine/images/gateway-architecture.svg)](https://cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project.

### Prerequisites

- git
- make
- python
- pip
- virtualenv
- vscode
- skaffold
- docker
- minikube
- kubectl
- kubectx
- gcloud

To deloy this project you will need a Google Cloud account, [create here](https://cloud.google.com/).

"This project will generate costs,take care."

### Deploying

First of all you need to clone this repository:

```bash
git clone https://github.com/claick-oliveira/k8s-gateway-api
```

To deploy this project we use terraform, but if you prefer you can see the commands to create the infrastrcutre in [COMMANDS](COMMANDS.md).

#### Infrastructure

First let's check the architecture that we will create.

#TODO: ## Add the architecture diagram

#### Terraform

Now that we know about the architecture and resources, let's create. First we need to connect our shell to the `gcloud`:

```bash
gcloud auth login
```

Now that we connected:

```bash
cd terraform
terraform apply
```

This project you need to fill some variables:

- **gcp_project_name**: The GCP project ID
- **gcp_region**: The GCP region
- **gcp_zone**: The GCP availability zone

### Running the service

First we need to connect in our GKE:

```bash
gcloud container clusters get-credentials <CLUSTER_NAME> --region <REGION> --project <PROJECT_ID>
```

To be easy and skaffold use the correct environment, let's configure `kubectx`:

Get the name of the environment:

```bash
kubectx
```

Now change the name for staging:

```bash
kubectx staging=<YOUR ENVIRONMENT>
```

To run the server you need to execute, but you need to be in the root folder:

```bash
skaffold run --default-repo us-central1-docker.pkg.dev/<PROJECT_ID>/example-svc
```

After this you can test the roemer service:

```bash
curl -X POST http://127.0.0.1:5000/roemer/planets/distance -H 'Content-Type: application/json' -d '{"data":["Earth"]}'
```

### Application

Access the folder and create your virtual env:

```bash
cd k8s-gateway-api
make venv
```

Now let's activate your virtual env:

```bash
make activate
```

To start to code you need to install the requirements and de dev requirements:

```bash
make requirements
make requirementsdev
```

### Running the tests

To run the tests you need to execute:

```bash
make test
```

### And coding style tests

In this project we'll use [PEP 8](https://www.python.org/dev/peps/pep-0008/) as style guide.

## Clean

To clean the files generated as coverage, builds, env you can use:

``` bash
make cleanfull
skaffold delete
```

To clean the infrastructure:

```bash
terraform destroy
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/claick-oliveira/amazonmq-api-example/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Claick Oliveira** - *Initial work* - [claick-oliveira](https://github.com/claick-oliveira)

See also the list of [contributors](https://github.com/claick-oliveira/k8s-gateway-api/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details
