import java.io.File
import java.util.Collections

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
        .zipWithNext()
        .filterIndexed { i, _ -> i % 2 == 0 }

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

    var minThreaded = Collections.synchronizedList(mutableListOf<Long>())
    seeds.parallelStream().forEach { (firstSeed, length) ->
        var min = Long.MAX_VALUE
        println("Starting ${firstSeed}..${firstSeed + length} (${length}) on ${Thread.currentThread().name}")
        for (seed in firstSeed..firstSeed + length) {
            var location = seed
            for (map in maps) {
                location = map.get(location)
            }
            if (location < min) {
                min = location
            }
        }
        minThreaded.add(min)
        println("Finished ${firstSeed}..${firstSeed + length} (${length}) on ${Thread.currentThread().name}")
    }

    var min = minThreaded.minOrNull()!!

    println(min)
}