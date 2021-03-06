from operator import itemgetter

class Mus:

    def __init__(self, id, name, long, orch_id):
        self.id = id
        self.name = name
        self.long = long
        self.orch_id = orch_id

class Orch:

    def __init__(self, id, instr):
        self.id = id
        self.instr = instr

class MusOrch:

    def __init__(self, orch_id, mus_id):
        self.mus_id = mus_id
        self.orch_id = orch_id

orch = [
    Orch(1, 'Piano'),
    Orch(2, 'Flute'),
    Orch(3, 'Violin'),

    Orch(11, 'Piano other'),
    Orch(22, 'Flute other'),
    Orch(33, 'Violin other'),

]

mus = [
    Mus(1, 'Moonlight Sonata', 60, 1),
    Mus(2, 'Swan Lack', 10, 2),
    Mus(3, 'Turkish March ', 3, 3),

]

mus_orch = [
    MusOrch(1, 1),
    MusOrch(2, 2),
    MusOrch(3, 3),
    MusOrch(1, 2),
    MusOrch(2, 3),

    MusOrch(11, 1),
    MusOrch(22, 2),
    MusOrch(33, 3),
    MusOrch(11, 3),

]

def main():

    one_to_many = [(m.name, m.long, o.instr)
                   for o in orch
                   for m in mus
                   if m.orch_id == o.id]

    many_to_many_temp = [(o.instr, mo.orch_id, mo.mus_id)
                         for o in orch
                         for mo in mus_orch
                         if o.id == mo.orch_id]

    many_to_many = [(m.name, m.long, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for m in mus if m.id == emp_id]

    print('A1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nA2')
    res_12_unsorted = []

    for o in orch:

        o_mus = list(filter(lambda i: i[2] == o.instr, one_to_many))

        if len(o_mus) > 0:

            o_long = [long for _, long, _ in o_mus]

            o_long_sum = sum(o_long)
            res_12_unsorted.append((o.instr, o_long_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nA3')
    res_13 = {}

    for o in orch:
        if 'Flute' in o.instr:
            o_mus = list(filter(lambda i: i[2] == o.instr, many_to_many))

            o_mus_instr = [x for x, _, _ in o_mus]

            res_13[o.instr] = o_mus_instr

    print(res_13)

if __name__ == '__main__':
    main()

