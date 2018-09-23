#!/usr/bin/env python
#
# is click really better than argparse?
#
import click
import boto3
import terraform


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))


@cli.command()
def sync():
    click.echo('Synching')


@cli.command()
def clone():
    click.echo('Cloning')


@cli.command()
def s3ls():
    # Let's use Amazon S3
    try:
        s3 = boto3.resource('s3')
    except e:
        print e

    for bucket in s3.buckets.all():
        print(bucket.name)

    dynamodb = boto3.client('dynamodb')
    response = dynamodb.list_tables()
    print(response)
    print(response['TableNames'])


@cli.command()
def render():
    terraform.render_remote_state()
