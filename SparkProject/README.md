# This is guidance of SparkProject from Ren-Hau Chuang.

 Please unzip all files under spark directory
 Please put movielens files ml-20m and ml-latest-small  both under spark directory 

When type the path, please be careful if the path is right.

※ When you want to open the csv file, please do not use excel. 


Instead, use text editors such as sublime text or Notepad in case of unpredictable errors.

# To execute the programs, please ensure assignments' documents: ml-20m, ml-latest-small and files:

RenHau_Chuang_task1.py ,RenHau_Chuang_task2.py are under spark directory.

## Execution instruction:

## For MovieAvgRating.py

1.  to retrieve big file:
bin/spark-submit MovieAvgRating.py ml-20m/ratings.csv > result_task1_big.csv

2.  to retrieve small file:
bin/spark-submit MovieAvgRating.py ml-latest-small/ratings.csv > result_task1_small.csv

## For averageratings_eachtag.py

1.  to retrieve big file
bin/spark-submit averageratings_eachtag.py ml-20m/ratings.csv ml-20m/tags.csv result_task2_big.csv

2.  to retrieve small file:
bin/spark-submit averageratings_eachtag.py ml-latest-small/ratings.csv ml-latest-small/tags.csv result_task2_small.csv
