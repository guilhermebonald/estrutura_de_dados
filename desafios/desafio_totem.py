""" 
A universidade ABDC está em pleno processo de matrícula dos alunos, a qual é feita presencialmente,
em uma sala em que há dois totens que imprimem as senhas para atendimento. Cada totem fica de um 
lado da sala, onde dois alunos esperam sentados até que sua vez seja chamada.

O atendente da universidade identificou um problema no sistema de senhas, o qual apesar de ser 
centralizado, senhas repetidas estavam sendo emitidas, o que causava transtorno, pois assim dois
alunos chegavam ao balcão de atendimento ao mesmo tempo. O sistema de senhas é novo, e está na 
primeira semana de testes em produção.

A equipe de desenvolvimento do sistema, da qual você faz parte, identificou que duas filas estavam 
sendo criadas para o mesmo fim, uma para cada totem, por isso a confusão, já que senhas iguais eram 
geradas para ambas as filas. A tarefa de resolver o problema dos números gerados em duplicidade ficou 
sob sua responsabilidade.
Assim, você precisa desenvolver um código em Python que exiba apenas os números gerados em duplicidade 
em ambas as filas. Como seria o código desenvolvido?
"""

def verifica_duplicidade(fila1: list, fila2: list) -> list:
    duplicados = list(set(fila1) & set(fila2))
    return duplicados


fila1 = [1, 4, 6, 9]
fila2 = [4, 2, 9, 8]

print(f"Duplicados: {verifica_duplicidade(fila1, fila2)}")