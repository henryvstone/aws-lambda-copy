resource "aws_s3_bucket" "starting_files" {
  bucket = "henryvstone-starting-files"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "ending_files" {
  bucket = "henryvstone-ending-files"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

