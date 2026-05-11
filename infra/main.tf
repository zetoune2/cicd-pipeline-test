terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "app" {
  name = "ghcr.io/zetoune2/cicd-pipeline-test:latest"
  pull_triggers = [timestamp()]
}

resource "docker_container" "app" {
  name  = "cicd-demo-app"
  image = docker_image.app.image_id

  ports {
    internal = 8000
    external = 8080
  }
}
