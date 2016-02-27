<?php
	if(isset($_POST['sendCode']))
	{
		if($_POST['promCode'] == "214")
		{

			echo "Success!";
		}else
		{
			echo "Wrong Code!";
		}
	}else if(isset($_GET['sendCode']))
	{
		if($_GET['promCode'] == "214")
		{

			echo "Success!";
		}else
		{
			echo "Wrong Code!";
		}
	}

?>
<html>
<head>
  <title>
      Hack Promotion Code
  </title>
</head>

<body>
<form action="" method="post">
  <p>Prom Code: </p>
  <input type="text" name="promCode" id="promCode" />
  <input type="submit" name="sendCode" id="sendCode" />
</form>

</body>

</html>
