print("hello world")
import os, fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


file = find('*.md', '/home/tom/PycharmProjects/Polar')[0]
# print(file)

with open(file, "a") as myfile:
    myfile.write("---")

markdown_notes = open(file, 'r+')
# print(file.read())
markD_notes_list = []
for line in markdown_notes:
    stripped_line = line.strip()
    markD_notes_list.append(stripped_line)
markdown_notes.close()

index_of_dashes = []
i = 0
while i < len(markD_notes_list) - 1:
    i += 1
    if markD_notes_list[i] == '---':
        index_of_dashes.append(i)
index_of_dashes.insert(0, 0)
# print(index_of_dashes)

notes_list = []
i = 0
while i < len(index_of_dashes) - 1:
    start = index_of_dashes[i]
    end = index_of_dashes[i + 1]
    notes_list.append(markD_notes_list[start:end])
    i += 1
    # print(notes_list)

pre_formatted_notes = []
for list in notes_list:
    pre_formatted_notes.append(list[5:])
    # print(pre_formatted_notes)


def convert_to_str(input_seq, seperator):
    # Join all the strings in list
    final_str = seperator.join(input_seq)
    return final_str


notes_text = open('notes.txt', 'a')
for note in pre_formatted_notes:
    notes_text.write(convert_to_str(note, ' '))
    notes_text.write('\n')
notes_text.close()

os.remove(file)
os.system('gedit notes.txt')

notes_text = open("notes.txt", "r+")
notes_text.truncate(0)
notes_text.close()
