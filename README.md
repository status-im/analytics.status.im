# Description

Application for displaying Status.im Analytics built using Hexo.

# Usage

* `yarn run build` - Build the application artifacts and output to `public` folder.
* `yarn run deploy` - Deploy to the `gh-pages` branch in the repo using Node.js script.

# Continuous Integration

Configured via the [`Jenkinsfile`](/Jenkinsfile) and a build job is executed on every push to `master` branch here:
https://ci.status.im/job/website/job/analytics.status.im/
