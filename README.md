# yaml-secrets-injector
Allow to inject secrets from GHA to yaml files. As example can be used with helm to inject the secrets

This action is usefull to manage your project secrets via Github instead of external applications.

# Usage
Use this action in your workflow as in the example:

```yaml
      - name: Inject secrets to yaml files
        uses: none0nfg/yaml-secrets-injector@v0.0.1
        with:
          inject_files: |-
              path/to/file1.yaml
              path/to/file2.yaml
          secrets: ${{ toJSON(secrets) }} # It would contain all your repository secrets in json (let it be {"DEV_PASSWORD": "pass123"} for now)
```

Example of the file to inject:
```yaml
SECRETS:
  password: "{{ DEV_PASSWORD }}" # Here, DEV_PASSWORD it's a key of GHAs secret
```

Result:
```yaml
SECRETS:
  password: "pass123"
```

Action will inject matched keys to yaml files by rewriting them. 