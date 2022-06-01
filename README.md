[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# delete-module

The delete-module for [Fybrik](https://github.com/fybrik/fybrik) allows to delete objects in s3.
Currently deleting empty buckets is not supported.

## Register as a Fybrik module

To register delete-module as a Fybrik module apply `module.yaml` to the fybrik-system namespace of your cluster.

To install the latest release run:

```bash
kubectl apply -f -n fybrik-system https://raw.githubusercontent.com/fybrik/delete-module/main/module.yaml
```

### Version compatibility matrix

| Fybrik           | delete-module     | Command
| ---              | ---     | ---
| master           | master  | `https://raw.githubusercontent.com/fybrik/delete-module/main/module.yaml`

