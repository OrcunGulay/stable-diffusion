import pickle

with open("pipe.pkl", "rb") as file:
    loaded_pipe = pickle.load(file)

prompt = "Recep Tayyip Erdogan"
image = loaded_pipe(prompt).images[0]
image.save("sonuc.png")
