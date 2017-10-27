#define the  html_list function
def html_list(string_list):
    print("<ul>")
    for i in string_list:
        print("<li>" + i + "</li>")
    print("</ul>")
html_list(['first string', 'second string'])
