[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# delete-module

The delete-module for [Fybrik](https://github.com/fybrik/fybrik) allows to delete objects in s3 buckets and remove empty buckets after object deletion.

## Register as a Fybrik module

To register delete-module as a Fybrik module apply `module.yaml` to the fybrik-system namespace of your cluster.

To install the latest release run:

```bash
kubectl apply -f https://github.com/Raviv-S/delete-module/blob/main/module.yaml -n fybrik-system
```

### Version compatibility matrix

| Fybrik           | AFM     | Command
| ---              | ---     | ---
| master           | master  | `https://raw.githubusercontent.com/Raviv-S/delete-module/main/module.yaml`

