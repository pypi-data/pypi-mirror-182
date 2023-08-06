from io import open
import os

def preprocess(dataset,file):
    model = dataset
    moedl_path = 'data/'+model

    if os.path.exists(moedl_path):
        ratings_final = open( moedl_path + '/ratings_final.txt','r',encoding='utf-8')
    else:
        os.mkdir(moedl_path)
        ratings_final = open( moedl_path + '/ratings_final.txt','w',encoding='utf-8')
        with open(file,"r") as fw:
            lines = fw.readlines()
            for line in lines:
                if line:
                    ratings_final.write(line)

    rating_file = open( moedl_path + '/rating_train.dat','w',encoding='utf-8')
    with  open (moedl_path+'/ratings_final.txt', "r") as fw:
        lines = fw.readlines()
        for line in lines:
            if line:
                user, item, rating = line.strip().split("\t")
                rating_file.write("u" + user + "\t" + "i" + item + "\t" + rating + "\n")

    rating_file = open( moedl_path + '/rating_test.dat','w',encoding='utf-8')
    with  open (moedl_path+'/ratings_final.txt', "r") as fw:
        lines = fw.readlines()[1001:10000]
        for line in lines:
            if line:
                user, item, rating = line.strip().split("\t")
                rating_file.write("u" + user + "\t" + "i" + item + "\t" + rating + "\n")