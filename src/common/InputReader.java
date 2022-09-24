package aoc.common;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class InputReader {
    public static void processInputLines(String filename, Solver solver) {
        final var path = Paths.get(filename);
        try (final var lines = Files.lines(path)) {
            lines.forEachOrdered(solver::processLine);
        }
        catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
