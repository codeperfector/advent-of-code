import java.io.File

val out = File("input.txt")
            .readLines()
            .map(String::trim)
            .map(String::toInt)
            .windowed(size=3, step=1, partialWindows=false,transform=List<Int>::sum)
            .windowed(size=2, step=1, partialWindows=false)
            .count {(first, second) -> first < second}


println("lines $out")