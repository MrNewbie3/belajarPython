def create_html(tag, text,**atributes):
    html=f"<{tag}"
    
    for key, value in atributes.items():
        html = html + f" {key}='{value}'"

    html =html + f">{text}</{tag}>"
    return html


html=create_html("a", "hello ini adalah teks python menggunakan html", href="www.google.com", )
print(html)

html=create_html("p", "Hello there")
print(html)


def create(tag, text, **attributes):
    html= f"<{tag}"

    for key, value in attributes.items:
        html = html + f"{key}={value}"
        
    html = f">{text}</{tag}>"
    return html

html = create_html("a", "ini link", href="www.youtube.com", style= "link")
print(html)
html = create_html("p", "YOOOO, Sup mann")
print(html)



def cate(tag, text, **attributes):
    html=f"<{tag}"
    for key, value in attributes.items():
        html= html + f"{key}='{value}'"

    html=f">{text}</{tag}>"
    return html

html= cate("H1", "Hello World")
print(html)

html= cate("p", "Hello World")
print(html)
