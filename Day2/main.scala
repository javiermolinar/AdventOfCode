import scala.io.Source

object AdventOfCode {
  def main(args: Array[String]): Unit = {   
    //Not an efficient solution
    val lines = Source.fromFile("input").getLines.toList;
    println(lines.filter(x=>countOcurrences(x).exists(y=>y==2)).length *
     lines.filter(x=>countOcurrences(x).exists(y=>y==3)).length)
  }

  def countOcurrences(id:String) : Array[Int] = {
    val ocurrences = Array.fill(26)(0)
    id.map(x=> ocurrences(x-'a')+= 1)
    ocurrences
  }
}