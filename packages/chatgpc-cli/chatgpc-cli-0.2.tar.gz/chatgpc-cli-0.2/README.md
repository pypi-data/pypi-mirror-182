# chatgpc-cli
ChatGPC Natural language Command Line Interface

## Example Use Cases

```
$ git log pretty
>>> Run:  git log --pretty=format:"%h %ad | %s%d [%an]" [y/N]: y
$ git log --pretty=format:"%h %ad | %s%d [%an]"

$ set kubernetes namespace
>>> Run:  kubectl config set-context default --namespace=kube-system [y/N] y
$ kubectl config set-context default --namespace=kube-system

$ exec into the docker image called foobar
>>> Run:  docker exec -it foobar bash [y/N]: y
$ docker exec -it foobar bash
```

## Background
Simple cli wrapper for OpenAI's ChatGPC which was created from the Natural Language shell tutorial  https://openai.com/blog/openai-api/