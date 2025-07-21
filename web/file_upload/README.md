# File Uploads

If a server configuration blocks execution of scripts in an upload directory, we can maybe bypass that by uploading our own config file.
> Apache: `.htaccess`
```

```

> ISS server: `web.config`
```
<staticContent>
    <mimeMap fileExtension=".json" mimeType="application/json" />
</staticContent>
```

<br>

# Obfuscation of extensions: (Copied from Portswigger)
1. Provide multiple extensions. Depending on the algorithm used to parse the filename, the following file may be interpreted as either a PHP file or JPG image: `exploit.php.jpg`
2. Add trailing characters. Some components will strip or ignore trailing whitespaces, dots, and suchlike: `exploit.php.`
3. Try using the URL encoding (or double URL encoding) for dots, forward slashes, and backward slashes. If the value isn't decoded when validating the file extension, but is later decoded server-side, this can also allow you to upload malicious files that would otherwise be blocked: `exploit%2Ephp`
4. Add semicolons or URL-encoded null byte characters before the file extension. If validation is written in a high-level language like PHP or Java, but the server processes the file using lower-level functions in C/C++, for example, this can cause discrepancies in what is treated as the end of the filename: `exploit.asp;.jpg` or `exploit.asp%00.jpg`
5. Try using multibyte unicode characters, which may be converted to null bytes and dots after unicode conversion or normalization. Sequences like `xC0 x2E`, `xC4 xAE` or `xC0 xAE` may be translated to x2E if the filename parsed as a UTF-8 string, but then converted to ASCII characters before being used in a path.
6. `exploit.p.phphp`

# Embed php in valid image:
`exiftool -Comment="<?php system(\$_GET['cmd']); ?>" image.jpg`