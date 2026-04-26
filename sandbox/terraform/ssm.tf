data "aws_caller_identity" "current" {}

resource "aws_ssm_parameter" "test_param" {
  name      = "/aft/test/account-id"
  type      = "String"
  value     = data.aws_caller_identity.current.account_id
  overwrite = true
}