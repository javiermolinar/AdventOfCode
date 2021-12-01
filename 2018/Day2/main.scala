import scala.io.Source

object AdventOfCode {
  def main(args: Array[String]): Unit = {      
    val lines = Source.fromFile("input").getLines.toList;
    println(lines.filter(x=>x.groupBy(identity).mapValues(_.size).toSeq.exists(y => y._2 == 2)).length *
     lines.filter(x=>x.groupBy(identity).mapValues(_.size).toSeq.exists(y => y._2 == 3)).length)
  }  
}