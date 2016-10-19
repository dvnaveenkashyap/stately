const html = require('choo/html')

module.exports = (user) => {
  return html`
    <nav class="navbar navbar-default">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Stately</a>
        </div>

        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li><a href="/cases">Cases</a></li>
            <li><a href="/travel-request">Travel request</a></li>
            <li><a href="/indebtedness">Indebtedness</a></li>
          </ul>

          ${user.email ? html`<p class="navbar-text navbar-right">Signed in as ${user.email}</p>` : ''}
        </div>
      </div>
    </nav>
  `
}
