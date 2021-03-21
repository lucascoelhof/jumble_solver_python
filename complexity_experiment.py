from jumble import parse_word_list_file, jumble
import time
import matplotlib.pyplot as plt

if __name__ == "__main__":

    words = ["fun", "cars", "robot", "camera", "sentinel", "absolute", "crocodile", "abominable", "personality", "cytoskeleton", "acetylcholine",
             "ridiculousness", "procrastination", "extraterrestrial", "industrialization", "parliamentarianism", "intellectualization", "counterrevolutionist",
             "otorhinolaryngologist", "electroencephalography", "hydrochlorofluorocarbon", "laryngotracheobronchitis", "antidisestablishmentarism"]
    xaxis = range(2, len(words)+2)
    jumble_dict = parse_word_list_file("words.txt")
    time_words = []
    for word in words:
        start_time = time.time()
        jumble(jumble_dict, word)
        time_words.append(time.time() - start_time)
        print(time_words[-1])

    plt.plot(xaxis, time_words)
    plt.xlabel("Number of letters")
    plt.ylabel("Execution time (s)")
    plt.grid()
    plt.show()
