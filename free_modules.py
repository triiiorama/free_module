import string


def load_all_symbols():
    """Загрузка всех допустимых символов"""
    liters_eng = list(string.ascii_letters)
    nums = list(string.digits)
    liters_rus = ["Б", "Г", "Д", "Ж", "З", "И", "Й", "Л", "П", "У","Ф", "Ц",
                  "Ч",  "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", "б", "в",
                  "г", "д", "ж", "з", "и", "й", "к", "л", "м", "н", "п",
                  "т", "ф", "ц", "ч", "ш", "щ", "ъ", "ь", "э", "ю", "я",]

    special_symbols = ["$", "`", "~", "!", "@", "#", "№", "%", "^", "&", "(",")",
                       "_", "-", "+", "=", "{", "}", "[", "]", ";", "'", ",", "."]

    all_simple_symbols = set(liters_eng + nums + liters_rus)
    all_special_symbols = set(special_symbols)
    return all_simple_symbols, all_special_symbols


def get_free_modules(module):
    """Получить строку уникальных модулей"""
    try:
        # path_structure = r"D:\PyProjects\get_free_modules\fish\true_structure_sed.dat"
        path_structure = r"D:\PyProjects\get_free_modules\fish\false_structure_sed.dat"
        all_simple_symbols = load_all_symbols()[0]
        all_special_symbols = load_all_symbols()[1]


        with open(path_structure, "r") as structure_dat:
            structure_dat = structure_dat.read().strip().split("\n")
        
        structure = []
        for line in structure_dat:
            if module in line:
                structure.append(line)

        if structure:
            use_simple_symbols = []
            use_special_symbols = []
            for i in structure:
                for symbol in all_simple_symbols:
                    if f"{module}${symbol}" in i:
                        use_simple_symbols.append(symbol)
                for symbol in all_special_symbols:
                    if f"{module}${symbol}" in i:
                        use_special_symbols.append(symbol)


            use_simple_symbols = set(use_simple_symbols)
            use_special_symbols = set(use_special_symbols)

            uniq_simple_symbols = list(all_simple_symbols - use_simple_symbols)
            uniq_special_symbols = list(all_special_symbols - use_special_symbols)
            uniq_simple_symbols = sorted(uniq_simple_symbols, key=lambda c: (c.capitalize(), c))
            uniq_special_symbols = sorted(uniq_special_symbols)
            all_uniq_symbols = uniq_simple_symbols + uniq_special_symbols
            all_uniq_symbols = ' '.join(all_uniq_symbols)
            return all_uniq_symbols
        else:
            return f"Объект с модулем {module} не существует"
    except:
        return """Ошибка: Файл со структурой недосягаем.
        Возможно сервер недоступен,
        либо отсутствует файл -
        structure_sed.dat в корне каталога."""
