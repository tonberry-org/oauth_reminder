data "aws_ssm_parameter" "newrelic_account_id" {
  name = "/newrelic/account_id"
}
