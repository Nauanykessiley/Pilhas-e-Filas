class Pilha:
   def __init__(self):
       self.itens = []   # cria a lista vazia para a pilha

   def push(self, nome):  # adicionar (empilhar)
       self.itens.append(nome)

   def pop(self):  # remover (desempilhar)
       if not self.vazia():
           return self.itens.pop()
       return None

   def mostrar(self):
       print("Pilha:", self.itens)

   def vazia(self):
       return len(self.itens) == 0


# Exemplo de uso
p = Pilha()
p.push("João")
p.push("Caio")
p.push("Luana")
p.mostrar()

print("Removido:", p.pop())  # remove o último
p.mostrar()


class Fila:
   def __init__(self):
       self.itens = []   # cria a lista vazia para a fila

   def push(self, nome):  # adicionar no fim da fila
       self.itens.append(nome)

   def pop(self):  # remover o primeiro da fila
       if not self.vazia():
           return self.itens.pop(0)  # tira o da frente
       return None

   def mostrar(self):
       print("Fila:", self.itens)

   def vazia(self):
       return len(self.itens) == 0


# Exemplo de uso
f = Fila()
f.enqueue("João")
f.enqueue("Caio")
f.enqueue("Luana")
f.mostrar()

print("Removido:", f.dequeue())  # remove o primeiro
f.mostrar()







