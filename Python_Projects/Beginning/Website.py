my_variable = '''
    <html>
        <head>
            <title>Look at this</title>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
'''

my_html_file = open("/Python_Projects/Blank", "w")

my_html_file.write(my_variable)

my_html_file.close()

