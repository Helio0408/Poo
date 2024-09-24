class ArvBin:
    def __init__(self, len):
        self.tam = 0
        self.max = len
        self.arr = [None] * len
        self.aux = [None] * len
        self.fb = [0] * len

    def find(self, v):
        for i in range(self.max):
            if self.arr[i] is not None:
                if v == self.arr[i]:
                    return True
        return False

    def insert(self, value):
        pos = 0
        if self.find(value):
            return

        while self.arr[pos] is not None:
            if value < self.arr[pos]:
                pos = pos * 2 + 1
            else:
                pos = pos * 2 + 2

        self.arr[pos] = value
        self.tam += 1

    def __len__(self):
        return self.tam

    def remove(self, v):
        pos = -1

        for i in range(self.max):
            if self.get_node(i) is not None and v == self.get_node(i):
                pos = i
                break

        return self.remove_ind(pos)

    def remove_ind(self, pos):
        filhos = 0
        flag = 0
        sub = [None] * self.max

        if pos < 0:
            return False

        if pos * 2 + 1 > self.max:
            self.set_node(pos, None)
            self.tam -= 1
            return True

        if self.get_node(pos * 2 + 1) is not None:
            filhos += 1
            flag = pos * 2 + 1
        if self.get_node(pos * 2 + 2) is not None:
            filhos += 1
            flag = pos * 2 + 2

        if filhos == 0:
            self.set_node(pos, None)
            self.tam -= 1
            return True
        elif filhos == 1:
            self.rem_sub_arv(flag, 0)
            self.arr[pos] = None
            sub[:self.max] = self.aux[:self.max]
            self.add_sub_arv(pos, 0, sub)
            self.tam -= 1
            return True
        elif filhos == 2:
            menor = pos
            mode = 0

            if self.count_nodes(self.node_left(pos)) <= self.count_nodes(self.node_right(pos)):
                menor = self.node_left(pos)
                mode = 2
            else:
                menor = self.node_right(pos)
                mode = 1

            while self.get_node(menor * 2 + mode) is not None:
                menor = menor * 2 + mode

            self.set_node(pos, self.get_node(menor))
            self.remove_ind(menor)
            return True

        return False

    def __str__(self):
        str_repr = ["digraph {\n"]
        cont = 0

        if self.tam == 0:
            str_repr.append("}\n\n")
            return "".join(str_repr)

        if self.tam == 1:
            str_repr.append(f"\"0 {self.arr[0]}\" ")
            str_repr.append("}\n\n")
            return "".join(str_repr)

        for i in range(self.max):
            if self.arr[i] is not None:
                if 2 * i + 1 < self.max and self.arr[2 * i + 1] is not None:
                    cont += 1
                    str_repr.append(f"\"{i} {self.arr[i]}\" ->\"{2 * i + 1} {self.arr[2 * i + 1]}\"\n")
                if 2 * i + 2 < self.max and self.arr[2 * i + 2] is not None:
                    cont += 1
                    str_repr.append(f"\"{i} {self.arr[i]}\" ->\"{2 * i + 2} {self.arr[2 * i + 2]}\"\n")

        str_repr.append("}\n\n")

        return "".join(str_repr)

    def count_nodes(self, i):
        if self.arr[i] is None:
            return 0

        return 1 + self.count_nodes(2 * i + 1) + self.count_nodes(2 * i + 2)

    def get_node(self, i):
        return self.arr[i]

    def node_left(self, i):
        if 2 * i + 1 < self.max and 2 * i + 1 > 0:
            return 2 * i + 1
        else:
            return -1

    def node_right(self, i):
        if 2 * i + 2 < self.max and 2 * i + 2 > 0:
            return 2 * i + 2
        else:
            return -1

    def set_node(self, i, v):
        self.arr[i] = v

    def rem_sub_arv(self, raiz, cont):
        if cont == 0:
            for i in range(self.max):
                if self.aux[i] is not None:
                    self.aux[i] = None
                else:
                    break

        if raiz < 0:
            return cont

        if self.get_node(raiz) is None or raiz == -1:
            return cont

        self.aux[cont] = self.get_node(raiz)
        self.set_node(raiz, None)
        cont += 1
        self.tam -= 1

        cont = self.rem_sub_arv(self.node_left(raiz), cont)
        cont = self.rem_sub_arv(self.node_right(raiz), cont)

        return cont

    def add_sub_arv(self, raiz, cont, array):
        pos = raiz

        if cont >= len(array) or array[cont] is None or raiz == -1:
            return

        self.set_node(pos, array[cont])
        array[cont] = None
        cont += 1
        self.tam += 1

        while cont < len(array) and array[cont] is not None:
            while self.get_node(pos) is not None:
                if array[cont] < self.get_node(pos):
                    pos = self.node_left(pos)
                else:
                    pos = self.node_right(pos)

            self.set_node(pos, array[cont])
            array[cont] = None
            cont += 1
            self.tam += 1

            pos = raiz


def main():
    arv1 = ArvBin(500)

    while True:
        try:
            linha = input().strip()
            p = linha.split(" ")

            if p[0] == "i":
                arv1.insert(p[1])
            elif p[0] == "d":
                arv1.remove(p[1])

        except EOFError:
            break

    print(arv1)


if __name__ == "__main__":
    main()
