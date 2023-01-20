resource "aws_cloudwatch_event_rule" "evnet_rule" {
  name                = local.project_name
  schedule_expression = "cron(20 0 * * ? *)"
}


resource "aws_cloudwatch_event_target" "event_target" {
  rule      = aws_cloudwatch_event_rule.evnet_rule.name
  target_id = local.project_name

  input = <<DOC
{
}
DOC
  arn   = aws_lambda_function.lambda.arn
}


resource "aws_lambda_permission" "event_permission" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.evnet_rule.arn

}

resource "aws_cloudwatch_log_group" "log_group" {
  name              = "/aws/lambda/${aws_lambda_function.lambda.function_name}"
  retention_in_days = 7
}
