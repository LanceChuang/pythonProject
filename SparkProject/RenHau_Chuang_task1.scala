import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import java.io._
import org.apache.spark.mllib.recommendation.ALS
import org.apache.spark.mllib.recommendation.Rating
object Demo {
  def main(args: Array[String]) {
    val testfile = args(1)
    val datafile = args(0)


   // Load and parse the data
    val sparkConf = new SparkConf().setAppName("Ren-HauChuang").setMaster("local[*]")
    val sc = new SparkContext(sparkConf)
    val data = sc.textFile(datafile)
    val testing = sc.textFile(testfile)
    //val data = sc.textFile("src/ml-latest-small/ratings.csv")
    //val testing = sc.textFile("src/testing_small.csv")
// val data = sc.textFile("src/ml-20m/ratings.csv")
//val testing = sc.textFile("src/testing_20m.csv")
    val header = data.first()
    val header_testing = testing.first()
    val testings = testing.filter(l=>l!=header_testing).map(_.split(",").take(2)).map{case Array(userId,movieId)=>((userId,movieId),0)}
    //val actualrating = data.filter(l=>l!=header).map(_.split(",").take(3))
    val ratingdata = data.filter(l=>l!=header).map(_.split(",").take(3))
      .map{case Array(userId, movieId, rating)=>((userId,movieId),rating)}
    //val newratingData = ratingdata.subtractByKey(testings).map{case ((x,z),y)=>(x,z,y)}
    //println("---newratings---")
    //newratingData.take(10).foreach(println)
  val training = ratingdata.subtractByKey(testings).map{case ((userId,movieId),rating)=>Rating(userId.toInt, movieId.toInt, rating.toDouble)}

    // Build the recommendation model using ALS
    val rank = 6
    val numIterations = 10
    val model = ALS.train(training, rank, numIterations, 0.03)

    // Evaluate the model on testing data
    val testing_for_evaluation = testings.map{case ((userId, movieId), rating)=> Rating(userId.toInt, movieId.toInt, rating.toDouble)}
    val movieItems = testing_for_evaluation.map { case Rating(userId, movieId,rating) =>
      (userId, movieId)
    }

    val predictions =
      model.predict(movieItems).map { case Rating(userId, movieId, rating) =>
        ((userId, movieId), rating)
      }


    val Predsallvalue = predictions.map{case ((userId, movieId), rating) => ((userId.toInt,movieId.toInt),rating.toDouble)}
    val mid = testings.map{case ((userId,movieId),0)=> ((userId.toInt,movieId.toInt),0.0)}
    val missingvalue = mid.subtractByKey(Predsallvalue).map{case((x,y),z)=> (x,(y,z))}
    val tmp = training.map{case Rating(userId,movieId,rating)=> (rating)}.sum()/training.count()
    val result = missingvalue.map{case(x,(y,z))=> ((x,y),tmp)}.union(predictions).sortByKey()
    val ratesAndPreds = ratingdata.map{case ((userId,movieId),rating)=>((userId.toInt,movieId.toInt),rating.toDouble)}.join(result)
    Predsallvalue.unpersist()
    result.unpersist()
    //println("====after conducting ratesAndPreds====")
    //write predicttions into files
    val resultforprint = ratesAndPreds.sortByKey()//.map{case ((userId,movieId),(actual,predicted))=> ((userId,movieId),predicted)}
          .map{case  ((userId,movieId),(actual,predicted))=>userId+","+movieId+","+predicted}
  
if (datafile =="ml-20m/ratings.csv"){
   val pw = new PrintWriter(new File("RenHau_Chuang_result_task1_big.txt"))
      pw.write("UserId,MovieId,Pred_rating\n")
      for (x<-resultforprint.collect()){
        pw.write(x+"\n")
      }
      pw.close()
    }
    else{
      val pw = new PrintWriter(new File("RenHau_Chuang_result_task1_small.txt"))
      pw.write("UserId,MovieId,Pred_rating\n")
      for (x<-resultforprint.collect()){
        pw.write(x+"\n")
      }
      pw.close()
    }
  val pw = new PrintWriter(new File("RenHau_Chuang_result_task1_big.txt"))
    pw.write("UserId,MovieId,Pred_rating\n")
    for (x<-resultforprint.collect()){
      pw.write(x+"\n")
    }
    pw.close()

  //  println("===after printing===")
    resultforprint.unpersist()
 val difference =  ratesAndPreds.map{case ((userId,movieId),(actual,predicted))=> math.abs(actual-predicted)}
//println("===after difference===")
    val zero = difference.filter(l=>l>=0.0 && l<1.0).count()
    val one = difference.filter(l=>l>=1.0 && l<2.0).count()
    val two = difference.filter(l=>l>=2.0 && l<3.0).count()
    val three = difference.filter(l=>l>=3.0 && l<4.0).count()
    val four = difference.filter(l=>l>=4.0).count()
    println(">=0 and <1: "+zero)
    println(">=1 and <2: "+one)
    println(">=2 and <3: "+two)
    println(">=3 and <4: "+three)
    println(">=4: "+four)
   // println("total numbers:"+difference.count())
    val MSE = ratesAndPreds.map{
      case ((userId, movieId), (actual, predicted)) =>  math.pow((actual - predicted), 2)
    }.reduce(_ + _) / ratesAndPreds.count
    val RMSE = math.sqrt(MSE)
    println("RMSE = " + RMSE)


   }
}
