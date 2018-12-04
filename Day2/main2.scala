import scala.io.Source

object AdventOfCode {
  def main(args: Array[String]): Unit = {      
     val lines = Source.fromFile("input").getLines.toList
     //It creates a combination one by one between all the elements, them collect those that only have one single different letter 
     val correctBoxId = lines.combinations(2).collect { case List(a,b) if ((a zip b).filter(z => z._1 == z._2).length == lines(0).length -1) => (a zip b) }.toList(0)
     correctBoxId.filter(z => z._1 == z._2).map(x=>print(x._1));
  }  
}