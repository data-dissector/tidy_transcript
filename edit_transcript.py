# import re

filename = 'transcript.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
    contents = contents.lower().replace("\n", " ")

print(contents)

filename = 'tidy_transcript.txt'
with open(filename, 'w') as f:
    f.write(contents)

## remove timestamps
# def remove_pattern(text, pattern):
#     r = re.findall(pattern, text)
#     for i in r:
#         text = re.sub(i, "", text)
#     return text
#
# tidy_contents = remove_pattern(contents, "[0-5][0-9]:[0-5][0-9] ")
# tidy_contents
#
# filename = 'tidy_transcript.txt'
# with open(filename, 'w') as f:
#     f.write(tidy_contents)
