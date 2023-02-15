module "vpc" {
  source            = "./modules/vpc"
  vpc_name          = "main-vpc"
  subnet_name       = "main-us-central1"
  subnet_name_proxy = "main-us-central1-proxy"
  cidr_range        = "10.0.0.0/20"
  cidr_range_proxy  = "10.100.0.0/20"
  cidr_pods         = "172.16.0.0/16"
  cidr_services     = "172.17.0.0/16"
  gcp_region        = var.gcp_region
}
