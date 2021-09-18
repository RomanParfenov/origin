

def trans_file(root_folder, name_new_file):

    import os
    directory = os.listdir(root_folder)
    file_res = os.path.join(os.getcwd(), name_new_file)
    date = {}
    for i in directory:
        file_root = os.path.join(os.getcwd(), f'sorted/{i}')
        with open(file_root, 'r', encoding='utf-8') as file:
                leng = len(file.readlines())
        with open(file_root, 'r', encoding='utf-8') as file:
                string = file.read()
                date.setdefault(i, [f"{leng}", string])

    data_new = sorted(date.items(), key=lambda x: x[1])

    with open(file_res, 'w+', encoding='utf-8') as file:
        for key in data_new:
            file.write(f"{key[0]}"+"\n")
            for kin in key[1]:
             file.write(f"{kin}"+"\n")

trans_file('/Users/toshiba\PycharmProjects\pythonProject\sorted', 'sorted/res.txt')













