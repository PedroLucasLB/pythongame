from random import randint

lista_npcs = []

player = {
    "nome": "top",
    "level": 1,
    "exp": 0,
    "exp_max": 20,
    "hp_max": 100,
    "hp" : 100,
    "dano": 20,
} 

def criar_npc(level):
    # level = randint(0, 50)

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
        "hp_max": 100 * level,
        "exp": 7 * level
    }

    return novo_npc

def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        lista_npcs.append(npc)

def exibe_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)

def exibir_npc(npc):
    print(
            f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']} "
        )
    
def exibir_player():
    print(
            f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']} "
        )

def reset_player():
    player['hp'] = player['hp_max']

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] *= 2
        player['dano'] *=2
        player['hp'] *=2
        player['hp_max'] *=2

def iniciar_batalha(npc):
    while player["hp"] > 0 and npc['hp'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        hp_sempre_zero(npc)
        exibir_info_batalha(npc)
    
    if player["hp"] > 0:
        print(f"O {player['nome']} venceu e ganhou {npc['exp']} de EXP")
        player["exp"] += npc['exp']
        exibir_player()
    else:
        print(f"O {npc['nome']} ganhou!!!")
        exibir_npc(npc)

    level_up()

    reset_player()
    reset_npc(npc)

def atacar_npc(npc):
    npc['hp'] -= player ["dano"]

def atacar_player(npc):
    player['hp'] -= npc["dano"]

def exibir_info_batalha(npc):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['nome']}: {npc['hp']}/{npc['hp_max']}")
    print('--------------------------------\n')

def hp_sempre_zero(npc):
    if player["hp"] < 0:
        player["hp"] = 0
    if npc['hp'] < 0:
        npc['hp'] = 0


gerar_npcs(5)

npc_selecionado = lista_npcs[0]

iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)

