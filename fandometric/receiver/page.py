page = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Authentication successful</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <h1>Authentication successful</h1>
  <p>You can now close this browser window. Do not share these keys without first <a href="https://www.tumblr.com/settings/apps">revoking Fandometric’s access</a> to your account.</p>
  <table>
    <tr>
      <td>Your access token</td>
      <td class="code">{oauth_token}</td>
    </tr>
    <tr>
      <td>Your access token secret</td>
      <td class="code">{oauth_token_secret}</td>
    </tr>
  </table>

  <ul class="navigation">
    <li><a href="https://www.tumblr.com/settings/apps">Fuck I changed my mind</a></li>
    <li><a href="https://github.com/kelvin13/fandometric">Github</a></li>
    <li><a href="https://github.com/kelvin13/fandometric/blob/master/readme.md">User guide</a></li>
  </ul>
  
</body>

</html>"""