#!/usr/bin/env python
#
# is click really better than argparse?
#
import click
import common
import boto3
import sys
import terraform


class Tfw(object):

    def __init__(self, home):
        self.home = home
        self.config = {}
        self.verbose = False

    def set_config(self, key, value):
        self.config[key] = value
        if self.verbose:
            click.echo('  config[%s] = %s' % (key, value), file=sys.stderr)

    def __repr__(self):
        return '<Tfw %r>' % self.home


pass_repo = click.make_pass_decorator(Tfw)


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('--verbose', '-v', is_flag=True, help='Enables verbose mode.')
@click.version_option('1.0')
@click.pass_context
def cli(ctx, debug, verbose):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

# check that the tools we require are present
#package_check

# check that we have AWS credentials
#check_aws_credentials

#GIT_BRANCH=$(get_git_branch)
#TF_WORKSPACE=$(map_branch_to_workspace ${GIT_BRANCH})
#TF_VARS_FILE=$(map_branch_to_tfvars ${GIT_BRANCH})

# create the S3 bucket, DynamoDB & matching backend.tf
#generate_terraform_backend


@cli.command()
@pass_repo
def plan(ctx):
    # terraform plan -var-file=${TF_VARS_FILE} -out=plan/plan.out
    click.echo('terraform plan')
    print terraform.__file__
    terraform.foo()


@cli.command()
def apply():
    click.echo('terraform apply')
    # terraform apply plan/plan.out
    # terraform output
    # once more for the camera
    # terraform output -json > output.json


@cli.command()
def destroy():
    click.echo('terraform destroy')
    # terraform destroy -var-file=${TF_VARS_FILE} -auto-approve
    # terraform workspace select default
    # terraform workspace delete ${TF_WORKSPACE}


@cli.command()
def s3ls():
    # Let's use Amazon S3
    try:
        s3 = boto3.resource('s3')
    except Exception as e:
        print e

    for bucket in s3.buckets.all():
        print(bucket.name)

    dynamodb = boto3.client('dynamodb')
    response = dynamodb.list_tables()
    print(response)
    print(response['TableNames'])


@cli.command()
def amils():
    # SHA=99cf6d3b1bcb2437a5ce2c2bf2e66e9e143cbfc9
    try:
        ec2 = boto3.resource('ec2')
        ami_filter = [{'Name': 'tag:SHA', 'Values': ['x99cf6d3b1bcb2437a5ce2c2bf2e66e9e143cbfc9']}]
        images = ec2.images.filter(Filters=ami_filter)
    except Exception as e:
        print e
        exit(2)

    print images

    for ami in images:
        print(ami)
        print(ami.tags)

    if len(list(images)) > 0:
        print "Found more than 1 image with matching SHA!"
    else:
        print "No images found with SHA"


@cli.command()
def render():
    terraform.render_remote_state()


@cli.command()
def map_branch():
    branch = common.get_git_branch()
    click.echo(common.map_branch_to_workspace(branch))


if __name__ == '__main__':
    cli()
