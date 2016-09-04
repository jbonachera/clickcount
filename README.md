# Click Count application

[![Build Status](https://travis-ci.org/jbonachera/clickcount.svg)](https://travis-ci.org/jbonachera/clickcount)

This project is running on an instance of another project:  https://github.com/jbonachera/clickcount-infra.

# Workflow

The following workflow is used:

  * any PR or push triggers a CI run, on travis. Travis check if the application can build, and passes the tests.
  * accepting a PR on the _master_ branch triggers a CI run, a release of a new Docker image on the Docker hub (https://hub.docker.com/r/jbonachera/clickcount/), and a deployment of this image in the Staging environment, which runs on clickcount-staging.<domain>.
  * pushing a new tag will promote the image related to the tag into the Production environment, which runs on clickcount.<domain>.

# Docker tagging

The following tagging strategy is used (all the work is done by Travis CI):

  * every release is tagged with the most recent commit SHA fingerprint, and is aliased as `jbonachera/clickcount:dev`
  * tagging a commit in the git repository tags the related docker image with the same name; for instance, running `git tag -a v0.1` on the commit `beeac69...` will alias `jbonachera/clickcount:beeac69...` as `jbonachera/clickcount:v0.1`. It will also alias the `lastest` tag on it, for convenience.

So, running `jbonachera/clickcount:dev` is running the most recent release of the `master` branch, and running `jbonachera/clickcount` is running the most recent "approved" (tagged) release.
