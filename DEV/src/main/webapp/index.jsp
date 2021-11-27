<html>
 <head>
  <title>Registration form</title>
</head>
<body>
<h2>Jenkins CI/CD pipeline for java web app</h2>
 <h2>Registration form</h2>
 <form>
  <label for="username">Username:</label>
  <input type="text" name="username" id="username" />
  <label for="password">Password:</label>
  <input type="password" name="password" id="password" />
  <input type="radio" name="gender" value="male" />Male<br />
  <input type="radio" name="gender" value="female" />Female<br />
  <input type="radio" name="gender" value="other" />Other
  <input list="Options" />
  <datalist id="Options">
    <option value="Option1"></option>
    <option value="Option2"></option>
    <option value="Option3"></option>
  </datalist>
<input type="submit" value="Submit" />
</form>
<h2><a href="login.jsp">Login</a></h2>
  
  </body>
</html>
