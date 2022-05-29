import Enum, only: [map: 2, reduce: 3]
import IO, only: [puts: 1, read: 2]
import String, only: [split: 3, to_atom: 1, to_integer: 1]

defmodule Day01 do
  def part_1(commands) do
    start = %{hpos: 0, depth: 0}
    %{hpos: hpos, depth: depth} = reduce(commands, start, &apply_command/2)
    hpos * depth
  end

  defp apply_command(command, aState) do
    %{hpos: hpos, depth: depth} = aState

    case command do
      [:forward, val] -> %{aState | hpos: hpos + val}
      [:down, val] -> %{aState | depth: depth + val}
      [:up, val] -> %{aState | depth: depth - val}
    end
  end
end

commands =
  read(:stdio, :all)
  |> split("\n", trim: true)
  |> map(&split(&1, " ", trim: true))
  |> map(fn [dir, val] -> [to_atom(dir), to_integer(val)] end)

puts Day01.part_1(commands)
