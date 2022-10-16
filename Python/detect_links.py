'''
Exercise: Read an html file and extract all the links and write to another file. Now you can assume more than one
urls in one line.
'''
with open('file10.html', 'r') as webpage:
    with open('file11.txt', 'a') as wf:
        page = webpage.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos==-1:
                link_exist = False
            else:
                first_quote = page.find('\"', pos)
                second_quote = page.find('\"', first_quote+1)
                url = page[first_quote+1:second_quote]
                wf.write(f'{url}\n')
                page = page[second_quote:]
