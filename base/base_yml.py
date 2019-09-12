import yaml


def yml_data_with_file(file_name, key):

    with open("data/" + file_name + ".yml", 'r', encoding='UTF-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        data = data[key]

        case_data_list = []
        for case_data in data.values():
            case_data_list.append(case_data)

        return case_data_list
