provider "local" {
  version = "~> 2.1"
}
resource "local_file" "example" {
  content  = "hello"
  filename = "${path.module}/hello.txt"
}
