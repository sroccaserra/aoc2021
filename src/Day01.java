import java.io.IOException;
import java.lang.Integer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

import static java.lang.String.format;

public class Day01
{
    private final static class Day01Solver implements Solver
    {
        private final List<Integer> numbers;
        private final static Integer HUGE = 99999;

        public Day01Solver() {
            numbers = new ArrayList<>();
        }

        public Integer solve1() {
            Integer result = 0;
            Integer previous = HUGE;
            for (final Integer n : numbers) {
                if (n > previous) {
                    ++result;
                }
                previous = n;
            }
            return result;
        }

        public Integer solve2() {
            Integer result = 0;
            Integer p1 = HUGE, p2 = HUGE, p3 = HUGE;
            for (final Integer n : numbers) {
                if (n + p1 + p2 > p1 + p2 + p3) {
                    ++result;
                }
                p3 = p2;
                p2 = p1;
                p1 = n;
            }
            return result;
        }

        public void processLine(String line) {
            numbers.add(Integer.valueOf(line));
        }

    }

    public static void main(String[] args) {
        final Day01Solver solver = new Day01Solver();
        InputReader.readLines(args[0], solver);
        System.out.println(format("%d", solver.solve1()));
        System.out.println(format("%d", solver.solve2()));
    }
}

interface Solver {
    void processLine(String line);
}

class InputReader {
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
