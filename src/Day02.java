import java.util.List;
import java.util.ArrayList;

import aoc.common.InputReader;
import aoc.common.Solver;

public class Day02
{
    private final static class Day02Solver implements Solver
    {
        private final List<Command> commands;

        public Day02Solver() {
            commands = new ArrayList<>();
        }

        public Results solve() {
            Integer hpos = 0;
            Integer depth_1 = 0;
            Integer depth_2 = 0;
            Integer aim = 0;
            for (final Command command : commands) {
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

        public void processLine(String line) {
            final String[] parts = line.split(" ");
            commands.add(new Command(parts[0], Integer.valueOf(parts[1])));
        }
    }

    private static class Command {
        public final String direction;
        public final Integer value;

        public Command(String direction, Integer value) {
            this.direction = direction;
            this.value = value;
        }
    }

    private static class Results {
        public final Integer first;
        public final Integer second;

        public Results(Integer first, Integer second) {
            this.first = first;
            this.second = second;
        }
    }

    public static void main(String[] args) {
        final Day02Solver solver = new Day02Solver();
        InputReader.readLines(args[0], solver);
        final Results results = solver.solve();
        System.out.println(results.first);
        System.out.println(results.second);
    }
}
