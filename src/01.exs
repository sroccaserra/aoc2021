import Enum, only: [count: 2, map: 2, zip: 2]
import IO, only: [puts: 1, read: 2]
import String, only: [split: 3, to_integer: 1]

defmodule Day01 do
    def part_1(numbers) do
        zip(tl(numbers), numbers)
        |> count(fn {left, right} -> left > right end)
    end
end

numbers = read(:stdio, :all)
    |> split("\n", trim: true)
    |> map(&(to_integer(&1)))

puts Day01.part_1(numbers)
