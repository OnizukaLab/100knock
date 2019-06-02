from q86 import generate_vector
from utils import load_term_list
from sklearn.metrics.pairwise import cosine_similarity


term = load_term_list()

england = generate_vector("Japan")
value = []
for t in term:
    vec = generate_vector(t)
    cos_sim = cosine_similarity(england, vec)
    value.append((t, cos_sim))

value = sorted(value, key=lambda x: x[1], reverse=True)
for i in range(11):
    print(value[i])
