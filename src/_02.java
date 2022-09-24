import java.util.List;
import java.util.ArrayList;

import aoc.common.Solver;
import static aoc.common.InputReader.processInputLines;

public class _02 implements Solver {
    private final List<Command> commands = new ArrayList<>();

    Results solve() {
        var hpos = 0;
        var depth_1 = 0;
        var depth_2 = 0;
        var aim = 0;
        for (final var command : commands) {
            switch (command.direction) {
                case "forward" -> {
                    hpos += command.value;
                    depth_2 +=  aim * command.value;
                }
                case "up" -> {
                    depth_1 -= command.value;
                    aim -=  command.value;
                }
                case "down" -> {
                    depth_1 += command.value;
                    aim +=  command.value;
                }
            }
        }
        return new Results(hpos * depth_1, hpos * depth_2);
    }

    @Override
    public void processLine(String line) {
        final var parts = line.split(" ");
        commands.add(new Command(parts[0], Integer.valueOf(parts[1])));
    }

    private static record Command(String direction, Integer value) {}
    private static record Results(Integer first, Integer second) {}

    public static void main(String[] args) {
        final var solver = new _02();
        processInputLines(args[0], solver);
        final var results = solver.solve();
        System.out.println(results.first);
        System.out.println(results.second);
    }
}
