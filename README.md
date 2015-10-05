Eazy Duz It
===========
### "Boy you should've known by now, Eazy duz it." --Eazy E
Eazy Duz It aims to streamline and simplify the code contribution cycle by allowing you to concentrate more of your time on coding while minimizing the time necessary to contribute changes to the repo.  It does this by standardizing the PR templates, to ensure best practices and consistency amongst our varied repos.

## Dependencies 
This tool requires the following sub-tools:
* hub (https://hub.github.com/)

```sh
    brew install hub
```

* pbcopy/pbpaste
* a Github account

## Usage
```sh
# Navigate to a git repo
cd some/git/repo
# Ensure hub is installed (>= 2.2.0)
hub --version 
# Ensure hub can log in (this causes hub to generate a log-in token)
hub browse
```

## Examples
### Pull-requests
This example will automatically create a pull-request, add the PR template and pre-fill out version, README.MD information.

```sh
# On a feature branch, generate a pull-request with a simple title.
./easy-duz-it.py -pr -t "CORE-267: Adds support for protocol buffers"
```

### Release Tags
This example will generate a pre-release for you automatically
```sh
# After you've successfully merged your topic branch, switch to master and run the following
./easy-duz-it.py -pr -t "fixing spelling."
```
