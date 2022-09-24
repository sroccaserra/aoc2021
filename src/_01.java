import java.util.ArrayList;
import java.util.List;

import static java.lang.String.format;

import aoc.common.Solver;
import static aoc.common.InputReader.processInputLines;

public class _01 implements Solver {
    private final List<Integer> numbers = new ArrayList<>();
    private final static Integer HUGE = 99999;

    Integer solve1() {
        var result = 0;
        var previous = HUGE;
        for (final var n : numbers) {
            if (n > previous) {
                ++result;
            }
            previous = n;
        }
        return result;
    }

    Integer solve2() {
        var result = 0;
        Integer p1 = HUGE, p2 = HUGE, p3 = HUGE;
        for (final var n : numbers) {
            if (n + p1 + p2 > p1 + p2 + p3) {
                ++result;
            }
            p3 = p2;
            p2 = p1;
            p1 = n;
        }
        return result;
    }

    @Override
    public void processLine(String line) {
        numbers.add(Integer.valueOf(line));
    }

    public static void main(String[] args) {
        final var solver = new _01();
        processInputLines(args[0], solver);
        System.out.println(format("%d", solver.solve1()));
        System.out.println(format("%d", solver.solve2()));
    }
}
