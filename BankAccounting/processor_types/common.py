import json

JSON_PATH = "data.json"


def set_category(key):
    with open(JSON_PATH, "r+") as f:
        category_data = json.load(f)
        if key in category_data["Index"]:
            sub_category = category_data["Index"][key]
            main_category = category_data["SubCategories"][sub_category]
            return sub_category, main_category
        else:
            sub_category = input(f"What is the sub category for {key}?")
            category_data["Index"][key] = sub_category
            if sub_category in category_data["SubCategories"]:
                main_category = category_data["SubCategories"][sub_category]
            else:
                is_valid_main_category = False
                while not is_valid_main_category:
                    main_category = input(f"What is the main category for {sub_category}?")
                    if main_category in category_data["MainCategories"]:
                        is_valid_main_category = True
                    else:
                        print(f"{main_category} is an invalid main category")
                category_data["SubCategories"][sub_category] = main_category
            f.seek(0)
            json.dump(category_data, f)
            f.truncate()
            return sub_category, main_category


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def get_category_key(description):
    phrases = description.split(' ')
    key = ""
    for phrase in phrases:
        if not has_numbers(phrase):
            key = " ".join([key, phrase])
    return key
