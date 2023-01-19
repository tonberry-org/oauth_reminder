
resource "aws_dynamodb_table" "dynamodb" {
  name           = local.project_name
  hash_key       = "symbol"
  range_key      = "timestamp"
  read_capacity  = 1
  write_capacity = 1

  attribute {
    name = "symbol"
    type = "S"
  }

  attribute {
    name = "timestamp"
    type = "S"
  }

  tags = {
    Name = "Market Scheduler"
  }
}
