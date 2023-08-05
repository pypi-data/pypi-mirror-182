# ECS Foo Example Package

This is a simple example package for the ECS Foo members to enjoy.

## How to upload the project in the PyPackage Index

We need to build the distribution files. To do so we use build. To make sure that we have the latest version:

```bash
pip install -U build
```

Then, we just go inside the package folder and run:

```bash
python -m build
```

It will create a new folder called dist.

To upload these files to the **Python Package Index** we first need to have an account.

That can be done in: **https://pypi.org/account/register/**

After we have an account, will use the tool **twine** to upload our package.
We can install it also from **pip**:

```bash
pip install twine
```

And then run: 

```bash
twine upload dist/*
```

Completely different.