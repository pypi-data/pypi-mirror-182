# mlsteam-model-sdk
SDK for accessing MLSteam models

## Setup

```bash
pip3 install mlsteam-model-sdk
```

To process encrypted model versions, install the *Themis development package* according to the official [instrunctions](https://docs.cossacklabs.com/themis/languages/python/installation/). Debian/Ubuntu users have a handy installation method:

```bash
# for users that already have administrator privileges
mlsteam-model-cli install-themisdev

# for those that need privilege lifting
sudo mlsteam-model-cli install-themisdev
```

## Usage

A minimum example for downloading a model version:

> This example assumes the program is running in an MLSteam system.
> If it is not the case, you may need to setup *API_TOKEN* with
> `mlsteam-model-cli init --api_token=YOUR_API_TOKEN`

```python
from mlsteam_model_sdk.sdk.model import Model

sdk_model = Model()
sdk_model.download_model_version(project_name='project_owner/project_name',
                                 model_name='model_name',
                                 version_name='version_name')
```

> By default, the model version will be downloaded at `$HOME/.mlsteam-model-sdk/models/download/`.

This loads a model version and makes prediction:

```python
mv = sdk_model.load_model_version(model_name='model_name',
                                  version_name='version_name')
outputs = mv.predict(inputs)
```
