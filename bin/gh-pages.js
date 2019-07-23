var ghpages = require('gh-pages')

/* use SSH auth by default */
let repoUrl = 'git@github.com:status-im/analytics.status.im.git'

/* alternative is to use github used and API token */
if (process.env.GH_USER != undefined) {
  let repoUrl = ( 
    'https://' + process.env.GH_USER + ':' + process.env.GH_TOKEN
    + '@github.com/status-im/analytics.status.im.git'
  )
}
 
ghpages.publish('public', {
  repo: repoUrl,
  branch: 'gh-pages',
  dotfiles: true,
  silent: false
}, function(err) {
  if (err !== undefined) {
    console.error(err)
    throw err
  }
})
