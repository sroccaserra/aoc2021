import java.util.List;
import java.util.ArrayList;

import aoc.common.InputReader;
import aoc.common.Solver;

public class _02
{
    private final static class Day02Solver implements Solver
    {
        private final List<Command> commands = new ArrayList<>();

        Results solve() {
            var hpos = 0;
            var depth_1 = 0;
            var depth_2 = 0;
            var aim = 0;
            for (final var command : commands) {
                switch (command.direction) {
                    case "forward":
                        hpos += command.value;
                        depth_2 +=  aim * command.value;
                        break;
                    case "up":
                        depth_1 -= command.value;
                        aim -=  command.value;
                        break;
                    case "down":
                        depth_1 += command.value;
                        aim +=  command.value;
                        break;
                }
            }

            return new Results(hpos * depth_1, hpos * depth_2);
        }

        @Override
        public void processLine(String line) {
            final String[] parts = line.split(" ");
            commands.add(new Command(parts[0], Integer.valueOf(parts[1])));
        }
    }

    private static record Command(String direction, Integer value) {}
    private static record Results(Integer first, Integer second) {}

    public static void main(String[] args) {
        final var solver = new Day02Solver();
        InputReader.readLines(args[0], solver);
        final Results results = solver.solve();
        System.out.println(results.first);
        System.out.println(results.second);
    }
}
