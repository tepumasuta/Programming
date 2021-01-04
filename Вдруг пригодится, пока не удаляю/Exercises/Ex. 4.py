def dict_fusion_with_adding_intersects(*args):
    output_dict = {}

    for d in args:
        keys = d.keys()
        tmp_dict = {}

        #  Если вдруг у разных словарей есть один ключ и по нему доступны разные значения
        #  то по этому ключу будет доступен кортеж всех значений
        for key in keys:
            if key in output_dict.keys():
                #  Скорее всего это костыль, но я и не сеньор, чтобы писать божественный код.
                #  Здесь я значения, доступные по ключу из возвращаемого словаря и из добавляемого сливаю
                #  в один список. И потом этот список, уже как кортеж, пихаю в словарь для пересёкшихся значений

                tmp_list = []
                if type(output_dict.get(key)) == list or \
                        type(output_dict.get(key)) == tuple:
                    tmp_list.extend(output_dict.get(key))
                else:
                    tmp_list.append(output_dict.get(key))
                tmp_list.append(d.get(key))

                tmp_dict.setdefault(key, tuple(tmp_list))

        output_dict.update(d)
        output_dict.update(tmp_dict)

    return output_dict


#  Дебаг
print(dict_fusion_with_adding_intersects({"one": 1, "two": 2, "three": 3}, {'four': 4, 'five': 5, 'six': 6}),
      dict_fusion_with_adding_intersects({"one": 1, "two": 2, "three": 3}),
      dict_fusion_with_adding_intersects(),
      dict_fusion_with_adding_intersects({"one": 1, "two": 2, "three": 3}, {'one': 'один',
                                                                            'five': "пять", 'six': "шесть"}),
      dict_fusion_with_adding_intersects({'one': 1}, {'one': 'один'}, {'one': 'uno'}), sep="\n")
