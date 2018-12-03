import scala.io.Source

object AdventOfCode {
  def main(args: Array[String]): Unit = { 
   println(calibrate("frecuencies"))
  }
  def calibrate(fileName: String): Int = {
    Source.fromFile(fileName).getLines.foldLeft(0)(_ + _.toInt)
  }
}
