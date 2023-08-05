`sealedsecret`: A tool to manage [SealedSecrets](https://github.com/bitnami-labs/sealed-secrets)

## Installation

`pipx install sealedsecretmgr`

## Usage

To list existing SealedSecrets with keys in your namespace

```
$ sealedsecret list
my-super-secret
	DATABASE_PASSWORD
```

You can pass an optional `--namespace` argument.


To retrieve and view a SealedSecret you can get it.

```
sealedsecret get secret-name
```

To create a new SealedSecret:
```
sealedsecret create new-secret-name my-key my-value-to-protect
```

To add a key or edit an existing key in an exitsing SealedSecret:
```
sealedsecret update existing-secret-name my-new-key a-value
```

The update and create commands only print the resource, you can redirect the output of edit an update to a file and then apply it using `kubectl apply -f` or you can pipe directly to `kubectl apply -`
