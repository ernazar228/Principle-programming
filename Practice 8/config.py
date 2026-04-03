from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename, encoding='utf-8')

    config = {}
    if parser.has_section(section):
        for key, value in parser.items(section):
            config[key] = value.strip()
    else:
        raise Exception(f'Section {section} not found in {filename}')

    return config