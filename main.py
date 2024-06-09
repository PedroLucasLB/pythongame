from random import randint

lista_npcs = []

def criar_npc():
    level = randint(0, 50)

    if level <= 10:
        categoria = "filhote"
    elif level <= 30:
        categoria = "Jovem"
    elif level <= 49:
        categoria = "Adulto"
    else:
        categoria = "Campeão"   

    novo_npc = {
        "nome": f"Monstro #{categoria}",
        "level": level,
        "dano": 12 * level,
        "hp": 100 * level,
    }

    lista_npcs.append(novo_npc)

def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        criar_npc()

def exibe_npcs():
    for npc in lista_npcs:
        print(
            f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']}"
        )

gerar_npcs(10)

