package aoc.common;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class InputReader {
    public static void readLines(String filename, Solver solver) {
        final Path path = Paths.get(filename);
        try (final Stream<String> lines = Files.lines(path)) {
            lines.forEachOrdered(line -> solver.processLine(line));
        }
        catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
