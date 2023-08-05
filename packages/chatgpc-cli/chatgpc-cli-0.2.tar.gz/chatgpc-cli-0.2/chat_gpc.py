#!/usr/bin/env python3

import click, os, openai

@click.command()
@click.argument('input', nargs=-1)
def cli(input):
    # ChatGPC Wrapper published in https://openai.com/blog/openai-api/

    # Confirm openai key is set
    if not os.getenv('OPENAI_API_KEY'):
        config_path = "~/.zshrc" if 'zsh' in os.getenv('SHELL') else "~/.bashrc"
        click.echo('\nCreate OpenAI key at https://beta.openai.com/account/api-keys')
        click.echo(f"Copy and paste using your key `echo export OPENAI_API_KEY=XXXXXX >> {config_path}` \n")
        return

    prompt = """Input: List files
    Output: ls -la

    Input: Count files in a directory
    Output: ls -la | wc -l

    Input: Disk space used by home directory
    Output: du ~

    Input: Replace foo with bar in all .py files
    Output: sed -i .bak -- 's/foo/bar/g' *.py

    Input: Delete the models subdirectory
    Ouptut: rm -rf ./models"""

    template = """

    Input: {}
    Output:"""

    prompt += template.format(" ".join(input))

    result = openai.Completion.create(
        model='davinci',
        prompt=prompt,
        stop="\n",
        max_tokens=100,
        temperature=0.0
    )
    command = result.choices[0]['text']

    if click.confirm(f">>> Run: {click.style(command, 'red')}", default=False):
        os.system(command)

if __name__ == '__main__':
    cli()