import re


text_file = open("source.txt")

text_lines = text_file.readlines()

for line in text_lines:
    txt_regex = re.findall("^var(.*)", line)
    print(txt_regex)

    # <span class="red">var paysage</span>
