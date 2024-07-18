def notas(*notes, situation=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notes: uma ou mais notas dos alunos (aceita várias).
    :param situation: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    student = {"total": len(notes),
               "maior": max(notes),
               "menor": min(notes),
               "média": sum(notes) / len(notes)}

    if situation:
        if student["média"] >= 7:
            status = "BOA"
        elif student["média"] >= 5:
            status = "RAZOÁVEL"
        else:
            status = "RUIM"

        student["situação"] = status

    return student


response = notas(5.5, 1.5, 10, 6.5, situation=True)
print(response)
help(notas)
