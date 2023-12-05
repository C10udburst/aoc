import java.io.File

class FancyMap(val chunks: List<List<Long>>) {
    fun get(x: Long): Long {
        for (chunk in chunks) {
            val (destStart, srcStart, length) = chunk
            if (x >= srcStart && x < srcStart + length) {
                return destStart + (x - srcStart)
            }
        }
        return x
    }
}

fun main() {
    var file = File("5.in").bufferedReader()

    var seeds = file
        .readLine()
        .split(":")
        .last()
        .trim()
        .split(" ")
        .map { it.toLong() }

    var maps = file
        .readText()
        .split(":", "\n\n")
        .filterIndexed { i, _ -> i % 2 == 1 }
        .map { it.trim() }
        .map {
            FancyMap(
                it.split("\n")
                    .map { it.trim() }
                    .map { it.split(" ") }
                    .map { it.map { it.toLong() } }
            )
        }

    var locations = mutableMapOf<Long, Long>();
    for (seed in seeds) {
        locations[seed] = seed
        for (map in maps) {
            locations[seed] = map.get(locations[seed]!!)
        }
    }

    var min = locations.values.minOrNull()!!
    println(min)
}