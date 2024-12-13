from datetime import datetime
import csv
import time

class Ponomoro:

    def __init__(self, materia, topico, tempo_estudo):
        self.materia = materia
        self.topico = topico
        self.tempo_estudo = tempo_estudo

    def start(self):
        self.hora_inicio = datetime.now()
        print(f"{self.hora_inicio} -> Iniciando Pomodoro: {self.topico} ({self.materia})")

    def end(self):
        self.hora_fim = datetime.now()
        tempo_gasto = self.hora_fim - self.hora_inicio
        print(f"Tempo gasto em {self.topico} ({self.materia}): {tempo_gasto}")

        # Salvar dados em um arquivo CSV
        with open('pomodoros.csv', 'a', newline='') as csvfile:
            fieldnames = ['materia', 'topico', 'tempo_inicio', 'tempo_fim', 'tempo_gasto']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'materia': self.materia,
                             'topico': self.topico,
                             'tempo_inicio': self.hora_inicio,
                             'tempo_fim': self.hora_fim,
                             'tempo_gasto': tempo_gasto})

estudo = Ponomoro('Português', 'Verbos', 2)
estudo.start()
time.sleep(5)
estudo.end()
