
def reflected_xss(user_input):
    print(f"<html><body>Hello {user_input}</body></html>")

reflected_xss("<script>alert('XSS!')</script>")
