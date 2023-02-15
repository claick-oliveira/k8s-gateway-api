// vpc module
output "name" {
  description = "The name of the VPC"
  value       = google_compute_network.vpc.name
}
