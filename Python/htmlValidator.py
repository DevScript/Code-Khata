import html5lib

html5parser = html5lib.HTMLParser(strict=True)
html5parser.parse("""
<!DOCTYPE html>
<html lang="en">

</html>
""")
