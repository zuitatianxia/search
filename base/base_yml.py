import yaml
def yml_data_with_file(file_name):
    with open("./data/"+file_name+".yml", 'r') as f:
        return yaml.load(f)
#         print(type(data))  # 打印data类型
#         print(data)  # 打印data返回值
# if __name__ == '__main__':
#     yml_data_with_file()