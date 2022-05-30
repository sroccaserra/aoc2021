import Enum, only: [map: 2, reduce: 3]
import IO, only: [puts: 1, read: 2]
import String, only: [split: 3, to_atom: 1, to_integer: 1]

defmodule Day01 do
  def part_1(commands) do
    start = %{hpos: 0, depth: 0}
    stop = reduce(commands, start, &apply_command_1/2)
    stop.hpos * stop.depth
  end

  def part_2(commands) do
    start = %{hpos: 0, depth: 0, aim: 0}
    stop = reduce(commands, start, &apply_command_2/2)
    stop.hpos * stop.depth
  end

  defp apply_command_1(command, aState) do
    %{hpos: hpos, depth: depth} = aState

    case command do
      [:forward, x] -> %{aState | hpos: hpos + x}
      [:down, x] -> %{aState | depth: depth + x}
      [:up, x] -> %{aState | depth: depth - x}
    end
  end

  defp apply_command_2(command, aState) do
    %{hpos: hpos, depth: depth, aim: aim} = aState

    case command do
      [:forward, x] -> %{aState | hpos: hpos + x, depth: depth + aim * x}
      [:down, x] -> %{aState | aim: aim + x}
      [:up, x] -> %{aState | aim: aim - x}
    end
  end
end

commands =
  read(:stdio, :all)
  |> split("\n", trim: true)
  |> map(&split(&1, " ", trim: true))
  |> map(fn [dir, val] -> [to_atom(dir), to_integer(val)] end)

puts Day01.part_1(commands)
puts Day01.part_2(commands)
