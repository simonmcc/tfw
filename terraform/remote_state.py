from string import Template


def render_remote_state(filename='remote_state.tf',
                        bucket_name='abc',
                        project_name='123',
                        aws_default_region='eu-west-1'):
    template = Template("""terraform {
  backend "s3" {
    bucket         = "$bucket_name"
    key            = "$project_name"
    region         = "$aws_default_region"
    dynamodb_table = "terraform_locks"
  }
}""")

    rt = template.substitute(bucket_name=bucket_name,
                             project_name=project_name,
                             aws_default_region=aws_default_region)

    print(rt)
