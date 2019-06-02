from q86 import generate_vector
from utils import load_matrix_obj, load_term_list
from q87 import cos_sim

matrix = load_matrix_obj()
term = load_term_list()

spain = generate_vector("Spain")
madrid = generate_vector("Madrid")
athens = generate_vector("Athens")
comp = spain - madrid + athens

value = []
for t in term:
    vec = generate_vector(t)
    cos_similarity = cos_sim(comp, vec)
    value.append((t, cos_similarity))

value = sorted(value, key=lambda x: x[1], reverse=True)
for i in value[0:11]:
    print(i)

"""
('Spain', 0.9093913155724523)
('Sweden', 0.8754266459902352)
('Austria', 0.8475392752861137)
('Italy', 0.8168008359486456)
('Netherlands', 0.8136732284398145)
('Télévisions', 0.8065533918664556)
('France', 0.7963059019825142)
('Norway', 0.795113925728944)
('Belgium', 0.790554362024707)
('Denmark', 0.7861447876367613)
('Vichy', 0.7853153999807845)
"""